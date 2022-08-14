#Program for global variables

Name = "Shiv"
def myfunc():
 # print("My name is " + Name)

  Name = "ABC"
  print(Name) 
myfunc()

Name = "XYZ"
def myfunc2():
  global Name 
  Name = "ABC" 
  print(Name) 
myfunc2()
print("My name is " + Name)