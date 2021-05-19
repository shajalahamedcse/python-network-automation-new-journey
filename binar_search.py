print("Insert numbers")
x = input()

print("Number you want to search:")
y = int(input())

li = x.split(",")
ele = []
for x in li:
  ele.append(int(x))

ele.sort()
print(ele)
## Data Preproccess

low = 0
high = len(ele)-1
gate = True
if y < ele[0] or y>ele[high]:
    gate = False 

while low <= high and gate:
  mid = int((low+high)/2)
  print("hi1y")
  if ele[mid]>y:
      high = mid
      continue
  if ele[mid]<y:
      print("hi")
      low= mid
      continue
  if ele[mid]==y:
      print(mid)
      break
