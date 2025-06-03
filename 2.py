import os
print("xxx")
print(os.getcwd()) 
print("xxx")

base_path = os.path.dirname(__file__)
file_path = os.path.join(base_path, 'a.txt')

with open(file_path, "r", encoding='utf8') as file:
    for line in file:
        print(line)