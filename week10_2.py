#10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
f_name=input("Enter file name:")
fh=open(f_name)
hrs=dict()
for l in fh:
    if(l.startswith("From ")):
        tmp_str=l.split()
        #6.1
        tmp_hrs=tmp_str[5].split(":")
        hrs[tmp_hrs[0]]=hrs.get(tmp_hrs[0],0)+1
        
out=list(sorted(hrs))
for i in out:
    print(i,hrs[i])