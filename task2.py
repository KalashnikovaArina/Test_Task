import sys
def dot_state(file1, file2):
  with open(file1, "r") as f:
        lines = f.readlines()
        x, y = map(float, lines[0].split())
        a, b = map(float, lines[1].split())  
  with open(file2) as f:
    for line in f:
        x0, y0 = map(float, line.split())
        if ((x-x0)**2 / a**2 + (y-y0)**2 / b**2 < 1):
          print("1")
        elif ((x-x0)**2 / a**2 + (y-y0)**2 / b**2 == 1):
          print("0")
        elif ((x-x0)**2 / a**2 + (y-y0)**2 / b**2 > 1):
          print("2")
        
dot_state(sys.argv[1], sys.argv[2])