from glob import iglob
from pathlib import Path
import csv
from shutil import move, copy
import logging
import sys

# input('paste location of csv shortlists: ')
csv_path = r'T:\Ascential Events\WARC\Public\WARC.com\Editorial\Awards (Warc)\2020 Awards\1. WARC Awards\Scoresheets back from judges\Shortlists'
csv_files = iglob(fr'{csv_path}\\*.csv')
# input('paste destination location: ')
path = r'T:\Ascential Events\WARC\Backup Server\Loading\Monthly content for Newgen\Project content - March 2020\WARC Awards 2020'

def setup_custom_logger(name):
    formatter = logging.Formatter(fmt='%(asctime)s %(levelname)-8s %(message)s',
                                  datefmt='%d-%m-%Y %H:%M:%S')
    handler = logging.FileHandler(name, mode='w')
    handler.setFormatter(formatter)
    screen_handler = logging.StreamHandler(stream=sys.stdout)
    screen_handler.setFormatter(formatter)
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    logger.addHandler(screen_handler)
    return logger

logger = setup_custom_logger('logs/compile-papers.log')

def file_copier(file, dst):

	if not 'MARKUP' in file: # skips duplicated markup docs
		fn = file.split('\\')[-1]
		try:
			copy(file, f'{dst}\\{fn}')
			logger.info(fn)
		except Exception as e:
			logger.error(e)
			# continue

def file_mover(file, dst):
	
	fn = file.split('\\')[-1]
	try:
		move(file, f'{dst}\\{fn}')
		logger.info(fn)
	except Exception as e:
		logger.error(e)
		# continue

def check_dirs():
	pass

def main():
	'''moves or copies assets for shortlisted entries only'''

	select = int(input('''

		- '1' for docx 
		- '2' for pdfs
		- '3' for abstracts
		
		> select: '''))

	if select not in range(1,4):
		print('\n\t- incorrect input')
		main()
	else:
		logger.info(f"checking dirs exist in '{path}'...")
		for f in csv_files:
			# this will become the new directory name
			dn = f.split('\\')[-1].split('_')[0].replace('.csv', '')

			# destination directories
			# SHORTLISTS
			docx_dst = path + fr'\\edited papers\\shortlisted\\docs\\{dn}'
			pdf_dst = path + fr'\\edited papers\\shortlisted\\pdfs\\{dn}'
			abs_dst = path + fr'\\abstracts\\shortlisted\\{dn}'
			# ENTRANTS
			ent_docx_dst = path + fr'\\edited papers\\entrants\\{dn}'
			ent_abs_dst = path + fr'\\abstracts\\entrants\\{dn}'
			# MURKIES
			mrk_docx_dst = path + fr'\\edited papers\\murkies\\{dn}'
			mrk_abs_dst = path + fr'\\abstracts\\murkies\\{dn}'

			destinations = [docx_dst, pdf_dst, abs_dst, ent_docx_dst, ent_abs_dst, mrk_abs_dst, mrk_docx_dst]

			logger.info(f'### {dn} ###')

			for dst in destinations:
				dst = Path(dst)
				if not dst.is_dir():
					dst.mkdir(parents=True, exist_ok=True)
					print('made dir:', str(dst).split('\\')[-3:])
					
			logger.info('dir check finished')
			#
			try:
				with open(f, newline='') as csvf:
					r = csv.DictReader(csvf)
					for row in r:
						# catch blank rows 
						if len(row['ID']) > 3:
							ID = row['ID']
							docx_file = iglob(fr'{path}\\Returned papers & abstracts\\**\\{ID}*.docx', recursive=True)
							pdf_file = iglob(fr'{path}\\Judges papers\\**\\*{ID}*.pdf', recursive=True)
							txt_file = iglob(fr'Abstracts cleanup\\abstracts\\{ID}*.txt', recursive=True)

							if select == 1:
								pass
								# file_copier(docx_file, docx_dst)
							elif select == 2:
								pass
								# file_copier(pdf_file, pdf_dst)
							elif select == 3:
								# file_mover(txt_file, abs_dst)
								pass

			except Exception as e:
				logger.error(e)
				logger.info('no csv files in path')

if __name__ == '__main__':
	main()


## OLD CODE ##

# def shortlisted_docxs():

# 	for f in csv_files:
# 		# this will become the new directory name
# 		dn = f.split('\\')[-1].split('_')[0].replace('.csv', '')
# 		print(dn)

# 		# creates new directories if they don't exist
# 		docx_dst = path / fr'Shortlisted papers\\edited docs\\{dn}'

# 		if not Path(docx_dst).is_dir():
# 			docx_dst.mkdir(parents=True, exist_ok=True)

# 		with open(f, newline='') as csvf:
# 			r = csv.DictReader(csvf)
# 			for row in r:
# 				# catch blank rows 
# 				if len(row['ID']) > 3:
# 					ID = row['ID']
# 					# this is weak because of folder naming
# 					docx_files = iglob(fr'{path}\\Returned papers & abstracts\\**\\{ID}*.docx', recursive=True)
# 					for file in docx_files:
# 						p = Path(file)
# 						fn = p.parts[-1]

# 						if not 'MARKUP' in fn:

# 							try:
# 								copy(file, f'{docx_dst}\\{fn}')
# 								print(fn)
# 							except Exception as e:
# 								logger.error(e)
# 								continue

# def shortlisted_pdfs():

# 	for f in csv_files:
# 		# this will become the new directory name
# 		dn = f.split('\\')[-1].split('_')[0].replace('.csv', '')
# 		print(dn)

# 		# creates new directories for pdfs if they don't exist
# 		pdf_dst = path / fr'Shortlisted papers\\pdfs\\{dn}'

# 		if not Path(pdf_dst).is_dir():
# 			pdf_dst.mkdir(parents=True, exist_ok=True)

# 		with open(f, newline='') as csvf:
# 			r = csv.DictReader(csvf)
# 			for row in r:
# 				# catch blank rows 
# 				if len(row['ID']) > 3:
# 					ID = row['ID']
# 					# this is weak because of folder naming
# 					pdf_files = iglob(fr'{path}\\Judges papers\\**\\*{ID}*.pdf', recursive=True)

# 					for file in pdf_files:
# 						p = Path(file)
# 						fn = p.parts[-1]

# 						try:
# 							copy(file, f'{pdf_dst}\\{fn}')
# 							print(fn)
# 						except Exception as e:
# 							logger.error(e)
# 							continue