
# Q3. File Methods and Exception Handling

try:
    file = open("student.txt", "r")

    print("File Name:", file.name)
    print("File Mode:", file.mode)

    # Using read()
    print("\nUsing read():")
    print(file.read())

    # Using seek() to move file pointer
    file.seek(0)

    # Using readline()
    print("\nUsing readline():")
    print(file.readline())

    # Using seek() again
    file.seek(0)

    # Using readlines()
    print("\nUsing readlines():")
    print(file.readlines())

    # Demonstrating tell()
    file.seek(0)
    print("\nCurrent File Position:", file.tell())

    file.seek(5)
    print("File Position After seek():", file.tell())

except FileNotFoundError:
    print("Error: File not found.")

except PermissionError:
    print("Error: Permission denied.")

else:
    print("\nFile operations completed successfully.")

finally:
    try:
        file.close()
        print("File closed successfully.")
    except NameError:
        print("File was not opened.")
