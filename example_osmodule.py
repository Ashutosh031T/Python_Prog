import os

def list_directory_contents(directory):
    try:
        # Get the list of entries in the specified directory
        entries = os.listdir(directory)
        
        # Print each entry
        for entry in entries:
            print(entry)
    except FileNotFoundError:
        print(f"The directory '{directory}' does not exist.")
    except PermissionError:
        print(f"Permission denied to access '{directory}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Replace '.' with the path to the directory you want to list
# directory_path = '.'
# list_directory_contents(directory_path)
