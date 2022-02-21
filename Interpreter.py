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
from dis import Instruction


def readfile (file):
   code = ""
   with open(file) as robot:
      lines = robot.readlines()
      for data in lines:
         if not data.strip():
            continue
         code += (data.rstrip().lstrip())

   numParentesis = 0
   word = ""
   fileCode = []
   for letter in code:
      if letter == '(':
         numParentesis += 1
         
      elif letter == ')':
         numParentesis -= 1
      if numParentesis == 0:
         word += ')'
         fileCode.append(word)
         word = ""
         continue

      word += letter
   
   return fileCode

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
   for instruction in code:
      print(instruction)
      word = ""
      for letter in instruction:
         if letter != ' ':
            if letter != '(':
               word += letter
         else: 
            print(word)
            if word in controlStructure:
               funcion = controlStructure[word]

            elif word in command:
               funcion = command[word]
            else:
               return "Invalid Sintaxis"
            
            if not funcion(instruction):
               return "Invalid Sintaxis"
            break
            

   return "Valid Sintaxis"
         

            

code = readfile("Robot.txt")

print(validInput(code))







    