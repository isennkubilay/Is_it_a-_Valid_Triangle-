def checkValidty(a,b,c):
  if (a + b <= c) or (a + c <= b) or (b + c <= a):
    return False
  
  return True
def main():
  x = int(input("Enter the first value: "))
  y = int(input("Enter the second value: "))
  z = int(input("Enter the third value: "))
  if checkValidty(x,y,z):
    print("Valid")
  else:
    print("Invalid")
main()