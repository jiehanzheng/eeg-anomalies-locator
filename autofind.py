from __future__ import print_function
import sys
import eegtools
import numpy as np
from sklearn.svm import OneClassSVM

CONTAMINATION=0.01

def process_file(filename):
  print('='*80)
  print(filename)
  print('='*80)

  print("Loading EEG", filename, "...", file=sys.stderr)
  eeg = eegtools.io.load_edf(open(filename))

  def find_anomaly(label1, label2, winsize):
    print("Find anomaly in channel", label1 + '-' + label2 + '...', file=sys.stderr)
    print("-"*80)
    print("Channel [" + label1 + '-' + label2 + ']')
    print("-"*80)

    # find difference
    electrode1 = eeg.chan_lab.index(label1)
    electrode2 = eeg.chan_lab.index(label2)
    wave = eeg.X[electrode1] - eeg.X[electrode2]

    # # import random
    # wave = [random.uniform(-20,20) for _ in range(400*30)] + [random.uniform(-2000,2000) for _ in range(5*30)]
    # wave = np.array(wave)

    print("Splitting into windows...", file=sys.stderr)
    wave_windows = np.array_split(wave, len(wave)/eeg.sample_rate/winsize)
    # wave_windows = np.array_split(wave, len(wave)/winsize)

    print("Extracting features...", file=sys.stderr)
    def extract_features(wave_window): 
      max_val = max(wave_window)
      min_val = min(wave_window)
      stdev = np.std(wave_window)
      sum_val = sum(wave_window)
      sum_pos_val = sum([x for x in wave_window if x > 0])
      sum_abs_val = sum([abs(x) for x in wave_window])
      return [max_val, min_val, stdev, sum_val, sum_pos_val, sum_abs_val]

    Examples = np.array(map(extract_features, wave_windows))

    print("Training model, assuming no more than", CONTAMINATION, "anomaly...", file=sys.stderr)
    od = OneClassSVM(nu=CONTAMINATION, kernel='poly', gamma=0.05, max_iter=100000)
    od.fit(Examples)

    decisions = od.decision_function(Examples)
    # print decisions
    # print max(decisions), min(decisions)

    print("Most likely windows with anomaly:")
    # find most likely windows, in desc order
    largest_indices = np.argsort((-np.absolute(decisions)).ravel())[:20]
    for large_index in largest_indices:
      print(large_index*winsize/60, "min (score:", decisions[large_index][0], ")")

    sys.stdout.flush()

  find_anomaly("Fp1", "F3", 15)
  find_anomaly("F7", "T3", 15)
  find_anomaly("Fp2", "F4", 15)

if __name__ == '__main__':
  process_file(sys.argv[1])
