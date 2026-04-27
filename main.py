import pandas as pd
from datetime import datetime

now = datetime.now()

data = {"Time": [now]}
df = pd.DataFrame(data)

print(df)


with open("Students_list.txt","w") as file:
    file.write("John Doe\n")
    file.write("Jane Smith\n")
    file.write("Alice Johnson\n")
    file.write("Bob Brown\n")
try:    
    with open("Students_list.txt","r") as file:
        students = file.read()
        print(students)
except FileNotFoundError:
    print("The file was not found.")
    
with open("Students_list.txt","a") as file:
    file.write("Charlie Davis\n")
    
with open("Students_list.txt","r") as file:
    students = file.readlines()
    for student in students:
        print(student)
        


    
