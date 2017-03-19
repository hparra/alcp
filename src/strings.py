
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

def is_palindrome(string):
  """Check whether the given string is a palindrome"""
  if string is None:
    return True
  if len(string) < 2:
    return True
  i = 0
  n = len(string)
  while i < n-1:
    if string[i] != string[n-i-1]:
        return False
    i += 1
  return True

def is_palindromer(string, start=0, stop=None):
  if string is None:
    return True
  if len(string) < 2:
    return True
  if stop is None:
    stop = len(string)
  if start > stop - 1:
    return True
  if string[start] != string[stop-start-1]:
    return False
  else:
    return is_palindromer(string, start+1, stop)

def split(string, separator):
  """Return an array of new strings partitioned by separator string"""
  if separator == "":
    raise ValueError("empty separator")
  if string is None:
    return []
  if string == "" and separator is None:
    return []
  if separator is None:
    return [string]
  array = []
  prev = 0 # start of previous string
  i = 0
  n = len(separator)
  while i < len(string) - n + 1:
    substring = string[i:i+n]
    if substring == separator: # split here
      array.append(string[prev:i])
      i += n
      prev = i
    else:
      i += 1
  array.append(string[prev:]) # leftovers
  return array

def splitr(string, separator, start=0, stop=None, prev=0):
  """Return an array of new strings partitioned by separator string.
  This is done recursively.
  """
  if separator == "":
    raise ValueError("empty separator")
  if string is None:
    return []
  if string == "" and separator is None:
    return []
  if separator is None:
    return [string]
  if stop is None:
    stop = len(string) - len(separator)
  if start > stop:
    return [string[prev:]]
  new_start = start + len(separator)
  if string[start:new_start] == separator:
    return [string[prev:start]] + splitr(string, separator, new_start, stop, new_start)
  else:
    return splitr(string, separator, start+1, stop, prev)
