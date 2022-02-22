def readfile (file):
   code = ""
   with open(file) as robot:
      lines = robot.readlines()
      for data in lines:
         if not data.strip():
            continue
         code += (data.rstrip().lstrip())

   return debug(code)
   
def tokenizeString(aString, separators):
    separators.sort(key=len)
    listToReturn = []
    i = 0
    while i < len(aString):
        theSeparator = ""
        for current in separators:
            if current == aString[i:i+len(current)]:
                theSeparator = current
        if theSeparator != "":
            listToReturn += [theSeparator]
            i = i + len(theSeparator)
        else:
            if listToReturn == []:
                listToReturn = [""]
            if(listToReturn[-1] in separators):
                listToReturn += [""]
            listToReturn[-1] += aString[i]
            i += 1
    return listToReturn

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

def tokenizeInfo(info):
    lista = []
    for data in info:
      tokens = tokenizeString(aString = data, separators = ["(", ")", " "])
      a = list(filter(str.strip, tokens))
      lista.append(a)
    return lista

#COMMANDS
def defvar (tokens):
   global variables
   if len(tokens) == 5:
      if tokens[0] == "(" and tokens[-1] == ")":
            if tokens[1] == "defvar" and tokens[3].isnumeric():
               variables.append(tokens[2])
               return True
   return False

def equals (tokens):
   global variables
   if len(tokens) == 5:
      if tokens[0] == "(" and tokens[-1] == ")":
            if tokens[1] == "=" and tokens[3].isnumeric() and tokens[2] in variables:
               return True
   return False

def move (tokens):
   global variables
   if len(tokens) == 4:
      if tokens[0] == "(" and tokens[-1] == ")":
         if tokens[1] == "move" and (tokens[2] in variables or tokens[2].isnumeric()):
            return True
   return False

def turn (tokens):
   global xdire
   if len(tokens) == 4:
      if tokens[0] == "(" and tokens[-1] == ")":
         if tokens[1] == "turn" and (tokens[2] in xdire or tokens[2] == ":around"):
            return True
   return False

def face (tokens):
   global orientations
   if len(tokens) == 4:
      if tokens[0] == "(" and tokens[-1] == ")":
         if tokens[1] == "face" and tokens[2] in orientations:
            return True
   return False

def put (tokens):
   global carries
   global variables
   
   if len(tokens) == 5:
      if tokens[0] == "(" and tokens[-1] == ")":
         if tokens[2] in carries:
            if tokens[3].isnumeric() or tokens[3] in variables:
               return True
   return False

def pick (tokens):
   global carries
   global variables
   if len(tokens) == 5:
      if tokens[0] == "(" and tokens[-1] == ")":
         if tokens[2] in carries:
            if tokens[3].isnumeric() or tokens[3] in variables:
               return True
   return False
   
def move_dir (tokens):
   global variables
   global xdire
   global ydire
   if len(tokens) == 5:
      if tokens[0] == "(" and tokens[-1] == ")":
         if tokens[2].isnumeric() or tokens[2] in variables:
            if tokens[3] in xdire or tokens[3] in ydire:
               return True
   return False

def run_dir (tokens):
   global xdire
   global ydire
   global zdire
   if len(tokens) >= 4 and tokens[0] == "(" and tokens[-1] == ")":
      for i in range(len(tokens)):
         if i != 0 and i != len(tokens)-1 and i != 1:
            if tokens[i] in xdire + ydire + zdire:
               continue
            else:
               return False
   return True

def move_face (tokens):
   if len(tokens) == 5:
      if tokens[0] == "(" and tokens[-1] == ")":
         if tokens[3] in orientations and (tokens[2].isnumeric() or tokens[2] in variables):
            return True
   return False

def skip (tokens):
   if len(tokens) == 3 and tokens[0] == "(" and tokens[-1] == ")":
      return True
   return False

#CONTROL STRUCTURES
def if_(tokens): #TODO
   global conditions
   if len(tokens) >= 6 and tokens[0] == "(" and tokens[-1] == ")":
      if tokens[3] in conditions:
         funcion = conditions[tokens[3]]
         if tokens[3] == "not":
            param = 9
            if tokens[5] == "can-put-p" or tokens[3] == "can-pick-p":
               param = 10
         elif tokens[3] == "can-put-p" or tokens[3] == "can-pick-p":
            param = 7
         else:
            param = 6
         condicion = tokens[2:param]
         if not funcion(condicion):
            return False
         block = tokens[param:-1]
         com = []
         command=[]
         for symbol in block:
            com.append(symbol)
            if symbol == ')':
               command.append(com)
               com = []
         for i in command:
            funcion = commands[i[1]]
            if not funcion(i):
               return False
         return True
   return False   
         
