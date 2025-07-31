import os

def viewFile():
    cwd = os.getcwd()
    print(f"Files in {cwd}:")
    files = [f for f in os.listdir(cwd) if os.path.isfile(os.path.join(cwd, f))]
    for f in files:
        print(f)

    filename = input("Enter a file name from these names: ")

    if filename not in files:
        print("Error: File not found in current directory.")
        return

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            contents = file.read()
            print(contents)
    except Exception as e:
        print(f"Error opening file: {e}")
def main():
    while True:
        print("""
1   List the current directory
2   Move up
3   Move down
4   Number of files in the directory
5   Size of the directory in bytes
6   Search for a file name
7   View the contents of a file
8   Quit the program
""")
        choice = input("Enter a number: ")

        if choice == '7':
            viewFile()
        elif choice == '8':
            print("Exiting program.")
            break
        # handle other choices...

if __name__ == "__main__":
    main()
