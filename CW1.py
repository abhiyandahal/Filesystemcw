import os
import sys

def get_file_name():
  """Gets the file name from the user."""
  print("Enter the file name: ")
  file_name = input()

  return file_name

def get_content():
  """Gets the content from the user."""
  print("Enter the content you want to write to the file: ")
  content = input()

  return content

def write_to_file(file_name, content):
  """Writes the given content to the file with the given file name."""
  try:
    with open(file_name, "w") as f:
      f.write(content)
  except FileNotFoundError:
    print("File does not exist.")

def delete_file(filename):
  """Deletes the file with the given filename."""
  if not os.path.exists(filename):
    print("File does not exist.")
    return

  os.remove(filename)

def read_from_file(file_name):
  """Reads the text from the file with the given filename."""
  with open(file_name, "r") as f:
    text = f.read()

  return text

def update_file(file_name, content):
  """Updates the file with the given filename with the given content."""
  if not os.path.exists(file_name):
    print("File does not exist.")
    return

  with open(file_name, "w") as f:
    f.write(content)

def change_file_permissions(file_name, mode):
  """Changes the permissions of the file with the given filename to the given mode."""
  if not os.path.exists(file_name):
    print("File does not exist.")
    return

  os.chmod(file_name, mode)

def create_directory(directory_name):
  """Creates a new directory with the given directory name."""
  if os.path.exists(directory_name):
    print("Directory already exists.")
    return

  os.mkdir(directory_name)

def delete_directory(directory_name):
  """Deletes the directory with the given directory name."""
  if not os.path.exists(directory_name):
    print("Directory does not exist.")
    return

  os.rmdir(directory_name)

def get_directory_name():
  """Gets the directory name from the user."""
  print("Enter the directory name: ")
  directory_name = input()

  return directory_name

def main():
    while True:
        print("What do you want to do?")
        print("1. Create a file")
        print("2. Write to a file")
        print("3. Delete a file")
        print("4. Read from a file")
        print("5. Update a file")
        print("6. Change the permissions of a file")
        print("7. Create a directory")
        print("8. Delete a directory")
        print("9. Exit")

        choice = input("Enter your choice: ")

        # Validate choice as an integer from 1 to 9
        if not choice.isdigit() or not (1 <= int(choice) <= 9):
            print("Invalid choice. Please enter a valid option.\n")
            continue

        if choice == "1":
            file_name = get_file_name()
            content = get_content()
            write_to_file(file_name, content)
        elif choice == "2":
            file_name = get_file_name()
            content = get_content()
            write_to_file(file_name, content)
        elif choice == "3":
            file_name = get_file_name()
            delete_file(file_name)
        elif choice == "4":
            file_name = get_file_name()
            text = read_from_file(file_name)
            print(text)
        elif choice == "5":
            file_name = get_file_name()
            content = get_content()
            update_file(file_name, content)
        elif choice == "6":
            file_name = get_file_name()
            mode = input("Enter the new mode: ")
            try:
                mode = int(mode)
            except ValueError:
                print("Invalid mode.")
                continue
            change_file_permissions(file_name, mode)
        elif choice == "7":
            directory_name = get_directory_name()
            create_directory(directory_name)
        elif choice == "8":
            directory_name = get_directory_name()
            delete_directory(directory_name)
        elif choice == "9":
            print("Goodbye!")
            sys.exit()  # Exit the program

        print("Do you want to continue? (y/n)")
        continue_program = input()

        if continue_program.lower() != "y":
            print("Goodbye!")
            break  # Exit the loop

if __name__ == "__main__":
    main()