def loop (tokens): #TODO
   global conditions
   if len(tokens) >= 5 and tokens[0] == "(" and tokens[-1] == ")":
      if tokens[3] in conditions:
         funcion = conditions[tokens[3]]
         if tokens[3] == "not":
            param = 9
            if tokens[5] == "can-put-p" or tokens[3] == "can-pick-p":
               param = 10
         elif tokens[3] == "can-put-p" or tokens[3] == "can-pick-p":
            param = 7
         else:
            param = 6
         condicion = tokens[2:param]
         if not funcion(condicion):
            return False

         block = tokens[param+1:-2]
         com = []
         command=[]
         for symbol in block:
            com.append(symbol)
            if symbol == ')':
               command.append(com)
               com = []
         
         for i in command:
            funcion = commands[i[1]]
            if not funcion(i):
               return False
      return True
   return False

def repeat(tokens):
   global commands
   global conditions
   if len(tokens) >= 5 and tokens[0] == "(" and tokens[-1] == ")":
      if tokens[2].isnumeric():
         block = tokens[4:-2]
         com = []
         command=[]
         for symbol in block:
            com.append(symbol)
            if symbol == ')':
               command.append(com)
               com = []
         
         for i in command:
            funcion = commands[i[1]]
            if not funcion(i):
               return False
         return True
   return False

def defun (tokens):
   if len(tokens) >= 7 and tokens[0] == "(" and tokens[-1] == ")":
      paramStop = 4
      numParam = 0
      while tokens[paramStop] != ')':
         numParam += 1
         paramStop += 1
      
      functions[tokens[2]] = numParam
      
      block = tokens[paramStop+2:-2]
      com = []
      command=[]
      for symbol in block:
         com.append(symbol)
         if symbol == ')':
            command.append(com)
            com = []
         
      for i in command:
         funcion = commands[i[1]]
         if not funcion(i):
            return False
      
      return True
   return False

# CONDITIONS

def facing(tokens):
   global orientations
   if len(tokens) == 4:
       if tokens[0] == "(" and tokens[-1] == ")":
           if tokens[2] in orientations:
            return True
   return False

def can_p(tokens):
   global variables
   global carries
   if len(tokens) == 5:
      if tokens[0] == "(" and tokens[-1] == ")":
        if tokens[3].isnumeric() or tokens[3] in variables:
         if tokens[2] in carries:
            return True
   return False

def can_move(tokens):
   global orientations
   if len(tokens) == 4:
       if tokens[0] == "(" and tokens[-1] == ")":
           if tokens[2] in orientations:
            return True
   return False

def not_(tokens):
   global conditions
   if len(tokens) == 6 or len(tokens)==7:
      if tokens[3] in conditions:
         funcion = conditions[tokens[3]]
         if funcion(tokens[2:-1]):
            return True
   return False

#RECURSION
def recursion_ (tokens):
   param = functions[tokens[1]]
   if (len(tokens)-3) == param:
      return True
   return False

#VERIFY SINTAXIS
def IsItValid (code):
   global controlStructures
   global commands
   global functions
   for instruction in code:
      if instruction[1] in controlStructures:
         funcion = controlStructures[instruction[1]]
      elif instruction[1] in commands:
         funcion = commands[instruction[1]]
      elif instruction[1] in functions:
         if not recursion_(instruction):
            return False
         else:
            continue   
      else:
         return False
         
      if not funcion(instruction):
         return False

   return True

###########################################
orientations = [":north", ":south", ":east", ":west"]
xdire = [":left", ":right"]
ydire = [":front", ":back"]
zdire = [":up", ":down"]

carries = [":chips", ":balloons"]

variables =[]
functions = {}

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
              "can-put-p": can_p,
              "can-pick-p": can_p,
              "can-move-p": can_move,
              "not": not_}

code = readfile("Robot.txt")
if code != False:
   tokens = tokenizeInfo(code)
   if IsItValid(tokens):
      print("Valid Sintaxis")
   else:
      print("Invalid Sintaxis")
else:
   print("Invalid Sintaxis")




    

