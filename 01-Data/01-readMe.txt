Note000. DYD data cannot be shared without ecobee's permission therefore:
- an example of metadata file format provided in folder 0000_00; and
- an example of data file format provided in folder 2017-09

Note001. For ease of processing using python code:
- folder 0000_00 created to house meta data

Note002.For unzipping the monthly data folders:
- requires monthly folders for output (format: YYYY-MM)
- use file UnzipData.py

Note003. For some zipped folders:
- the code returns an inner folder instead of 
  directly displaying the csv files directly 
  in the monthly folder. The csv files to be 
  transfered to outer folder manually.
- the code returns an error to be unzipped by hand.

Note004. For finding the Ids (and filenames) common among specific 
monthly data folders:
- requires monthly data folders (format: YYYY-MM)
- use file getCommonIds.py
- creates a file named CommonIds.csv

