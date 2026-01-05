class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def newNode():
    temp = node(-1)
    temp.left = None
    temp.right = None
    return(temp);
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
def check(root, nodes_list):
    if root:
        if check(root.left, nodes_list) == 0:
            return False

        if len(nodes_list) != 0:
            if root.data in nodes_list or root.data < nodes_list[-1]:
                return 0

        nodes_list.append(root.data)

        if check(root.right, nodes_list) == 0:
            return False


def check_binary_search_tree_(root):
    nodes_list = []
    if check(root, nodes_list) in [False, 0]:
        return False
    else:
        return True

ht = int(input())
cnt = 0
values = map(int, input().split(' '))
values = list(values)
root  = newNode()
def inorder(root, ht):
    global cnt
    global values
    if cnt == len(values):
        return
    else:
        if(ht>0):
            root.left = newNode();
            inorder(root.left, ht-1);
        root.data = values[cnt];
        cnt+=1
        if(ht>0):
            root.right = newNode();
            inorder(root.right, ht-1);
inorder(root, ht);
if(check_binary_search_tree_(root)):
    print("Yes")
else:
    print("No")