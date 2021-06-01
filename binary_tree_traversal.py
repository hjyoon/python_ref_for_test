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
trace = []

def postorder(N):
    if N == None:
        return
    else:
        postorder(tree[N]['left'])
        postorder(tree[N]['right'])
        trace.append(N)

def preorder(N):
    if N == None:
        return
    else:
        trace.append(N)
        preorder(tree[N]['left'])
        preorder(tree[N]['right'])

def inorder(N):
    if N == None:
        return
    else:
        inorder(tree[N]['left'])
        trace.append(N)
        inorder(tree[N]['right'])

trace.clear()
postorder(root)
print(f'postorder : {"".join(trace)}')

trace.clear()
preorder(root)
print(f'preorder : {"".join(trace)}')

trace.clear()
inorder(root)
print(f'inorder : {"".join(trace)}')