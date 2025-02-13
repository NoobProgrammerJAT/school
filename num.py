file = open("num.txt", 'r')
#To Output A File
print(file.read())

#Alternative method to Output File
text = file.read()
print(text)
for line in file:
    print(line)

#outputing the number of characters, including spaces or backlash
print(file.read(4))

#To read a line

print(file.readline())
print(file.readline())

#To print as an array
text1 = file.readlines()
print(text1)
print(text1[1])
for i in range (len(text1)):
    print(text1[i])


text2 = file.readlines()
total = 0 
for i in range(len(text2)):
    total = total + int(text[i].rstrip())

print ("Total is ", total)




name = "    john     "
print(name.strip())
print(name.rstrip())
print(name.lstrip())



numArr = []
for line in file:
    numArr.append(int(line.rstrip()))

print(numArr)

file.close()
