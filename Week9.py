import os
import pandas as pd









try:
    with open("Week9.txt","r") as file:
            content=file.read()
            print(content)
except:
    print("The file was not found.")
