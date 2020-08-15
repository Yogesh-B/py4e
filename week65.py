#6.5 Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below. Convert the extracted value to a floating point number and print it out.

text = "X-DSPAM-Confidence:    0.8475"
index=-1
for c in text:
    if(c.isdigit()):
        index=text.find(c)
        break
tmp_str=text[index:]
num=float(tmp_str)
print(num)
        



