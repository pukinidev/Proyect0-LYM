"""
Proyect 0:
    - Create a parser:
        The program should read a text file that 
        constains commands and definitions for the
        robot and verify whether the syntax is correct.

Valeria Caro - v.caro@uniandes.edu.co - 202111040
Sofia Velasquez - s.velasquezm2@uniandes.edu.co - 202113334
"""

#Read file and debug it (ignore spaces and tabs)
def readfile (file):
    code = []
    with open(file) as robot:
        lines = robot.readlines()
        for data in lines:
            if not data.strip():
                continue
            code.append(data.rstrip().lstrip())

    return code
            
code = readfile("Robot.txt")
print(code)

# Define Grammmar

command = ["defvar", "move", "=", "turn", "face", "put", "pick", "move-dir","run-dirs", "move-face", "skip"]

controlStructure = ["if", "loop", "repeat", "defun"]

orientations = [":north", ":south", ":east", ":west"]



    