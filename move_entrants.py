import pandas as pd
from compile_papers import file_copier, file_mover
from pathlib import Path
from glob import glob

path = r'T:\Ascential Events\WARC\Backup Server\Loading\Monthly content for Newgen\Project content - March 2020\WARC Awards 2020'
excel_file = Path(path) / 'WARC Awards_EDIT.xlsx'

# main spreadsheet

cat_list = ['1. Innovation', '2. Purpose', '3. Content', '4. Social'] # make into dict, for other categories ['Shortlist', 'Channel', 'Data', 'Tech', 'P&S']

def sort_files(*args):

	# get all the ids from different tabs if they exist
	try:
		# Shortlists
		shortlisted = []
		for i in cat_list:
			df = pd.read_excel(excel_file, i)
			x = df['ID'].tolist()
			shortlisted.append((i, x))
			print(f'{i}: {len(x)}\n', x)
		# Dupes
		df = pd.read_excel(excel_file, 'Dupes')
		dupes = df['ID'].tolist()
		print(f'dupes: {len(dupes)}\n', dupes)
		# Murkies
		df = pd.read_excel(excel_file, 'Murkies')
		murkies = df['ID'].tolist()
		print(f'murkies: {len(murkies)}\n', murkies)
		# Entry, Category
		df = pd.read_excel(excel_file, 'Entries')
		entries = df['ID'].tolist()
		categories = df['Category'].tolist()
		print(f'entries: {len(entries)}\n', entries)
		all_ents = zip(entries, categories)
	except Exception as e:
		print(e)
		pass

	# split into separate functions
	destinations = {
	'Effective Innovation': '1. Innovation',
	'Effective Use of Brand Purpose': '2. Purpose',
	'Effective Content Strategy': '3. Content',
	'Effective Social Strategy': '4. Social'
	}

	try:
		for ID, cat in all_ents:
			if ID in murkies:

				# move murkies docxs
				print('MURKIES - DOCXS')
				docx_mrk = glob(fr'{path}\\Returned papers & abstracts\\**\\{ID}*.docx', recursive=True)
				if len(docx_mrk) > 0:
					dn = destinations[cat]
					dst = path + fr'\\edited papers\\murkies\\{dn}'
					file_copier(docx_mrk[0], dst)
					print(f'copied {ID}.docx -> ', dst)

				# move murkies abstracts
				print('MURKIES - ABSTRACTS')
				abs_mrk = glob(fr'Abstracts cleanup\\abstracts\\**\\{ID}*.txt', recursive=True)
				if len(abs_mrk) > 0: # to catch empty dupes (which have no corresponding file for id)
					dn = destinations[cat] # matches IDs category with correct folder
					dst = path + fr'\\abstracts\\murkies\\{dn}'
					file_mover(abs_mrk[0], dst)
					print(f'moved {ID}.txt -> ', dst)


			# currently this copies everything and doesn't pickup shortlisted
			# need to access the values within the lists for each key in shortlisted
			if not ID in shortlisted:
				# move entrants docxs
				print('ENTRANTS - DOCXS')
				docx_ent = glob(fr'{path}\\Returned papers & abstracts\\**\\{ID}*.docx', recursive=True)
				if len(docx_ent) > 0:
					dn = destinations[cat]
					dst = path + fr'\\edited papers\\entrants\\{dn}'
					file_copier(docx_ent[0], dst)
					print(f'copied {ID}.docx -> ', dst)

				# move entrant abstracts
				print('ENTRANTS - ABSTRACTS')
				abs_ent = glob(fr'Abstracts cleanup\\abstracts\\**\\{ID}*.txt', recursive=True)
				if len(abs_ent) > 0: # to catch empty dupes (which have no corresponding file for id)
					dn = destinations[cat] # matches IDs category with correct folder
					dst = path + fr'\\abstracts\\entrants\\{dn}'
					file_mover(abs_ent[0], dst)
					print(f'moved {ID}.txt -> ', dst)

			elif ID in shortlisted:
				pass

	except Exception as e:
		print(e)
		pass

def main():
	sort_files()
	# list_ids()

if __name__ == '__main__':
	main()
	# files = [r'T:\Ascential Events\WARC\Backup Server\Loading\Monthly content for Newgen\Project content - March 2020\WARC Awards 2020\\Returned papers & abstracts\Sue\131400_social.docx',]

	# for i in cat_list:
	# 	if i.split(' ')[1].lower() in file.split('\\')[-1]:
	# 		print(i)
