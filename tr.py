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
    print('{0:3}'.format(lists[i][j]), end=" ", sep=" ")
  print()
