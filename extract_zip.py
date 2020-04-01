from glob import glob
from zipfile import ZipFile, BadZipFile
# from rarfile import RarFile # needs unrar added to Path

def extract_file(extensions, path):

	for ext in exts: 
		for file in glob(fr'{path}\*.{ext}'):
			fn = file.split('\\')[-1]
			print(f"\t- unzipping '{fn}'")
			try:
				with ZipFile(file, 'r') as zf:
					zf.extractall(rf'.\dropbox assets\temp')
					# print('\t- done')
			except BadZipFile:
				print(f"'{file}' is not a zip file")
				pass

			# if ext == 'rar':
			# 	try:
			# 		with RarFile(file, 'r') as rf:
			# 			# print(f"\t- unzipping '{fn}'")
			# 			rf.extractall(rf'.\dropbox assets\temp')
			# 	except BadZipFile:
			# 		print(f"'{file}' is not a zip file")
			# 		pass
			# print('\t- done')

	print('\nFinished!')

if __name__ == '__main__':

	path = r'.\dropbox assets'
	exts = ['zip'] # , 'rar'

	extract_file(exts, path)
