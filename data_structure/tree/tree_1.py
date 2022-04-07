# 리스트나 스택, 큐로 가계도나 조직도를 구현하기가 힘듬 so 계층형 구조를 가진 문제를 해결하기 위한 자료구조 형태가 트리!

# 이진 트리 : 이진 트리의 순회는 재귀 호출을 사용한다. 따라서 전위, 중위, 후위 순회를 간단하게 구현할 수 있음.
# 순회란 모든 원소를 빠트리거나 중복하지 않고 처리하는 연산을 의미함.

class Node :
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

  def __str__(self) :
    return str(self.data)

class Tree :
  def __init__(self):
    self.root = None

# 전위 순위는 DLR 순서로 순회한다

# D: 현재 노드를 출력한다.
# L: 현재 노드 왼쪽 서브트리로 이동한다.
# R: 현재 노드 오른쪽 서브트리로 이동한다.

  def preorderTravel(self, node):
    print(node, end = ' ')
    if not node.left == None : self.preorderTravel(node.left)
    if not node.right == None : self.preorderTravel(node.right)

  # 중위 순회는 LDR 순서로 순회한다.
  # 왼쪽 순회가 우선으로 출력이 중앙에 위치한다.
  def inorderTravel(self, node):
    if not node.left == None : self.inorderTravel(node.left)
    print(node, end = " ")
    if not node.right == None : self.inorderTravel(node.right)


  # 후위 순회는 LRD로 순회한다.
  # 출력이 가장 마지막에 위치한다.

  def postorderTravel(self, node):
    if not node.left == None : self.postorderTravel(node.left)
    if not node.right == None : self.postorderTravel(node.right)
    print(node, end= ' ')
    
  def makeRoot(self, node, left_node, right_node):
    if self.root == None:
      self.root = node
    node.left = left_node
    node.right = right_node


if __name__ == "__main__":
  node = []
  node.append(Node('-'))
  node.append(Node('*'))
  node.append(Node('/'))
  node.append(Node('A'))
  node.append(Node('B'))
  node.append(Node('C'))
  node.append(Node('D'))
  
  m_tree = Tree()
  for i in range(int(len(node)/2)):
    m_tree.makeRoot(node[i], node[i*2+1], node[i*2+2])

  print(       '전위 순회 : ', end='') ; m_tree.preorderTravel(m_tree.root)
  print('\n' + '중위 순회 : ', end='') ; m_tree.inorderTravel(m_tree.root)
  print('\n' + '후위 순회 : ', end='') ; m_tree.postorderTravel(m_tree.root)