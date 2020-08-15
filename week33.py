#3.3
score = input("Enter Score: ")
try:
    s=float(score)
except:
    print("Conversion Error")
    quit()
    
if( s>1.0 or s<0.0 ):
    print("input Out of Range")
    quit()

if(s>=0.9):
    print("A")
elif(s>=0.8):
    print("B")
elif(s>=0.7):
    print("C")
elif(s>=0.6):
    print("D")  
else:
    print("F")  