from re import X


x=open("file reading.txt")
z=x.read()

print(z)
for line in z:     #to print word by word
    print(line)
x.close()


