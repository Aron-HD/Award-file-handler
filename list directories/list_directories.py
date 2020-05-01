import os, pandas as pd
from glob import glob
from natsort import natsorted as nat
from subprocess import call, Popen


def main():
	'''
	lists all directories recursively in a given root folder
	and creates a csv with each folder as a header with files
	listed below.
	'''
	path = input('- paste folder path: ') # 

	dirs = (glob(path + r'\\**\\*', recursive=True))

	# zips folders as keys and lists of files as values
	dic = dict(zip(
			(directory.split('\\')[-1] for directory in dirs if os.path.isdir(directory)), 
			[nat(os.listdir(directory)) for directory in dirs if os.path.isdir(directory)]
			))

	df = pd.DataFrame({ key:pd.Series(value, dtype=str) for key, value in dic.items() })

	# write to csv file
	df.to_csv('listed_dirs.csv', index=False)

	# open in Excel
	# p = subprocess.Popen('listed_dirs.csv', shell=True)

	# open in powershell gridViewer
	print('\nPress enter to exit')
	call("powershell -NoExit Import-Csv listed_dirs.csv | Out-GridView; Read-Host -Prompt “Press Enter to exit”; exit")

if __name__ == '__main__':
	main()
