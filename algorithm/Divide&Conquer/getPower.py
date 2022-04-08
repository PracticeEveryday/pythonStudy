A, B = map(int, input().split())
print(B//2)
def getPower(A, B):
  if B == 0:
    return 1
  elif B % 2 == 0 :
    return getPower(A, B // 2) * getPower(A, B // 2)
  else :
    return getPower(A, B // 2)*A*getPower(A, B // 2)

print(getPower(A, B))