# zip() function

'''name = ["Manjeet", "Nikhil", "Sambhavi", "Astha"]
roll_no = [4,1,3,2]
marks = [40, 50, 60, 70]

mapped = list(zip(name, roll_no, marks))
print(mapped)'''


#FILE HANDLING

'''file1 = open("C:\\Users\\CHAVI JAIN\\OneDrive\\Desktop\\file.txt","r")
print(file1)

contents = file1.read()
print(contents)

#file pointer position
print(file1.tell())

file1.seek(0)

#Buffer
print(file1.read(8))

print(file1.read(8))

file1.seek(0)

if file1:
    for i in file1:
        #print(i)
        print(i,end="")

file1.close()'''

'''Write'''
'''file1 = open("C:\\Users\\CHAVI JAIN\\OneDrive\\Desktop\\file.txt","w")


for i in range(0,2) :
    
    name = input("\nEnter your name:")
    address = input("Enter your address:")
    email = input("Enter your email:")

    file1.write(name+"\n")
    file1.write(address+"\n")
    file1.write(email+"\n")

file1.close()'''

'''Append'''


'''file1 = open("C:\\Users\\CHAVI JAIN\\OneDrive\\Desktop\\file.txt","a")


for i in range(0,2) :
    
    name = input("\nEnter your name:")
    address = input("Enter your address:")
    email = input("Enter your email:")

    file1.write(name+"\n")
    file1.write(address+"\n")
    file1.write(email+"\n")

    
    

file1.close()

L =[1,2,3]
file1.write(str(L))
file1.write(str(10))
file1.close()'''


'''X, Y, Z = 43, 44, 45
S = "Spam"
D = {'a':1, 'b':2}
L = [1,2,3]
T = (10,20,30)

F = open("C:\\Users\\CHAVI JAIN\\OneDrive\\Desktop\\file.txt","w")
F.write(S+"\n")
F.write('%s,%s,%s\n'%(X,Y,Z))
F.write(str(L) + '$' + str(D) +'\n'+ str(T))
F.close()'''

'''with open("C:\\Users\\CHAVI JAIN\\OneDrive\\Desktop\\file.txt","w")as f:
    f.write('first line\n')
    f.write('second line\n')
    f.write('third line\n')

with open("C:\\Users\\CHAVI JAIN\\OneDrive\\Desktop\\file.txt","r")as f:
    content = f.readlines()

for i in content:
    print(i)'''

'''L = ["Chavi", " Vaibhav", " Divyam", " Yash"]
with open("C:\\Users\\CHAVI JAIN\\OneDrive\\Desktop\\file.txt","w")as f:
    f.writelines(L)

with open("C:\\Users\\CHAVI JAIN\\OneDrive\\Desktop\\file.txt","w")as f:
    for i in L:
        f.write(i)'''
    
#import image
'''with open("C:\\Users\\CHAVI JAIN\\OneDrive\\Documents\\photo.jpg","rb") as f1:
    print(f1.read())'''

'''with open("C:\\Users\\CHAVI JAIN\\OneDrive\\Documents\\chavi sign.jpg","rb") as f1:
    with open("C:\\Users\\CHAVI JAIN\\OneDrive\\Documents\\Chavi Jain Photo.jpg","wb") as f2:
        f2.write(f1.read())'''


#Exception Handling

try:
    n = int(input("Enter the number to divide:"))
    res = 100/n
except ZeroDivisionError :
    print("Cant be divided by zero!")

except ValueError:
    print("Enter valid input")

else:
    print("Result is", res)

finally:
    print("Execution completed")
    

                 

