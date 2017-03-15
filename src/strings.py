
def trim(string, characters=" \t\n\r"):
  charspace = {}
  for i in characters:
    charspace[i] = i
  i = 0
  j = len(string) - 1
  while i < j:
    found = False
    if string[i] in charspace:
      i += 1
      found = True
    if string[j] in charspace:
      j -= 1
      found = True
    if not found:
      break
  newstring = ''
  for k in range(i,j+1):
    newstring += string[k]
  return newstring

def parse_int(string):
  num = 0
  dim = 1 # dimension, 1 or -1
  for i in range(len(string)):
    if i == 0 and string[0] == '-':
      dim = -1
      continue
    code = ord(string[i])
    if code < ord('0') or code > ord('9'):
      raise ValueError("Not Parseable")
    digit = code - 48
    place_value = 10 ** (len(string) - 1 - i)
    num += digit * place_value * dim
  return num
