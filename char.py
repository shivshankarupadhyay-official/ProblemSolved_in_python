srt = "azyxyyzaaaq"

new = ["a","z","y","x"]

emp = [0]*26
for ch in srt:
    ascii_val = ord(ch)

    index = ascii_val-97

    emp[index]+=1

for ch in new:
    ascii_val = ord(ch)
    index = ascii_val - 97

    print(emp[index])