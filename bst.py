class node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


def insert(root,key):
    if root is None:
        return node(key)
    else:
        if root.data == key:
            return root
        elif root.data < key:
            root.right = insert(root.right,key)
        else :
            root.left = insert(root.left,key)
    return root
def max(root):
    z = root
    while(z.right):
        z = z.right
    return(z.data)
def min(root):
    z = root
    while(z.left):
        z = z.left
    return(z)
def max_left(root):
    z = root.left
    while(z.right):
        z = z.right
    return(z.data)
def min_right(root):
    z = root.right
    while(z.left):
        z = z.left
    return(z.data)

def delete(root,key):
    if root is None:
        return root
    if key < root.data:
        root.left = delete(root.left,key)
    elif key > root.data:
        root.right = delete(root.right,key)
    else :
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        temp = min(root.right)
        root.data = temp.data
        root.right = delete(root.right,temp.data)
    return root
    
    

def inorder(root):
    if root :
        inorder(root.left)
        print(root.data,end = "  ")
        inorder(root.right)
def preorder(root):
    if root :
        print(root.data,end = "  ")
        preorder(root.left)
        preorder(root.right)


if __name__ == "__main__":
    r = None
    for i in range(6):
        r = insert(r,int(input("Enter Your number :")))
    inorder(r)
    print("")
    preorder(r)
    print("")
    delete(r,int(input("Enter Your number :")))
    inorder(r)
    print("")
    preorder(r)
    print("")

