"""
Proyect 0:
    - Create a parser:
        The program should read a text file that 
        constains commands and definitions for the
        robot and verify whether the syntax is correct.

Valeria Caro - v.caro@uniandes.edu.co - 202111040
Sofia Velasquez - s.velasquezm2@uniandes.edu.co - 202113334
"""


orientations = [":north", ":south", ":east", ":west"]

direction = [":left", ":right"]

dire = [":front", ":back"]



variables =[]
functions = {}

#Read file and debug it (ignore spaces and tabs)

def readfile (file):
   code = ""
   with open(file) as robot:
      lines = robot.readlines()
      for data in lines:
         if not data.strip():
            continue
         code += (data.rstrip().lstrip())

   return debug(code)

def debug (code): #with parentesis
   word = ""
   debug = []
   numParentesis = 0
   for letter in code:
      if letter == '(':
         numParentesis += 1
      elif letter == ')':
         numParentesis -= 1

      word += letter
      if numParentesis == 0:
         word = word.replace(" )",")").replace("( ","(")
         debug.append(word)
         word = ""
         continue
      if word[-1]== ')':
            word+= " "
   if numParentesis != 0:
      return False
   return debug 

#commands
def defvar (words):
   global variables
   words = words.replace("(", "").replace(")","")
   tokens = words.split()
   if len(tokens) == 3:
      if tokens[2].isnumeric():
         variables.append(tokens[1])
         return True
   return False

def move (words):
   global variables
   words = words.replace("(", "").replace(")","")
   tokens = words.split()
   if len(tokens) == 2:
      if tokens[1].isnumeric() or tokens[1] in variables:
         return True
   return False

def equals (words):
   global variables
   words = words.replace("(", "").replace(")","")
   tokens = words.split()
   if len(tokens) == 3:
      if tokens[2].isnumeric() and tokens[1] in variables:
         return True
   return False

def turn (words):    
   global direction
   words = words.replace("(", "").replace(")","")
   tokens = words.split()
   if len(tokens) == 2:
      if tokens[1] in direction or tokens[1] == ":around":
         return True
   return False

def face (words):
   global orientations
   words = words.replace("(", "").replace(")","")
   tokens = words.split()
   if len(tokens) == 2:
      if tokens[1] in orientations:
         return True
   return False

def put (words):
   global variables
   words = words.replace("(", "").replace(")","")
   tokens = words.split()
   if len(tokens) == 3:
      if tokens[2].isnumeric() or tokens[2] in variables:
         if tokens[1] == ":balloons" or tokens[1] == ":chips":
            return True
   return False

def pick (words):
   global variables
   words = words.replace("(", "").replace(")","")
   tokens = words.split()
   if len(tokens) == 3:
      if tokens[2].isnumeric() or tokens[2] in variables:
         if tokens[1] == ":balloons" or tokens[1] == ":chips":
            return True
   return False
   
def move_dir (words):
   global variables
   global direction
   global dire
   words = words.replace("(", "").replace(")","")
   tokens = words.split()
   if len(tokens) == 3:
      if tokens[1].isnumeric() or tokens[1] in variables:
         if tokens[2] in direction or tokens[2] in dire:
            return True
   return False

def run_dir (words):
   global direction
   global dire
   words = words.replace("(", "").replace(")","")
   tokens = words.split()
   if len(tokens) >= 2:
      for i in range(len(tokens)):
         if i != 0:
            if tokens[i] in direction + dire:
               continue
            else:
               return False
   return True

def move_face (words):
   global variables
   global orientations
   words = words.replace("(", "").replace(")","")
   tokens = words.split()
   if len(tokens) == 3:
      if tokens[1].isnumeric() or tokens[1] in variables:
         if tokens[2] in orientations:
            return True
   return False

def skip (words):
   words = words.replace("(", "").replace(")","")
   tokens = words.split()
   if len(tokens) == 1:
      return True
   return False

#control Structures
def if_ (words):
   tokens = words.split()
   if len(tokens) >= 5:
      for i in range(1, len(tokens)):
            pass
      
   
def loop (words):
   return True

def repeat (words):
   return True

def defun (words):
   global functions
   tokens = words.split()
   param = 0
   if len(tokens) >= 4:
      index = 2
      for i in range (2,len(tokens)):
         if tokens[i] == "(":
            index+=1
            continue
         if tokens[i][-1] == ")":
            index +=1
            if tokens[i] == ")" or tokens[i]=="()":
               break
            param+=1
            break
         index +=1
         param +=1
      
      functions[tokens[1]] = param

      return tokens[index:]
   return False

#conditions
def facing (words):
   global orientations
   words = words.replace("(", "").replace(")","")
   tokens = words.split()
   if len(tokens) == 2:
      if tokens[1] in orientations:
         return True
   return False
   
def can_put (words):
   global variables
   words = words.replace("(", "").replace(")","")
   tokens = words.split()
   if len(tokens) == 3:
      if tokens[2].isnumeric() or tokens[2] in variables:
         if tokens[1] == ":balloons" or tokens[1] == ":chips":
            return True
   return False

def can_pick (words):
   global variables
   words = words.replace("(", "").replace(")","")
   tokens = words.split()
   if len(tokens) == 3:
      if tokens[2].isnumeric() or tokens[2] in variables:
         if tokens[1] == ":balloons" or tokens[1] == ":chips":
            return True
   return False



def can (words):
   global orientations
   words = words.replace("(", "").replace(")","")
   tokens = words.split()
   if len(tokens) == 2:
      if tokens[1] in orientations:
         return True
   return False

def not_ (words):
   global conditions
   tokens = words.split()
   if len(tokens) == 2:
      if tokens[1] in conditions:
         funcion = conditions[tokens[1]]
         if funcion(" ".join(tokens[1:])):
            return True
   return False


controlStructures = {"if": if_,
                    "loop": loop, 
                    "repeat": repeat, 
                    "defun": defun}

commands = {"defvar": defvar,
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

conditions = {"facing-p": facing,
              "can-put-p": can_put,
              "can-pick-p": can_pick,
              "can-move-p": can,
              "not": not_,}

def validInput (code):
   for instruction in code:
      print(instruction)
      word = ""
      for letter in instruction:
         if letter != ' ':
            if letter != '(':
               word += letter
         else: 
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
