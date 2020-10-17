#7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
#X-DSPAM-Confidence:    0.8475
#Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.
#You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.


f_name=input("Enter a file name:")
fh=open(f_name)
total=0
count=0
for l in fh:
    if(l.startswith("X-DSPAM-Confidence")):
        index=-1
        for i in l:
            if(i.isdigit()):
                index=l.find(i)
                break
        tmp_str=l[index:]
        total+=float(tmp_str)
        count+=1
print("Average spam confidence:",total/count)

        