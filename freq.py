lsi = [11,22,33,11,33,111,133,133,2211,1,133]
freq = {}

for i in range(0,len(lsi)):
    if lsi[i] in freq:
        freq[lsi[i]] += 1
    else:
        freq[lsi[i]] = 1

print(freq)