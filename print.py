import sys
import sys
import fileinput
import re
import time

fileToEdit = sys.argv[1]

def part_one():
    for line in fileinput.input(fileToEdit):
        ### part 1 code goes here ###
        ### change the following line so that instead of printing the word "something", it prints the contents of the file
        ### hint: we're inside a loop iterating over each line in the file
        print "something"

def part_two():
    for line in fileinput.input(fileToEdit):
        ### part 2 code starts here ###

        # it looks along the lines of this:
        # line = line.replace("<replacee>", "<replacer>")
        #line = "something"
        #line = line.replace("||", "|0|")

        ### part 2 code stops here###

        ### part 3 code starts here ###
        # this will look VERY similar to your solution to part 2


        ### part 3 code ends here ###

        ### part 4 code starts here ###
        # this will look VERY similar to your solutions to part 2 and 3
        #

        ### part 4 code ends here ###
        print line

def main():
    #part_one()
    part_two()
    
if __name__ == "__main__":
    main()
