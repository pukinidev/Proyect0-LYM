put = ['(', 'if', '(', 'can-pick-p', ':chips', '1', ')', '(', 'put', ':balloons', '1', ')', '(', 'put', ':balloons', '1', ')', ')']


paramP = 7
carries = [":chips", ":balloons"]


def can_pick(tokens):
   global variables
   global carries
   print((tokens))
   if len(tokens) == 5:
      if tokens[0] == "(" and tokens[-1] == ")":
        if tokens[3].isnumeric() or tokens[3] in variables:
         if tokens[2] in carries:
            return True
   return False

print(can_pick(put[2:paramP]))