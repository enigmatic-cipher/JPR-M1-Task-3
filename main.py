"""
Given n as input, print the following pattern
Input. n -> 4
Output:
1:A 
2:AB 
3:ABA 
4:ABAB
"""

n = 4
pt1 = 'A'
pt2 = 'B'
st = ''
for i in range(1,n+1):
  if (i%2 != 0):
    st = st + pt1
  else:
    st = st + pt2
  print(f"{i}:{st}")
