import os

def viewFile():
    cwd = os.getcwd()
    print(f"Files in {cwd}:")
    files = [f for f in os.listdir(cwd) if os.path.isfile(os.path.join(cwd, f))]
    if not files:
        print("No files found in the current directory.")
        return
    for f in files:
        print(f)

    filename = input("Enter a file name from these names: ")

    if filename not in files:
        print("Error: File not found in current directory.")
        return

    filepath = os.path.join(cwd, filename)
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            contents = file.read()
            print(contents)
    except Exception as e:
        print(f"Error opening file: