import pandas as pd
from compile_papers import file_copier, file_mover
from pathlib import Path
from glob import glob

# input
path = r'T:\Ascential Events\WARC\Backup Server\Loading\Monthly content for Newgen\Project content - March 2020\WARC Awards 2020'
# main spreadsheet
excel_file = Path(path) / 'WARC Awards_EDIT.xlsx'

cat_list = ['1. Innovation', '2. Purpose', '3. Content', '4. Social'] # make into dict, for other categories ['Shortlist', 'Channel', 'Data', 'Tech', 'P&S']

def list_ids(*args):
	'''
	- make sure tabs are correctly named in '{AWARD}_EDIT.xlsx'
	- gets all the ids from different tabs if they exist
	- could pass all of this to one dict in a more pythonic way [{i:[v]},]
	'''
	try:
		# Entry, Category
		df = pd.read_excel(excel_file, 'Entries')
		entries = df['ID'].tolist() # might want to ensure these are int
		categories = df['Category'].tolist()
		print(f'entries: {len(entries)}')
		all_ents = zip(entries, categories)			
		# Dupes
		df = pd.read_excel(excel_file, 'Dupes')
		dupes = df['ID'].tolist()
		print(f'dupes: {len(dupes)}')
		# Murkies
		df = pd.read_excel(excel_file, 'Murkies')
		murkies = df['ID'].tolist()
		print(f'murkies: {len(murkies)}')
		# Shortlists
		all_shortlisted = []
		shortlists = []
		for i in cat_list:
			df = pd.read_excel(excel_file, i) # reads corresponding shortlist tabs in main xl file
			x = df['ID'].tolist()
			shortlists.append((i, x))
			[all_shortlisted.append(i) for i in x]
			print(f'{i}: {len(x)}')

		entrants = []
		[entrants.append(i) for i in entries if not i in dupes if not i in murkies if not i in all_shortlisted]

		print(f'entrants: {len(entrants)}')

		sort_files(all_ents, murkies, dupes, all_shortlisted, entrants)

	except Exception as e:
		print(e)

def sort_files(all_ents, murkies, dupes, all_shortlisted, entrants):

	destinations = {
	'Effective Innovation': '1. Innovation',
	'Effective Use of Brand Purpose': '2. Purpose',
	'Effective Content Strategy': '3. Content',
	'Effective Social Strategy': '4. Social'
	}

	try:
		for ID, cat in all_ents:
			if ID in all_shortlisted:
				print('shortlisted -', ID)

			else:
				if ID in murkies:

					# move murkies docxs
					docx_mrk = glob(fr'{path}\\Returned papers & abstracts\\**\\{ID}*.docx', recursive=True)
					if len(docx_mrk) > 0: # to catch empty dupes (which have no corresponding file for id)
						dn = destinations[cat] # matches IDs category with correct category folder
						dst = path + fr'\\edited papers\\murkies\\{dn}'
						# file_mover(docx_mrk[0], dst)
						print(f'moved {ID}.docx -> ', dst.split('\\')[-3:])

					# move murkies abstracts
					abs_mrk = glob(fr'Abstracts cleanup\\abstracts\\**\\{ID}*.txt', recursive=True)
					if len(abs_mrk) > 0:
						dn = destinations[cat]
						dst = path + fr'\\abstracts\\murkies\\{dn}'
						# file_mover(abs_mrk[0], dst)
						print(f'moved {ID}.txt -> ', dst.split('\\')[-3:])

				if ID in entrants:
					# move entrants docxs
					docx_ent = glob(fr'{path}\\Returned papers & abstracts\\**\\{ID}*.docx', recursive=True)
					if len(docx_ent) > 0:
						dn = destinations[cat]
						dst = path + fr'\\edited papers\\entrants\\{dn}'
						# file_mover(docx_ent[0], dst)
						print(f'moved {ID}.docx -> ', dst.split('\\')[-3:])

					# move entrants abstracts
					abs_ent = glob(fr'Abstracts cleanup\\abstracts\\**\\{ID}*.txt', recursive=True)
					if len(abs_ent) > 0:
						dn = destinations[cat]
						dst = path + fr'\\abstracts\\entrants\\{dn}'
						# file_mover(abs_ent[0], dst)
						print(f'moved {ID}.txt -> ', dst.split('\\')[-3:])

	except Exception as e:
		print(e)
		pass

if __name__ == '__main__':
	list_ids()

