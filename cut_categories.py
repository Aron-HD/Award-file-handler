from glob import iglob
from pathlib import Path

def all_exts(target_folder):
	"""
	- Option 1: Renames all files in the specified folder
	"""

	for filepath in iglob(fr'{target_folder}\*', recursive=True):
		p = Path(filepath)
		new = f"{p.stem[0:6]}{p.suffix}"
		try:
			p.rename(Path(p.parent, new))
			print(new)
		except Exception as e:
			print(e)

def specific_exts(target_folder, exts):
	"""
	- Option 2 renames only files with specified extensions,
	  which must be separated by a space.
	"""

	for ext in exts:
		for filepath in iglob(fr'{target_folder}\*.{ext}', recursive=True):
			p = Path(filepath)
			new = f"{p.stem[0:6]}{p.suffix}"
			try:
				p.rename(Path(p.parent, new))
				print(new)
			except Exception as e:
				print(e)

def main():
	"""
	- Renames files, stripping anything from filename after ID.
	- Option 1 renames all files in the specified folder
	- Option 2 renames only files with specified extensions,
	  which must be separated by a space.
	"""

	print('  USE WITH CAUTION!\n')
	target_folder = input('- Paste folder path: ')
	selection = int(input("""
	# Select option
	- '1' = all files
	- '2' = specific extension/s
	> Type '1' or '2': """))

	if selection == 1:
		try:
			all_exts(target_folder)
		except Exception as e:
			print(e)
			main()

	if selection == 2:
		exts = map(str,input('- Specify extensions seperated by a space: ').split())
		try:
			specific_exts(target_folder, exts)
			main()
		except Exception as e:
			print(e)
			main()

if __name__ == '__main__':
	main()