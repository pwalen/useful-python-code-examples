stringo = "32 6566 3433 8998 3005 2332 0000"
stringo2 = ""
for i in stringo:
    if i.isdigit(): 
        i = "X"
    stringo2 += i
print(stringo2)