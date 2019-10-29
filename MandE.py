import sys
import running
from math import sqrt

argvs = sys.argv

CUT = 1.
I = [i for i in sys.stdin]
for i in I:
 i = (i.splitlines()[0])
 if sqrt(float(i.split(" ")[0])) > 1.: 
  print(sqrt(float(i.split(" ")[0])),end=" ")
  for j in i.split(" ")[1:]:
   print(float(j) * running.matching(sqrt(float(i.split(" ")[0])),argvs[1]) * running.flow(sqrt(float(i.split(" ")[0])), argvs[2]),end=" ")
  print("")
