#!/usr/bin/env python3

# a boilerplate is a simple script that demonstrates something about a program

"""Description of this program or application.
    You can use several lines"""

__appname__ = '[application name here]'
__author__ = 'Eleanor Jackson (eleanor.elizabeth.j@gmail.com)'
__version__ = '0.0.1'
__license__ = "License for this code/program"

## imports ##
import sys # module to interface our program with the operating system

## constants ##


## functions ##
def main(argv):
    """ Main entry point of the program """
    print('This is a boilerplate') # NOTE: indented using two tabs or 4 spaces
    return 0 # 0 is a success - the code has worked

if __name__ == "__main__": 
    """Makes sure the "main" function is called from command line"""  
    status = main(sys.argv)
    sys.exit(status)