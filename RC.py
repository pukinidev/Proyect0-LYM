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
