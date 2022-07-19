T = int (input())
x,y = map(int, input().split())

count: int = 0

for i in range(T):
  if x < y:
    while x != y:
      x += 1
      count += 1 
 
  if x > y:
    while x != y:
      y += 1
      count +=1 
    
