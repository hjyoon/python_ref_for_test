import collections

class Node(dict):
        def __init__(self):
            super().__init__()
            self.final = False;
            self.out = set();
            self.fail = None;
            
        def addout(self,out):
            if type(out) is set:
                self.out = self.out.union(out)
            else :
                self.out.add(out)
        
        def addchild(self,alphabet,node = None):
            self[alphabet] = Node() if node is None else node

class Aho_Corasick():
    def __init__(self,patterns):
        self.patterns = patterns
        self.head = Node()
        self.maketrie()
        self.constructfail()
        
    def search(self,sentence):
        crr = self.head
        ret = []
        for c in sentence :
            while crr is not self.head and c not in crr:
                crr = crr.fail
            if c in crr:
                crr = crr[c]
            
            if crr.final:
                ret.extend(list(crr.out))
        return ret
    
    def maketrie(self):
        for pattern in self.patterns:
            crr = self.head
            for c in pattern :
                if c not in crr:
                    crr.addchild(c)
                crr = crr[c]
            crr.final = True
            crr.addout(pattern)
            
    def constructfail(self):
        queue = collections.deque()
        self.head.fail = self.head
        queue.append(self.head)
        while queue:
            crr = queue.popleft()
            for nextc in crr:
                child = crr[nextc]
                if crr is self.head:
                    child.fail = self.head
                else :
                    f = crr.fail
                    while f is not self.head and nextc not in f:
                        f = f.fail
                    if nextc in f:
                        f = f[nextc]
                    child.fail = f

                child.addout(child.fail.out)
                child.final |= child.fail.final
                queue.append(child)

p = {'ad', 'abc', 'bcd', 'abab', 'ababc'}
ac = Aho_Corasick(p)
print(ac.search('eabcdeababababcd'))

# dictionary 를 사용하여 aho-corasick 모방하기

S = 'eabcdeababababcd'
p = {'ad', 'abc', 'bcd', 'abab', 'ababc'}
ans = {'ad':0, 'abc':0, 'bcd':0, 'abab':0, 'ababc':0}
graph = {}

for s in p:
    tmp = ''
    for c in s:
        tmp += c
        if tmp not in graph:
            graph[tmp] = {'valid':False, 'pi':None, 'indexes':None}
    graph[tmp]['valid'] = True

for k in graph.keys():
    for i in range(1, len(k)):
        t = k[i:]
        if t in graph:
            graph[k]['pi'] = t
            break

for k in graph.keys():
    s = set()
    pi = k
    while True:
        if pi == None:
            break
        else:
            s.add(pi)
            pi = graph[pi]['pi']
    graph[k]['indexes'] = s

pre = None
tmp = None
i = 0
while i < len(S):
    pre = tmp
    if tmp == None:
        tmp = S[i]
    else:
        tmp += S[i]
    if tmp in graph:
        pi = tmp
        for v in graph[pi]['indexes']:
            if graph[v]['valid'] == True:
                ans[v] += 1
        i += 1
    else:
        if pre in graph:
            tmp = graph[pre]['pi']
        else:
            tmp = None
            i += 1

#print(graph)
print(ans)