import pandas as pd


sequence = pd.read_csv('seq2.txt',sep='\s+')
s = []
for i in range(133):
    if sequence.ix[i].max()>1000000:
        s.append(sequence.ix[i].idxmax())
    else:
        s.append('N')

print(''.join(s))
