import os
data = []
with open('csv_20260206_08a514.txt', 'r') as x:
    for line in x:
        data.append(line)
info = []
datawt = []
datawt = data

for x in range(len(datawt)):
    print(x+1)
    prover = []
    fs = datawt[x].split(',')
    for x in fs:
        if x.isdigit() or (x.startswith('-') and x[1:].isdigit()):
            prover.append('0')
            print('digit')
        elif '.' in x:
            prover.append('1')
            print('float')
        else:
            prover.append('2')
            print('string')
    info.append(prover)
for x in range(len(info)):
    print(info[x])
itog = [int(x) for x in info[0]]
if sum(itog) == 10:
    print('head')




















