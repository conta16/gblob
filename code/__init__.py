import sys
#import os
from cmap import cmap
from exceptions import InvalidArgumentsError
from manageDir import manageDir

class Menu:
    def __init__(self):
        self.manageDir = manageDir()
        self.cmap = cmap(self.manageDir)
        self.check_args()
        
    def check_args(self):
        try:
            if (len(sys.argv) > 2):
                if sys.argv[1] == "clean":
                    self.manageDir.clean(sys.argv[2:])
                elif len(sys.argv) == 4:
                    if sys.argv[1].endswith(".xml") and sys.argv[2].isnumeric() and sys.argv[3].isnumeric():
                        self.cmap.createMap(sys.argv[1],sys.argv[2],sys.argv[3])
                    else:
                        raise InvalidArgumentsError
                else:
                    raise InvalidArgumentsError
            elif (len(sys.argv) == 2) and sys.argv[1] == "-h":
                print("Usage: [.xml] [RA] [DEC] - create a .fits skymap with source defined in [.xml] pointing at [RA] and [DEC]")
                print("       [clean] [files] - remove skymaps from skymaps folder")
            else:
                raise InvalidArgumentsError
        except InvalidArgumentsError:
            print("InvalidArgumentsError: wrong number/format of arguments. Check -h")
                    
if __name__ == "__main__":
    start = Menu()
