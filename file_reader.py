filename = input("Enter the filename to read: ")

try:
    with open(filename, 'r') as file:
        content = file.read()
        print("\nFile Content:")
        print(content)
except FileNotFoundError:
    print("File not found.")
