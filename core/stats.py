import os

class DirObj:
    def __init__(self, path):
        self.path = path
        self.files = []
        self.folders= []
        self.total_size = 0
        self.specials = []
    
    def size_converter (self,size):
        if size == 0:
            return("0 Bytes")
        i = 0
        size_formats = ["Bytes", "KB", "MB", "GB", "TB", "PB"]
        while size >= 1024 and i < len(size_formats) -1:
            size /= 1024
            i += 1
    
        return (f"{size:.2f} {size_formats[i]}")
    
    def run_stats (self,path:str, human = False, verbose = False):

        largest_file = None
        smallest_file = None
        largest_size=0
        smallest_size= 1000000000
        size = 0
    
        # Walks through a directory
        for (dirpath, dirnames, filenames) in os.walk (path):
            self.folders.extend(dirnames)
            self.files.extend(filenames)

            for file in filenames:
                file_path = os.path.join(dirpath,file)

                size = os.path.getsize(file_path)
                self.total_size += size
             
                if size > largest_size:
                    largest_file = file
                    largest_size = size
                if size <= smallest_size:
                    smallest_file = file
                    smallest_size = size
                # Calculates total size
            
        self.specials.extend ([largest_file, self.size_converter(largest_size) if human else largest_size, smallest_file, self.size_converter(smallest_size) if human else smallest_size])
        if human:
            self.total_size = self.size_converter(self.total_size)
            





    

 
    
    def print_stats(self):
        print(f"Total Files: {len(self.files)}\n"
              f"Total Folders: {len(self.folders)}\n"
              f"Total Size: {self.total_size}\n"
              f"Largest File: {self.specials[0]}- {self.specials[1]}\n"
              f"Smallest File: {self.specials [2]}- {self.specials[3]}\n"
              
              )



    
       
    
   
   

    
