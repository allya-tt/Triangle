import math
new_list=[] #список для каждой строки
lists=[] #список для всего треугольника
n=int(input())
for i in range(0, n):
    new_list = []
    for j in range(0, i+1):
        new_list.append(int(math.factorial(i)/(math.factorial(j)*math.factorial(i-j))))
    lists.append(new_list)
for i in range(n):
  print("  " * (n - i), end = " ", sep = " ")
  for j in range(0, i + 1):
      if n>12 and n<17:
          print('{0:5}'.format(lists[i][j]), end="", sep="")
      elif n>=17:
          print('{0:7}'.format(lists[i][j]), end="", sep="")
      else:
          print('{0:4}'.format(lists[i][j]), end="", sep=" ")
  print()
