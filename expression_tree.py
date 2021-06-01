S = '7 4 2 * + 1 -'
S = S.split()

op_list = '+-*/'

tree = {
    # 3:{'data':'*', 'left':1, 'right':2},
    # 1:{'data':'4', 'left':None, 'right':None},
    # 2:{'data':'2', 'left':None, 'right':None},
    # 4:{'data':'+', 'left':0, 'right':3},
    # 0:{'data':'7', 'left':None, 'right':None},
    # 6:{'data':'-', 'left':4, 'right':5},
    # 5:{'data':'1', 'left':None, 'right':None},
}

st = []
for i, s in enumerate(S):
    if s in op_list:
        right = st.pop()
        left = st.pop()
        if right['data'].isdigit():
            tree[right['index']] = {'data':right['data'], 'left':None, 'right':None}
        if left['data'].isdigit():
            tree[left['index']] = {'data':left['data'], 'left':None, 'right':None}
        tree[i] = {'data':s, 'left':left['index'], 'right':right['index']}
        st.append({'index':i, 'data':s})
    else:
        st.append({'index':i, 'data':s})

root = len(S)-1

def cal(N):
    if N == None:
        return ''
    else:
        a = cal(tree[N]['left'])
        b = cal(tree[N]['right'])
        return eval(f"{a}{tree[N]['data']}{b}")

def postorder(N):
    if N == None:
        return []
    else:
        a = postorder(tree[N]['left'])
        b = postorder(tree[N]['right'])
        return [*a] + [*b] + [tree[N]['data']]

def preorder(N):
    if N == None:
        return []
    else:
        a = preorder(tree[N]['left'])
        b = preorder(tree[N]['right'])
        return [tree[N]['data']] + [*a] + [*b]

def inorder(N):
    if N == None:
        return []
    else:
        a = inorder(tree[N]['left'])
        b = inorder(tree[N]['right'])
        return [*a] + [tree[N]['data']] + [*b]

print(f"preorder : {' '.join(preorder(root))}")
print(f"inorder : {' '.join(inorder(root))}")
print(f"postorder : {' '.join(postorder(root))}")
print(f"cal : {cal(root)}")