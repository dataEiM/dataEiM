import os
print("xxx")
print(os.getcwd()) 
print("xxx")
with open("a.txt", "r", encoding='utf8') as file:
    for line in file:
        print(line)