# This is a python script file
import random
import sys

if __name__ == '__main__':
  print("Hello Jenkins!")
  
  for i in range(10):
    print(f"Count: {i}")
    
  # trying to pass or fail randomly
  passed = [True, False, None]
  res = random.choice( passed )
  if res is None:
    sys.exit(2)
  elif not res:
    # exit with a string val
    sys.exit("Failed")
