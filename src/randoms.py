
from inspect import (
  getmembers,
  isfunction,
  getargspec,
)
from random import random

import arrays
import strings
MODULES = [arrays, strings]

def randint(a,b):
  """Return random number n, a <= n < b"""
  return int(random() * (b - a)) + a # implicit floor

# NOTE: I'm a metahelper!
def random_function(*modules):
  """Return a random function selected from set of one or more modules.
  Use this function select function you've already completed to whiteboard.
  Example usage: help(random_function(mymodule1, mymodule2))
  """
  function_tuples = reduce(lambda prev,curr: prev + getmembers(curr, isfunction), modules, [])
  function_count = len(function_tuples)
  function_tuple = function_tuples[randint(0,function_count)]
  return function_tuple[1]

if __name__ == '__main__':
  print help(random_function(*MODULES))
