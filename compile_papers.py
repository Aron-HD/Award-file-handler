from glob import iglob
from pathlib import Path
import csv
import shutil
from os import chdir

# make this input maybe? input('paste location of csv shortlists: ')
csv_path = r'T:\Ascential Events\WARC\Public\WARC.com\Editorial\Awards (Warc)\2020 Awards\1. WARC Awards\Scoresheets back from judges\Shortlists'
csv_files = iglob(fr'{csv_path}\\*.csv')
path = r'T:\Ascential Events\WARC\Backup Server\Loading\Monthly content for Newgen\Project content - March 2020\WARC Awards 2020'

def each_id():

	for f in csv_files:
		# this will become the directory name
		dn = f.split('\\')[-1].split('_')[0].replace('.csv', '')
		print(dn)

		# creates new directories if they don't exist
		newdir = Path.cwd() / fr'Shortlisted papers\\edited docs\\{dn}'
		if not Path(newdir).is_dir():
			newdir.mkdir(parents=True, exist_ok=True)

		with open(f, newline='') as csvf:
			r = csv.DictReader(csvf)
			for row in r:
				# catch blank rows 
				if len(row['ID']) > 3:
					ID = row['ID']
					# should this be indented?
					# this is weak because of folder naming
					docx_files = iglob(fr'{path}\\Returned papers & abstracts\\**\\{ID}*.docx', recursive=True)
					for file in docx_files:
						fn = file.split('\\')[-1]
						if not 'MARKUP' in fn:

							try:
								shutil.copy(file, f'Shortlisted papers\\edited docs\\{dn}\\{fn}')
								print(fn)
							except Exception as e:
								print(e)

def each_ref():

	for f in csv_files:
		# this will become the directory name
		dn = f.split('\\')[-1].split('_')[0].replace('.csv', '')
		print(dn)

		# creates new directories if they don't exist
		newdir = Path.cwd() / fr'Shortlisted papers\\pdfs\\{dn}'
		if not Path(newdir).is_dir():
			newdir.mkdir(parents=True, exist_ok=True)

		with open(f, newline='') as csvf:
			r = csv.DictReader(csvf)
			for row in r:
				# catch blank rows 
				if len(row['ID']) > 3:
					ID = row['ID']
					# should this be indented?
					# this is weak because of folder naming
					pdf_files = iglob(fr'{path}\\Judges papers\\**\\*{ID}*.pdf', recursive=True)
					for file in pdf_files:
						fn = file.split('\\')[-1]

						try:
							shutil.copy(file, f'Shortlisted papers\\pdfs\\{dn}\\{fn}')
							print(fn)
						except Exception as e:
								print(e)
				

def main():
	
	print(f"Original directory: '{Path.cwd()}'")

	try:
	    # change directory to the path inputed
	    chdir(path)
	    print(fr'Changed directory')

	except Exception as e:
	    # print exceptions
	    print(f"Couldn't access path: '{path}'\n ensure you've pasted a valid folder path") # print, not log
	    print(e)

	print(f"Current directory: '{Path.cwd()}'")

	select = int(input('''

		- '1' for docx 
		- '2' for pdfs
		
		> select: '''))

	if select == 1:
		each_id()
	elif select == 2:
		each_ref()
	else:
		main()



	# print(each_ref()) # why doesn't this work?
	# pprint()
	# pprint(pdf_shortlist())

if __name__ == '__main__':
	main()
