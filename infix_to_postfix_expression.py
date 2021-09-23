# 중위 표기법을 후위 표기법으로 변환

# 1) 피연산자가 들어오면 바로 출력한다.
# 2) 연산자가 들어오면 자기보다 우선순위가 높거나 같은 것들을 빼고 자신을 스택에 담는다.
# 3) 여는 괄호 '('를 만나면 무조건 스택에 담는다.
# 4) 닫는 괄호 ')'를 만나면 '('를 만날 때까지 스택에서 출력한다.

import re

#S = '10+3*(2+4)/2'
#S = '3+5*21/(7-2)'
S = '10+2*3+(4+2)/2'
#S = '(1+4-3)*4/2'
S = re.findall('[0-9]+|[^0-9]', S)
print(S)
st = []
ans = []

op_prior = {
    '*': 0, '/': 0,
    '+': 1, '-': 1
}

for s in S:
    if s == '(':
        st.append(s)
    elif s == ')':
        while len(st) > 0 and st[-1] != '(':
            ans.append(st.pop())
        st.pop()
    elif s in op_prior:
        while len(st) > 0:
            if st[-1] not in op_prior:
                break
            if op_prior[st[-1]] > op_prior[s]:
                break
            ans.append(st.pop())
        st.append(s)
    else:
        ans.append(s)

while len(st) > 0:
    ans.append(st.pop())

print(' '.join(ans))
