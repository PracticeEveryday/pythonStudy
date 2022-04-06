class Node:
  def __init__(self, val):
    self.val = val
    self.next = None
  
  def value(self,):
    return self.next.val

class Linked_list :
  def __init__(self):
    self.head = None
    self.tail = None

    self.no = 0

  def add_Node(self, Node):
    if self.head == None and self.tail == None:
      self.head = Node
      self.tail = Node

      self.no += 1
    else :
      self.tail.next = Node
      self.tail = Node

      self.no += 1
  
  def __len__(self):
    return self.no

a = Node(1)
b = Node(2)
LinkedList = Linked_list()
LinkedList.add_Node(a)
LinkedList.add_Node(b)
print(a.next)
print(LinkedList.__len__())
print(a.value())



# def printNodes():
#   current_node = Node
#   while current_node is not None:
#     print(current_node.val, end =' ')
#     current_node = current_node.next

# printNodes(head_node)

# a = 1
# b = a

# b = 2
# a = 3
# print(a, b)