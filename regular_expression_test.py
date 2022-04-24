import re

# re 모듈

# re.compile(pattern, flags=0)
# 정규식 패턴을 정규식 객체로 컴파일

# re.search(pattern, string, flags=0)
# string을 통해 스캔하여 정규식 pattern이 일치하는 첫 번째 위치를 찾고, 대응하는 일치 객체를 반환합니다. 문자열의 어느 위치도 패턴과 일치하지 않으면 None을 반환

# re.match(pattern, string, flags=0)
# string 시작 부분에서 0개 이상의 문자가 정규식 pattern과 일치하면, 해당 일치 객체를 반환합니다. 문자열이 패턴과 일치하지 않으면 None을 반환

# re.fullmatch(pattern, string, flags=0)
# 전체 string이 정규식 pattern과 일치하면, 해당하는 일치 객체를 반환합니다. 문자열이 패턴과 일치하지 않으면 None을 반환

# re.split(pattern, string, maxsplit=0, flags=0)
# string을 pattern으로 나눕니다. pattern에서 포착하는 괄호가 사용되면 패턴의 모든 그룹 텍스트도 결과 리스트의 일부로 반환됩니다.
# maxsplit이 0이 아니면, 최대 maxsplit 분할이 발생하고, 나머지 문자열이 리스트의 마지막 요소로 반환

# re.findall(pattern, string, flags=0)

# re.finditer(pattern, string, flags=0)
# string에서 겹치지 않는 RE pattern의 모든 일치를 일치 객체를 산출하는 이터레이터로 반환합니다.
# string은 왼쪽에서 오른쪽으로 스캔 되고, 일치는 찾은 순서대로 반환됩니다. 빈 일치가 결과에 포함

# re.sub(pattern, repl, string, count=0, flags=0)
# string에서 겹치지 않는 pattern의 가장 왼쪽 일치를 repl로 치환하여 얻은 문자열을 반환합니다. 패턴을 찾지 못하면, string이 변경되지 않고 반환

# re.subn(pattern, repl, string, count=0, flags=0)
# sub()와 같은 연산을 수행하지만, 튜플 (new_string, number_of_subs_made)를 반환

# re.escape(pattern)
# pattern에서 특수 문자를 이스케이프 처리합니다. 이것은 정규식 메타 문자가 포함되어있을 수 있는 임의의 리터럴 문자열을 일치시키려는 경우에 유용

# Pattern 객체

# Pattern.match() : 문자열의 시작 부분에서 RE가 일치하는지 판단합니다.
# Pattern.search() : 이 RE가 일치하는 위치를 찾으면서, 문자열을 훑습니다.
# Pattern.findall() : RE가 일치하는 모든 부분 문자열을 찾아 리스트로 반환합니다.
# Pattern.finditer() : RE가 일치하는 모든 부분 문자열을 찾아 이터레이터로 반환합니다.
# Pattern.sub()

# Match 객체

# Match.expand(template)
# sub() 메서드에서 수행되는 것처럼, 템플릿 문자열 template에 역 슬래시 치환을 수행하여 얻은 문자열을 반환

# Match.group([group1, ...])
# 일치의 하나 이상의 서브 그룹을 반환합니다. 단일 인자가 있으면, 결과는 단일 문자열입니다;
# 인자가 여러 개면, 결과는 인자당 하나의 항목이 있는 튜플입니다. 인자가 없으면, group1의 기본값은 0입니다 (전체 일치가 반환됩니다).

# Match.groups(default=None)
# 1에서 패턴에 있는 그룹의 수까지, 일치의 모든 서브 그룹을 포함하는 튜플을 반환합니다.
# default 인자는 일치에 참여하지 않은 그룹에 사용됩니다; 기본값은 None입니다.

# Match.groupdict(default=None)
# 일치의 모든 이름 있는 서브 그룹을 포함하고, 서브 그룹의 이름을 키로 사용하는 딕셔너리를 반환합니다.
# default 인자는 일치에 참여하지 않은 그룹에 사용됩니다; 기본값은 None입니다.

# Match.start([group])
# Match.end([group])
# group과 일치하는 부분 문자열의 시작과 끝 인덱스를 반환합니다;
# group의 기본값은 0입니다 (전체 일치 문자열을 뜻합니다). group이 있지만, 일치에 기여하지 않으면, -1을 반환

# Match.span([group])
# 일치가 m일 때, 2-튜플 (m.start(group), m.end(group))를 반환합니다.
# group이 일치에 기여하지 않으면, 이것은 (-1, -1)임에 유의하십시오. group의 기본값은 0으로, 전체 일치입니다.

s = '010-1234-5678-9'
p = re.compile(r'\d{3}-\d{3,4}-\d{4}')
m = p.match(s) # 시작부터만 일치하면 되고, 해당 부분을 찾은 뒤에는 더 이상 찾지않음
if m:
  print('일치')
else:
  print('불일치')

s = '010-1234-5678-9'
p = re.compile(r'\d{3}-\d{3,4}-\d{4}')
m = p.fullmatch(s) # 시작부터 끝까지 모두 일치해야 함
if m:
  print('일치')
else:
  print('불일치')

s = 'I was born on January 4, 1993'
p = re.compile(r'[0-9]+') # 가장 처음으로 일치하는 부분만 찾음
m = p.search(s)
print(m.span())

s = 'I am a boy'
p = re.compile(r'\b[a-zA-Z0-9]+\b')
print(p.findall(s)) # 일치하는 모든 부분을 찾고 리스트로 반환
# ['I', 'am', 'a', 'boy']

s = '1 2 Fizz 4 Buzz Fizz 7 8'
p = re.compile(r'[0-9]+')
print(p.sub('n', s)) # 일치하는 부분을 첫번째 인자로 바꿈
# n n Fizz n Buzz Fizz n n
