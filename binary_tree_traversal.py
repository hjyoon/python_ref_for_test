tree = {
        'A':{'left':'B', 'right':'C'},
        'B':{'left':'D', 'right':None},
        'C':{'left':'E', 'right':'F'},
        'D':{'left':None, 'right':None},
        'E':{'left':None, 'right':None},
        'F':{'left':None, 'right':'G'},
        'G':{'left':None, 'right':None},
    }

root = 'A'

def postorder(N):
    if N == None:
        return []
    else:
        a = postorder(tree[N]['left'])
        b = postorder(tree[N]['right'])
        return [*a] + [*b] + [N]

def preorder(N):
    if N == None:
        return []
    else:
        a = preorder(tree[N]['left'])
        b = preorder(tree[N]['right'])
        return [N] + [*a] + [*b]

def inorder(N):
    if N == None:
        return []
    else:
        a = inorder(tree[N]['left'])
        b = inorder(tree[N]['right'])
        return [*a] + [N] + [*b]

print(f'postorder : {" ".join(postorder(root))}')
print(f'preorder : {" ".join(preorder(root))}')
print(f'inorder : {" ".join(inorder(root))}')