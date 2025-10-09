# f = open('example.txt', 'r')

import json  # importing json to work with json file
import csv  # importing csv to work with csv file


# Reading Files (txt, json, csv)

# -----------------------------
# Reading text File
try:
    with open('example.txt', 'r') as file:
        content = file.read()  # storing the content of file and printing it
        # print(content)
except FileNotFoundError:
    print("❌ 404! File not found")
except PermissionError:
    print("☠️ Permission Denied")


# ------------------------------
# Reading JSON file
try:
    with open('example.json', 'r') as file:
        content = json.load(file)  # storing the content of file using json modules and it's method
        # print(content)
except FileNotFoundError:
    print("❌ 404! File not found")
except PermissionError:
    print("☠️ Permission Denied")
except json.decoder.JSONDecodeError as e:
    print("JSON Decoding issue", e)


# --------------------------------------------
# Reading CSV file

try:
    with open('data.csv', 'r') as file:
        content = csv.reader(file)  # storing the content of file using csv modules and it's method
        # accessing data line by line ⏬
        # for line in content:
        #     # print(line)
except FileNotFoundError:
    print("❌ 404! File not found")
except PermissionError:
    print("☠️ Permission Denied")
except json.decoder.JSONDecodeError as e:
    print("JSON Decoding issue", e)


# ***************************************************
# Writing files in python (txt, json, csv)

# Txt File
new_text = 'Trying to append more content into file'
file_path = "example.txt"

# with open(file=file_path, mode='a') as file:
#     file.write(new_text)
#     print(file)

#
# We cannot write/append list directly into a file as it's except the string
new_list = ['Trying', 'to', 'append', 'list']
with open(file_path, 'a') as file:
    for string in new_list:
        file.write('\n' + string)

# -------------
# JSON file


# writing new file
real_info = {
    "name": "Pratham",
    "age": 21,
    "job": "Frontend Developer"
}

# with open('info.json', 'w') as file:
#     json.dump(real_info, file, indent=4)
#     print('file created with json object')

#
new_info = {
    "experience": "2 years"
}
with open('info.json', 'r') as file:
    existing_data = json.load(file)

existing_data.update(new_info)

with open('info.json', 'w') as file:
    json.dump(existing_data, file, indent=4)
    print("Done")
