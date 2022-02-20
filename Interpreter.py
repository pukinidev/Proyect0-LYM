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

#command
def defvar (words):
   return True

def move (words):
   return True

def equals (words):
   return True

def turn (words):    
   return True

def face (words):
   return True

def put (words):
   return True

def pick (words):
   return True

def move_dir (words):
   return True

def run_dir (words):
   return True

def move_face (words):
   return True

def skip (words):
   return True

command = {"defvar": defvar,
         "move": move, 
        "=": equals, 
         "turn": turn, 
         "face": face, 
         "put": put, 
         "pick": pick, 
         "move-dir": move_dir,
         "run-dirs": run_dir, 
         "move-face":move_face, 
         "skip": skip}

#control Structures
def if_ (words):
   return True

def loop (words):
   return True

def repeat (words):
   return True

def defun (words):
   return True
	
controlStructure = {"if": if_,
                    "loop": loop, 
                    "repeat": repeat, 
                    "defun": defun}

orientations = [":north", ":south", ":east", ":west"]


def validInput (code):
	for linea in code:
		encontro = False

		for keyword in command:
			if linea.find(keyword) != -1:
					funcion = command[keyword]
					encontro = True
					break
		
		if encontro:
			if funcion(linea):
				continue
			else:
				return "NO"

		for keyword in controlStructure:
			if linea.find(keyword) != -1:
					funcion = controlStructure[keyword]
					encontro = True
					break
		
		if encontro:
			if funcion(linea):
				continue
			else:
				return "NO"

	return "YES"



code = readfile("Robot.txt")
print(validInput(code))







    