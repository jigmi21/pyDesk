import argparse
from core.stats import DirObj
from core.organize import FileOrganizer

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('path', type = str, help= "The path to the directory")
    arg = parser.parse_args()
    directory_object = DirObj(arg.path)
    directory_object.run_stats(arg.path, human = True)
    directory_object.print_stats()
    org_obj = FileOrganizer(arg.path)
    org_obj.action()
    org_obj.move()







if __name__ == '__main__':
    main()