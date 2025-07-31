import os
import shutil   

# Category: Size, Extension, Date
class FileOrganizer:
    
    def __init__(self, path):
        self.path = path
        self.extensions = []
        self.created_directory = []
        self.existing_directories = []

    

    def action(self):
        # Create extensions
        for (dirpath, dirnames, filenames) in os.walk(self.path):          
            for file in filenames:
                _, file_extension = os.path.splitext(file)
                if file_extension:
                    stripped_extension = file_extension.lstrip(".").lower().strip()
                    if stripped_extension not in self.extensions:
                        self.extensions.append(stripped_extension)

        self.existing_directories = [name.lower().strip() for name in os.listdir(self.path) if os.path.isdir(os.path.join(self.path,name))]    
            


        # Create Directories
        for ext in self.extensions:
            target_dir = os.path.join(self.path, ext)
            if ext not in self.existing_directories:
                os.mkdir(target_dir)
                self.created_directory.append(ext)
        for dir in self.created_directory:
            print(f"Created New Directory '{dir}'")
    
    
    
    def move (self):

        for (dirpath, dirnames, filenames) in os.walk (self.path):
            for file in filenames:
                _, file_extension = os.path.splitext(file)
                if file_extension:
                    source_path = os.path.join(dirpath, file)
                    stripped_extension = file_extension.lstrip(".").lower().strip()


                    for dir in self.created_directory:
                        destination_path = os.path.join(self.path,dir)
                        destination =  os.path.join(destination_path, file)
                        print(f"StrippedExt: {stripped_extension}")
                        print(f"dir: {dir}")
                        if source_path != destination and stripped_extension == dir:
                            shutil.move(source_path, destination_path)
                            print("Moved Successfully")