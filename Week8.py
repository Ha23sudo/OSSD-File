
try:
    with open("test.txt","r") as file:
        content=file.read()
        print(content)
except :
    print("The file was not found.")
       





file=open("StudentsList2.txt","w")
file.write("Ali \n")
file.write("Ahmad \n")
file.close()


file=open("StudentsList.txt","r")
content=file.read()
print(content)


file=open("StudentsList2.txt","a")
file.write("Sara \n")
file.close()
