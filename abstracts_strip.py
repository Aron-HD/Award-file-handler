import logging
import sys
from glob import iglob
from pathlib import Path

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

logger = setup_custom_logger(r'Abstracts cleanup\log.txt')

def stripchars(target_folder):
	"""
	Finds and replaces incompatible characters within all 
  	.txt files in the '\abstracts' directory.
  	"""
	for filepath in iglob(target_folder, recursive=True):
		p = Path(filepath)
		fn = p.parts[-1]

		with open(filepath, encoding='1252') as file:
			logger.info(f'read: {fn}')
			for line in file:
				output = line.strip().replace("Ð", "–").replace("Õ", "'").replace("Ô", "'").replace("Ž", "é").replace("Ò", "'").replace("Ó", "'").replace("ª", "™").replace("’", "'").replace("‘", "'")
				# only write back the block paragraph by stripping other shorter lines
				if len(output) >= 7:
					with open(filepath, 'w') as file:
						try:
							file.write(output)
							logger.info(f'write {fn}')
						except Exception as e:
							logger.error(e)
							continue

def renameid(target_folder):
	"""Renames files, stripping anything from filename after ID."""
	for filepath in iglob(target_folder, recursive=True):
		p = Path(filepath)
		new = f"{p.stem[0:6]}{p.suffix}"
		try:
			p.rename(Path(p.parent, new))
			logger.info(new)
		except Exception as e:
			logger.error(e)
			continue

def main():
	"""
	stripchars()
	- Finds and replaces incompatible characters within all 
	  .txt files in the '\abstracts' directory. 

	renameid()
	- Renames files, stripping anything from filename after ID.
	"""
	target_folder = r'Abstracts cleanup\abstracts\*.txt'
	
	try:
		stripchars(target_folder)
	except Exception as e:
		print(e)
		pass

	# renameid(target_folder)

if __name__ == '__main__':
	main()

# Ž = é
# Ð = –
# Õ , Ò , Ó , Ô = '
# ª = ™
