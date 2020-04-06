from shutil import move, Error
from glob import glob
import os

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
			mkdir(dst)
			move_file(file, dst)
		else:
			move_file(file, dst)

def dir_handler():
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
		'zips': ['.zip'] # don't move '.rar' files because can't unrar them yet
	}

	inpath = input('paste folder path: ')

	path = inpath + r'\dropbox assets\temp\*'
	zip_path = inpath + r'\dropbox assets' # zips are in the previous folder

	for key, value in dictionary.items():
		if key != 'zips':
			for i in value:
				extensions(i, path, key)
		elif key == 'zips':
			# pass
			for i in value:
				extensions(i, zip_path, key)

	dir_handler()


if __name__ == '__main__':
	main()
	

