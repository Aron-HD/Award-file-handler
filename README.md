# AWARD FILE HANDLER

Handles downloaded assets for awards entries and sorts them, separates shortlisted and winning papers and abstracts from other entries.

---
### EDITED ASSETS
---

#### *abstracts_strip.py*
Inititates a find and replace on special characters that cause encoding issues within our CMS and also removes unwanted whitespace to leave only a single block paragraph, so that abstract bullet points are generated correctly.

#### *compile_shortlists.py*
After judges scoresheets are returned and the shortlists are calculated from the '... - consolidated marks.xlsx' files, this script copies the tab titled 'Shortlist' from each workbook and exports them into a folder called '/Shortlists' as both individual csv files and one compiled xlsx file with a tab for each category.

#### *compile_papers.py*
After papers have come back from editors, this uses the csv files created by 'compile_csvs.py' to do two things:

1. copy the edited versions of the shortlisted papers from the relevant folders in the drive (something like '/Returned papers & abstracts')
2. grab the shortlisted pdfs from the pdfs sent to judging groups in the first round and copy them to a '/pdfs' folder

Currently it copies the files to avoid them being sent to a location that doesn't exist, but as I become more confident in the reliability of the script it will move them (using shutil module) instead.

Copying takes much longer, especially in the shared drive, is confusing and takes up unnecessary space.

---
### RAW ASSETS
---

#### *cut_categories.py*
Removes unwanted additional information from the end of filenames, leaving only the 6-digit ID number.

#### *enum_listdir.py*
Prints an enumerated list of various different folders

#### *extract_zip.py*
Unzips downloaded assets - currently restricted from adding rar functionality as can't add to %PATH% due to admin restrictions.

#### *move_files.py*
Moves processed assets and files them in relevant folders including, entry forms, surveys, any video types and zip files.

#### *categorise_files.py*
Sorts processed entry forms into corresponding category folders.

---
### IMPROVEMENTS
---

- create a script to setup correct folders for new award cycles
- move shortlisted abstracts to respective directories
- add instructions to readme for remaining scripts
- add logging to remaining scripts (ensure no overlaps)
- add functionality to move / copy and sort relevant abstracts ('.txt' files)
- add adjustment for MENA and Asia prize, which have no categories so don't need an 'all_shortlists.xlsx' file.
- incorporate other file handling into the same project and create a GUI for running the relevant scripts
- make sure the GUI has a checklist for each stage that needs doing to ensure scripts work well
