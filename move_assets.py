from shutil import move, Error
from glob import glob
from pathlib import Path
import os, PySimpleGUI as sg


def move_file(file, dst):
	"""Move file to a destination = move_file(file, dst)"""

	fn = file.split('\\')[-1]

	try:
		move(file, dst)
		print(f"\t>'{fn}'")
	except Exception as error:
		print(f"\nx already exists '{fn}'\n")
		pass
		
def extensions(ext, path, dst):
	"""Pass in extension, path to file and destination"""

	print(f'\n\t- moved: {ext} -> "{dst}"\n')

	for file in glob(rf'{path}\*{ext}'):
		
		if not os.path.exists(dst): # so that we don't send files to hell
			os.mkdir(dst)
			move_file(file, dst)
		else:
			move_file(file, dst)

def dir_handler(path):
	"""Delete all empty folders, print remaining""" # add logging

	for d in os.listdir(path[:-2]): # to remove '\*'
		if d != '_tmp':
			try:
				os.rmdir(fr'{path[:-2]}\\{d}')
				# make a new temp folder, catching errors if you are in the folder, or it already exists
				# os.mkdir(f'{path[:-2]}\\tmp')
			except (OSError, FileExistsError, PermissionError) as e:
				print('\nRemaining folders:') 
				print(f'\n- {d} is not empty\n') # keep any dirs with files in

def main():

	dictionary = {
		'surveys': ['_survey.docx'],
		'entry forms': ['.docx', '.pdf'], 
		'videos': ['.mov', '.mp4', '.avi', '.m4v'],
		'zips': ['.zip', '.rar']
	}

	sg.theme('DarkPurple4')
	
	layout = [
		# [sg.Output(size=(42,5))],
		[sg.Text('Paste a path here:')],
		[sg.InputText()],
		[sg.Submit(), sg.Cancel()]
	]

	window = sg.Window(
		'Awards Setup',
		layout,
		# icon=icon_file,
		keep_on_top=True,
		grab_anywhere=True
	) 

	while True:
		event, values = window.read()

		if event in ('Cancel', None):
			break

		if event == 'Submit':
			try:
				if len(values[0]) > 2:
					path = values[0]

					if Path(path).is_dir():

						p = Path(path)
						print('working in path:\n', p)
						
						fpath = path + r'\dropbox assets\temp\*'
						zip_path = path + r'\dropbox assets' # zips are in the previous folder

						for key, value in dictionary.items():
							if key != 'zips':
								for i in value:
									extensions(i, fpath, f'{path}/{key}')
							elif key == 'zips':
								for i in value:
									extensions(i, zip_path, f'{path}/{key}')

						dir_handler(fpath)

			except Exception as e:
				raise e
				
	window.close()

if __name__ == '__main__':
	main()
	

