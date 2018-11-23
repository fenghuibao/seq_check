import sys
from numpy.random import randint
from argparse import ArgumentParser
import pandas as pd

parser = ArgumentParser()
parser.add_argument('--infile', help = 'Input raw fastq file.', required=True)
parser.add_argument('--outfile', help = 'Outfile name', required=True)
o = parser.parse_args()

readsProcessed = 0

A = [0]*150
T = [0]*150
C = [0]*150
G = [0]*150

current_line = 0
with open(o.infile,'r') as file:
    for line in file:
        current_line += 1
        if (current_line+2)%4 == 0:
            readsProcessed += 1
            seq = line.strip('\n')
            for j in range(150):
                if seq[j] == 'A':
                    A[j] += 1
                elif seq[j] == 'T':
                    T[j] += 1
                elif seq[j] == 'C':
                    C[j] += 1
                elif seq[j] == 'G':
                    G[j] += 1
        if readsProcessed % 100000 ==0:
            print("Reads Processed: %s" % readsProcessed)
print("Reads Processed: %s" % readsProcessed)
sequence = pd.DataFrame({'A':A,'T':T,'C':C,'G':G})
sequence.to_csv(o.outfile,sep = ' ')


