# |  p  |  i  |  s  |  a  |  n  |  g  |     |  g  |  o  |  r |  e  |   n  |   g  |

# |  0  |  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |  9 | 10  |  11  |  12  | #positive indices

# | -13 | -12 | -11 | -10 |  -9 | -8  |  -7 |  -6 |  -5 | -4 | -3  |  -2  |  -1  | #negative indices

text = "pisang goreng"

a = text[2:]

print('e'+a+' bau')

# accessing string values via negative index.
if text[-1] == text[12]:
    print("True")
else:
    print("False")
  
"""
string is immutable i.e once created you can not change any of its character.
i.e text[2] == 'A' will give error
"""
