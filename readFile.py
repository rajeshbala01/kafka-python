

def read_file():
 g = input("Enter your real path of the file : ") 
 f = open(g, "r")
 for x in f:
  print(x)
 f.close

read_file()