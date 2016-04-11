# eeg-anomalies-locator
Finds anomalies in EEG data (in EDF format).

## Methodology
1. Splits input into 15-second windows
2. Extracts summary statistics like min, max, stdev, sum, etc.
3. Trains a SVM classifier
4. Outputs minute markers of the top 20 15-second segments that are furthest away from the SVM hyperplane

## Example output
```
> python autofind.py data/MA7037UC_1-1.edf 
Loading EEG...
Find anomaly in channel Fp1-F3...
Splitting into windows...
Extracting features...
Training models, assuming no more than 0.01 anomaly...
Most likely windows with anomaly:
172 min (score: 1.8347193764e+33 )
108 min (score: 3.84061772269e+32 )
173 min (score: 2.0958434103e+32 )
220 min (score: 1.75010124982e+32 )
108 min (score: 1.06212651453e+32 )
220 min (score: 1.05505858813e+32 )
216 min (score: 7.77351793251e+31 )
220 min (score: 7.68296110661e+31 )
109 min (score: 3.75689131902e+31 )
172 min (score: 3.02347323301e+31 )
172 min (score: 2.16866920334e+31 )
229 min (score: 1.85963984929e+31 )
229 min (score: 1.38057726793e+31 )
214 min (score: 1.20328730761e+31 )
220 min (score: 1.18017061548e+31 )
29 min (score: 9.45216996522e+30 )
221 min (score: 7.9802878321e+30 )
184 min (score: 6.65323566017e+30 )
167 min (score: 6.45611394441e+30 )
216 min (score: 4.97350544054e+30 )
Find anomaly in channel F7-T3...
Splitting into windows...
Extracting features...
Training models, assuming no more than 0.01 anomaly...
Most likely windows with anomaly:
161 min (score: 1.90288655036e+33 )
229 min (score: 1.09471452084e+33 )
108 min (score: 9.70249198924e+32 )
229 min (score: 7.81256472148e+32 )
162 min (score: 5.71996245893e+32 )
76 min (score: 5.13042166729e+32 )
229 min (score: 4.35093642597e+32 )
80 min (score: 4.05543665291e+32 )
109 min (score: 3.90441346133e+32 )
162 min (score: 3.83448893852e+32 )
52 min (score: 3.2827409731e+32 )
183 min (score: 2.86395401981e+32 )
217 min (score: 2.78217361773e+32 )
80 min (score: 2.15665432324e+32 )
161 min (score: 1.96824491807e+32 )
183 min (score: 1.82362415876e+32 )
108 min (score: 1.67819175571e+32 )
80 min (score: 1.40346833287e+32 )
63 min (score: 1.33646547823e+32 )
48 min (score: 1.30639096949e+32 )
Find anomaly in channel Fp2-F4...
Splitting into windows...
Extracting features...
Training models, assuming no more than 0.01 anomaly...
Most likely windows with anomaly:
0 min (score: 2.25512347252e+33 )
1 min (score: 2.12446669458e+33 )
56 min (score: 1.89882676937e+33 )
56 min (score: 9.48730233415e+32 )
0 min (score: 8.03692622275e+32 )
1 min (score: 4.38054890914e+32 )
129 min (score: 3.82347252187e+32 )
56 min (score: 2.5069287253e+32 )
42 min (score: 9.30640722372e+31 )
178 min (score: 9.17285776259e+31 )
1 min (score: 7.50609766137e+31 )
42 min (score: 6.98706740802e+31 )
108 min (score: 5.57938453052e+31 )
177 min (score: 4.06430005986e+31 )
129 min (score: 3.52065041589e+31 )
45 min (score: 3.50532043973e+31 )
108 min (score: 3.25727215471e+31 )
57 min (score: 2.85466753108e+31 )
109 min (score: 2.50344910095e+31 )
177 min (score: 2.29230068874e+31 )
```
