try:
    with open("input.txt","r") as file:
        data = file.read()
except FileNotFoundError:
    print("File not found. Please check the filename")
finally :
    file.close()
""" 
Creates a new file named output that contains modified content from input.txt
"""
try:
    with open("output.txt","w") as edit_file:
        edit_file.write(str.upper(data))
        print("The file has been created")
except FileNotFoundError:
    print("Could not create File")
finally:
    edit_file.close()