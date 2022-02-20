"""
Proyect 0:
    - Create a parser:
        The program should read a text file that 
        constains commands and definitions for the
        robot and verify whether the syntax is correct.
"""






# Read the text file
def readfile(file):
    with open(file) as robot:
        lines = robot.readlines()
        for data in lines:
            print(data)


print(readfile("Robot.txt"))