from glob import glob
import shutil
import os

dirs = ['purpose', 'content', 'social', 'innovation']

for d in dirs:
	if not os.path.exists(rf'.\\entry forms\\{d}'):
		os.mkdir(rf'.\\entry forms\\{d}')

for file in glob(rf'.\entry forms\*pur*.docx'):
	dst = rf'.\entry forms\purpose'
	shutil.move(file, dst)
	print(f"\t- moved '{file}' -> 'purpose'")

for file in glob(rf'.\entry forms\*con*.docx'):
	dst = rf'.\entry forms\content'
	shutil.move(file, dst)
	print(f"\t- moved '{file}' -> 'content'")

for file in glob(rf'.\entry forms\*soc*.docx'):
	dst = rf'.\entry forms\social'
	shutil.move(file, dst)
	print(f"\t- moved '{file}' -> 'social'")

for file in glob(rf'.\entry forms\*in*.docx'):
	dst = rf'.\entry forms\innovation'
	shutil.move(file, dst)
	print(f"\t- moved '{file}' -> 'innovation'")

for file in glob(rf'.\entry forms\*survey*.docx'):
	dst = rf'.\surveys'
	shutil.move(file, dst)
	print(f"\t- moved '{file}' -> 'surveys'")

