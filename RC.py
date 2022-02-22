loop = ['(', 'loop', '(', 'not', '(', 'can-put-p', ':balloons', '1', ')', ')', '(', '(', 'put', ':balloons', '1', ')', '(', 'put', ':balloons', '1', ')', ')', ')']
loop2 = ['(', 'loop', '(', 'not', '(', 'can-pick-p', ':balloons', '1', ')', ')', '(', '(', 'put', ':balloons', '1', ')', '(', 'put', ':balloons', '1', ')', ')', ')']
if_ = ['(', 'if', '(', 'not', '(', 'can-put-p', ':chips', '1', ')', ')', '(', 'put', ':balloons', '1', ')', '(', 'put', ':balloons', '1', ')', ')']
if_2=['(', 'if', '(', 'not', '(', 'can-pick-p', ':chips', '1', ')', ')', '(', 'put', ':balloons', '1', ')', '(', 'put', ':balloons', '1', ')', ')']


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