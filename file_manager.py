
import os

def create_file(file_name,text_message):
    try:

        with open(file_name,'w') as file:
             file.write(text_message)
             print(f"a new file is created {file_name} succesfully")
    except Exception as e:
        print("error creating file {e}")

def list_files():
    try:
        files=os.listdir()
        if files:
            print("files in the directory are: ")
            for file in files:
                if os.path.isdir(file):
                    print(f"{file}/")
                elif os.path.isfile(file):
                    print(file)
                else:
                    print(file)
        else:
            print("there are no files in the directory")
    except Exception as e:
        print("an exception occured {e}")

def change_directory(directory):
    try:
        os.chdir(directory)
        print (f"directory changed to {os.getcwd()}")
    except FileNotFoundError:
        print("file not found exception occured")
    except Exception as e:
        print("and exception occured {e}")

def file_operation(user_input):
    
    parts=user_input.split(maxsplit=2)

    command_name=parts[0].lower()

    if command_name=="touch" and len(parts)==3:
        file_name,text_message=parts[1],parts[2]
        create_file(file_name,text_message)
    elif command_name=="ls" and len(parts)==1:
         list_files()
    elif command_name=="cd" and len(parts)==2:
        directory=parts[1]
        change_directory(directory)
    else:
        print("entered command is invalid")

while True:
      user_input=input("enter the input")
      if(user_input.lower()=="exit"):
          print("exiting the file manager")
          break
      file_operation(user_input)