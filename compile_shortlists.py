import pandas as pd
from glob import iglob
from pathlib import Path

def main():
	'''
	grabs the sheet called 'Shortlist' from 
	every 'consolidated marks.xslx' excel sheet
	in the folder stated through input.
	'''
	
	# user input path to '{category} - consolidated marks.xlsx' file
	path = input('paste folder path: ') # logger.info('user input: ' + path)

	# filter only xlsx files in the path that have 'consolidated' in the filename
	files = iglob(fr'{path}\\*consolidated*.xlsx')

	# make a new directory for shortlists if it doesn't already exist
	newdir = path + '\\Shortlists'
	if not Path(newdir).is_dir(): # logger.info()
		newdir.mkdir() # logger.info("")

	# Create a Pandas Excel writer using XlsxWriter as the engine.
	all_shortlists = pd.ExcelWriter(fr'{newdir}\\all_shortlists.xlsx', engine='xlsxwriter') # logger.info("making new file 'all_shortlists.xlsx'")

	try:
		for file in files:
			p = Path(file)
			# define just filename
			f = p.parts[-1] # logger.info("")
			# define name for each sheet in new 'all_shortlists.xlsx' by removing '- consolidated marks.xlsx' from filename to get category
			sheetname = f.split(' - ')[0] 
			# define filename for each individual csv file by appending '_shortlist_test.csv' to category info through sheetname
			nf = sheetname + '_shortlist_test.csv'
			# make csv files in correct folder
			csvf = f'{newdir}\\{nf}'

			try:
				# read each xlsx file
				df = pd.read_excel(file, 'Shortlist') # logger.info("")

				# Write each dataframe to a separate sheet in 'all_shortlists.xlsx'
				df.to_excel(all_shortlists, sheet_name=sheetname, index=False) # logger.info("")

				# write each dataframe to a separate csv file in 'Shortlists folder', removing the index
				df.to_csv(csvf, index=False) # logger.info("")
				print(f)
				print(nf)

			except Exception as e:
				# print file and exception
				print('\tx ' + f)
				print("\n\t- Ensure consolidated marks excel files have a tab called 'Shortlist'")
				print(e)

	except Exception as e:
		print("\n\t- Ensure path is correct")
		print(e) # logger.error(e)
	# Close the Pandas Excel writer and output the Excel file.
	all_shortlists.save() # logger.info("saved 'all_shortlists.xlsx'")

if __name__ == '__main__':
	main()