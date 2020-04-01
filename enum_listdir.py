from glob import iglob
from natsort import natsorted as nat
from pathlib import Path
from shutil import copy, move

def list_docxs(path):
	[print(f) for f in enumerate([Path(file).parts[-1] for file in nat(iglob(fr'{path}\\**\\*.docx', recursive=True))])]

def list_txts(path):
	files = nat(iglob(fr'{path}\\**\\*.txt', recursive=True))

	[print('[' + str(file[0]) + '] \t- ' + file[1])
	for file in enumerate([Path(file).parts[-1] for file in files])]

	return files

def list_vids(path):
	files = nat(iglob(fr'{path}\\**\\*', recursive=True))

	[print('[' + str(file[0]) + '] \t- ' + file[1]) for file in enumerate(
		[Path(file).parts[-1] for file in files]
		) if [i for i in ['.mov', '.mp4', '.avi', '.m4v']] not in file]

	return files

def copy_file(files, dst):
	for file in enumerate(files):
		p = Path(file[-1])

		print('[' + str(file[0]) + '] \t- ' + file[1])
		# copy(p, dst)
		# move(p, dst)

def main():

	# path = input("paste folder path: ")

	path = r'T:\Ascential Events\WARC\Backup Server\Loading\Monthly content for Newgen\Project content - March 2020\WARC Awards 2020\_Raw papers'

	path2 = r'T:\Ascential Events\WARC\Backup Server\Loading\Monthly content for Newgen\Project content - March 2020\WARC Awards 2020\Returned papers & abstracts'

	vid_path = r'T:\Ascential Events\WARC\Backup Server\Loading\Monthly content for Newgen\Project content - March 2020\WARC Awards 2020\Videos'

	dst_dir = r'Abstracts cleanup\abstracts'

	print('''\
  Num 	|	File
------------------\
''')

	# move_file(list_txts(path2), dst_dir)

	# list_docxs(path)

	list_vids(vid_path)

if __name__ == '__main__':
	main()