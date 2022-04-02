
class ListPipe : 
  def __init__(self) :
    self.myPipe = []
  
  def addLeft(self, n) :
    self.myPipe.insert(0,n)
  
  def addRight(self, n) :
    self.myPipe.append(n)

  def getBeads(self) :
    return self.myPipe

def processBeads(myInput) :

  myPipe = ListPipe()

  for bead, direction in myInput:
    if direction == 0 :
      myPipe.addLeft(bead)
    elif direction == 1 :
      myPipe.addRight(bead)

  result = myPipe.getBeads()

  return result


def main():

  n = int(input())
  app_list = []
  lst = []

  for j in range(n):
    for i in input().split():
      app_list.append(int(i))

      if(len(app_list) == 2) :
        lst.append(app_list)

      if(len(app_list)>= 2):
        app_list = []
      

  # for i in range(n):
  #   lst.append([int(i) for i in input().split()])

  print(*processBeads(lst))

if __name__ == "__main__":
  main()