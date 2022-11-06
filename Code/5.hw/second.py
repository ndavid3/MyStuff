wrd = input()
rep = {".": "",
       ",": "",
       "?": "",
       "!": "",
       "-": "",
       ";": "",
       ":": "",
       "–": "",
       " ": ""
       }
for key, value in rep.items():
    wrd = wrd.replace(key, value)

wrd = wrd.lower()

bl = 0
n = len(wrd)
for i in range(0, n):
    if wrd[i] == wrd[n-i-1]:
        continue
    elif wrd[i] == "c" and wrd[n-i-1] == "s" and i < n-1 and wrd[i+1] == "s" and wrd[n-i-2] == "c":
        continue
    elif wrd[i] == "d" and wrd[n-i-1] == "z" and i < n-1 and wrd[i+1] == "z" and wrd[n-i-2] == "d":
        continue
    elif wrd[i] == "g" and wrd[n-i-1] == "y" and i < n-1 and wrd[i+1] == "y" and wrd[n-i-2] == "g":
        continue
    elif wrd[i] == "l" and wrd[n-i-1] == "y" and i < n-1 and wrd[i+1] == "y" and wrd[n-i-2] == "l":
        continue
    elif wrd[i] == "n" and wrd[n-i-1] == "y" and i < n-1 and wrd[i+1] == "y" and wrd[n-i-2] == "n":
        continue
    elif wrd[i] == "s" and wrd[n-i-1] == "z" and i < n-1 and wrd[i+1] == "z" and wrd[n-i-2] == "s":
        continue
    elif wrd[i] == "t" and wrd[n-i-1] == "y" and i < n-1 and wrd[i+1] == "y" and wrd[n-i-2] == "l":
        continue
    elif wrd[i] == "z" and wrd[n-i-1] == "s" and i < n-1 and wrd[i+1] == "s" and wrd[n-i-2] == "z":
        continue
    else:
        bl = 1

if bl == 1:
    print("Nem palindrom")
else:
    print("Palindrom")