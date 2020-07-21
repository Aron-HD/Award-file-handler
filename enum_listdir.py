from glob import iglob
from natsort import natsorted as nat
from pathlib import Path
from shutil import copy, move

def list_docxs(path):
	[print(f) for f in enumerate([Path(file).parts[-1] for file in nat(iglob(fr'{path}\\**\\*.docx', recursive=True))], start=1)]

def list_txts(path):
	files = nat(iglob(fr'{path}\\**\\*.txt', recursive=True))

	[print('[' + str(file[0]) + '] \t- ' + file[1])
	for file in enumerate([Path(file).parts[-1] for file in files])]

	return files

def list_vids(path):
	files = nat(iglob(fr'{path}\\**\\*', recursive=True))

	[print('[' + str(file[0]) + '] \t ' + file[1]) for file in enumerate(
		[Path(file).parts[-1] for file in files], 1
		, start=1) if [i for i in ['.mov', '.mp4', '.avi', '.m4v']] not in file]

	return files

def copy_file(files, dst):
	for file in enumerate(files):
		p = Path(file[-1])

		print('[' + str(file[0]) + '] \t ' + file[1])
		# copy(p, dst)
		# move(p, dst)

def main():

	# path = input("paste folder path: ")

	path = r'D:\2020 Awards\2020 3. Asia Prize\entry forms'

	# path2 = r'D:\2020 Awards\2020 3. Asia Prize\videos'

	vid_path = r'D:\2020 Awards\2020 3. Asia Prize\videos'

	# dst_dir = r'Abstracts cleanup\abstracts'

	print('Num		File')

	# move_file(list_txts(path2), dst_dir)

	list_docxs(path)

	# list_vids(vid_path)

if __name__ == '__main__':
	main()