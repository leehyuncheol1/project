import os

path = "./"
file_list = os.listdir(path)
file_list_py = [file for file in file_list if file.endswith(".py")]
print("file_list_py: {}".format(file_list_py))

file_list_py = []
for f in file_list:
    if f.endswith('.py'):
        file_list_py.append(f)
print(f"file_list_py: {file_list_py}") 
       