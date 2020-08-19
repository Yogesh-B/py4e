import re
f_name=input("Enter file name:")
fh=open(f_name)
sum=0       #sum of all
for l in fh:
    x=re.findall('[0-9]+',l)
    for i in x:
        sum+=float(i)
print("Sum==",sum)    