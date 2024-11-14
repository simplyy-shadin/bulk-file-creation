import os

def create_files_in_bulk(directory, file_prefix, num_files, file_extension, content=""):
    """
    Creates multiple files in bulk in a specified directory.

    :param directory: Directory where the files will be created
    :param file_prefix: Prefix for the file names (e.g., 'file' will create file1.txt, file2.txt, etc.)
    :param num_files: Number of files to create
    :param file_extension: Extension of the files (e.g., '.txt', '.csv')
    :param content: (Optional) Content to write in each file, default is empty string
    """
    # Ensure the directory exists, if not, create it
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"Directory '{directory}' created.")
    
    for i in range(1, num_files + 1):
        # Generate file name
        file_name = (f"{file_prefix}{i}{file_extension}")
        file_path = os.path.join(directory, file_name)
        
        # Open the file and write content
        with open(file_path, 'w') as file:
            file.write(content)
        
        print(f"Created: {file_path}")


if __name__ == "__main__":
    # Parameters for bulk file creation
    directory = input("Enter the directory path where files should be created: ")
    file_prefix = input("Enter the file prefix (e.g., 'file'): ")
    num_files = int(input("Enter the number of files to create: "))
    file_extension = input("Enter the file extension (e.g., '.txt'): ")
    content = input("Enter the content to write in each file (Leave empty for no content): ")

    # Create files in bulk
    create_files_in_bulk(directory, file_prefix, num_files, file_extension, content)
