
import os
def create_file():
    user_input=input("enter the filename and the message")
    try:
        file_name,text_message=user_input.split(maxsplit=1)
        with open (file_name,'w') as file:
            file.write(text_message)
            print(f"a new file is created {file_name}")
    except Exception as e:
     print(f"an exception occured {e}")

def read_file():

    file_name=input("enter the filename to read")
    
    with open(file_name,'r') as file:
        content=file.read()
        print(content)

def delete_file():
    file_name=input("enter the file name to delete")

    try:
        os.remove(file_name)
        print(f"{file_name} is removed")
    except FileNotFoundError:
        print(f"file {file_name} not found error")
    except Exception as e:
        print(f"an exception occured {e}")    

create_file()
read_file()
delete_file()