from __future__ import print_function
from autofind import process_file
import sys
import os

filenames = sys.argv[1:]
print("Will process:", filenames, file=sys.stderr)

for filename in filenames:
  print("Working on", filename, file=sys.stderr)

  assert filename.lower().endswith('.eeg')
  print("Converting .EEG to .edf...", file=sys.stderr)
  if os.system('nk2edf -no-annotations "' + filename + '"') != 0:
    print("WARNING: failed to nk2edf...ignoring .EEG file!", file=sys.stderr)
    continue

  fid = filename[:-4]  # strip .eeg
  edfname = fid + '_1-1.edf'

  if os.path.isfile(edfname) == False:
    print("WARNING: can't find .edf file according to convention, skipping...", file=sys.stderr)
    continue

  try:
    print('Processing', edfname, '...', file=sys.stderr)
    process_file(edfname)
  except KeyboardInterrupt:
    raise
  except Exception as e:
    print('Exception:', e, file=sys.stderr)
  finally:
    print('Deleting temporary .edf file:', edfname, file=sys.stderr)
    os.remove(edfname)
