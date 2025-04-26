# Function for file read, modify, and write
def file_read_write():
    try:
        # Ask the user for a filename
        filename = input("Enter the name of the file to read: ")
        
        # Attempt to open and read the file
        with open(filename, 'r') as file:
            content = file.read()
        
        # Modify the content (example: convert to uppercase)
        modified_content = content.upper()
        
        # Write the modified content to a new file
        new_filename = "modified_" + filename
        with open(new_filename, 'w') as new_file:
            new_file.write(modified_content)
        
        print(f"Modified content written to {new_filename}")

    except FileNotFoundError:
        print("Error: The file does not exist.")
    except IOError:
        print("Error: Unable to read the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Execute the function
file_read_write()