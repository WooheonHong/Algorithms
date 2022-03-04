Algorithms
=================================

Study for Coding Test & Interview 

# 테스트 진행 팁 

1. 예시보면서 문제 빠르게 이해
2. 조건 확실히 이해 
3. 테스트 케이스 진행(여기서 한번 제출) 
4. 엣지 케이스 진행 

# 참고사항 

- 1초에 1억번이라고 가정하면 주어진 데이터의 nlogn, n^2, n^3등을 해보면 필요한 시간복잡도가 대강 나온다. 
- 반환값의 타입에 유의하자. 


# 준비 



## VSCode

다음 Extension을 설치한다.

- dark+ theme 
- Gist 
- gitlens
- Settings Sync(상황에 따라) 
- Python 

## code snippet

VSCode Gist extension을 설치하면 다음을 수행할 수 있다.

1. Command+Shift+p를 눌러서 Gist: select profile을 통해 생성된 Token을 등록

2. Gist:Insert Text From Gist File 을 사용하면 코드 스니핏을 가져올 수 있다. 

# Python

## 주의 

- 슬라이싱은 매번 새롭게 객체를 생성해서 할당하므로 주의한다. 
- 중첩함수
    - global 변수를 재할당하면 로컬 변수로 선언됨. 재할당 하지 않고 변경하면 global변수도 변경됨. 
    - 불변객체인 경우 중첩 함수 내에서 변수의 값을 조작할 수 없으므로 클래스 변수를 활용할 수 있다. 
- 복잡한 list는 `copy.deepcopy()`로 처리해야 함. 


## Tip

- for루프와 i, -i 를 사용하는 것 보다 while left<right ; left += 1 , right -= 1 을 사용하는 것이 편하다. 
- 정렬 관련 함수들의 정렬순서
    - `logs.sort(key=lambda x: (x.split()[1:], x.split()[0]))` :  logs의 각 성분들을 split해서 리스트로 쪼갠뒤 x[1:], x[0]으로 정렬 
    - `heapq.heappush(heap, (abs(i), i, i))` i를 heap에 삽입하는데 절댓값이 작은 것 부터 우선순위를 주고 절댓값이 같으면 값이 작은걸로 
- list 합치기 
```
a = [1]
b = [2, 3]
# a += b
# a = [1, 2, 3]

# a += b, 
# a = [1, [2, 3]]

# a += [b]
# a = [1, [2, 3]]
```
- 여러 개를 할당해야하는 경우 참조가 헷갈리면 다중 할당으로 처리해버리자. 변수 스왑도 이 방식으로
- 투 포인터는 정렬된 배열에 사용한다. 
- 숫자 및 영문자만 남기기 `s = re.sub('[^a-z0-9], '', s)`. \w는 단어를 의미 
- 문자열을 조작할 때는 항상 슬라이싱을 우선으로 사용 
    - `S[:]` : 참조가 아닌 값을 복사하기 위해 `[:]`사용 가능 
        - `s = s[::-1]`은 메모리 오류가 뜰 수 있으므로 `s[:] = s[::-`]
    - `S[::-1]` : 뒤집는다.
    - `S[::2]` : 2칸씩 앞으로 이동한다. 
- 메모리 사용을 줄이기 위해 제너레이터 사용을 고려해보자. 
- 몫과 나머지를 동시에 구하려면 `divmod()`
- 전체 골격을 잡고 코딩할 때는 `pass`사용 
- IDE를 쓰지 못할 때를 대비해서 디버깅은 `print()`와 `locals()`이용 
- `print()`의 sep파라미터, end파라미터
- 리스트를 출력할 때는 `''.join()`으로 묶어서 처리 
- 특정 메소드나 함수 내부에서 `pprint.pprint(locals())`를 사용해 디버깅에 활용 
- 시간이 남으면 타입 힌트 정리 
- 간단한 주석을 남겨서 가독성을 높이기 
- 함수의 인자로 immutable object 사용하기. None을 명시적으로 할당하는 것도 좋음.  
- `any()`는 포함된 값 중 어느 하나가 참이라면 항상 참으로 출력
- `all()`은 모든 값이 참이여야 True 반환 
```
# No
def foo(a, b=[]):
    ...
def foo(a, b: Mapping = {}):
    ...

# Yes
def foo(a, b=None):
    if b is None:
        b = []
def foo(a, b: Optional[Sequence] = None):
    if b is None:
        b = []
```


## 자료형 
- int는 object의 하위 클래스. bool은 int의 하위 클래스 
- 파이썬의 유일한 mapping 타입은 딕셔너리
- set은 입력 순서가 유지되지 않으며, 중복된 값이 있을 경우 하나의 값만 유지 
- 파이썬에서 모든 것은 객체다. 
    - immutable : str, tuble, bytes, int, float. 불변 객체로 key를 정할 수 있다.
    - mutable : list, set, dict 
- 파이썬은 원시타입(primitive type)을 지원하지 않는다. 
- 가변 객체를 참조하고 있다면 참조 변수에서 값을 조작하는 경우 참조 대상의 변수도 변경됨. 
- `is`는 `id()`값을 비교하는 함수이고 `==`는 값을 비교하는 연산자다. 

## 자료구조 
- `list()`는 자유롭게 값을 추가, 삭제할 수 있는 동적 배열 
- 동적 배열에 동일한 자료형을 가진 객체를 삽입하지 않아도 된다. 
- `del a[1]`로 인덱스의 위치에 있는 값 제거. `a.remove(3)`로 해당하는 요소 삭제  
- 딕셔너리는 내부적으로 해시 테이블로 구현되어 있다. 모든 불변 객체를 키로 사용 가능(이 과정을 해싱). 
- 대부분의 언어에서는 해시 테이블을 이용한 자료형은 입력 순서가 유지되지 않는다. 파이썬 3.6이하에서는 `collections.OrderedDict()`를 사용해야 했으나 3.7부터는 입력 순서가 유지된다. 
- 키가 없는 딕셔너리에 대해서 조회시 Null오류가 발생하지 않도록 `collections.defaultdict`로 처리할 수 있다. 그러면 조회 시 항상 디폴트 값을 생성해 키 오류를 방지할 수 있다. 하지만 항상 디폴트를 생성하므로 반복문에서 graph 값이 변경된다는 오류가 발생한다. 따라서 `list()`로 묶어서 처리해야 한다.  
- `collections.Counter()`
    - collections.Counter클래스는 딕셔너리를 한번 더 wrapping 한 것임.
    - `b.most_common(k)`으로 상위 빈도 k개 탐색 
    - 존재하지 않는 키의 경우 0을 출력한다. 
- `collections.deque()` list의 pop(0)이 O(n)이지만 데크의 popleft는 O(1)이다. 
- 리스트에서 존재하지 않는 인덱스 조회 : `IndexError`. 딕셔너리에서 존재하지 않는 키 조회 : `KeyError`. 이런 경우에는 예외처리로 별도 추가 작업 가능 
- 딕셔너리와 set둘 다 {}를 사용하지만 key의 존재 유무로 다른 자료형으로 선언됨

```
graph = collections.defaultdict(list)
for x in list(graph):
```



# 시간 복잡도 

![image](https://t1.daumcdn.net/cfile/tistory/2302AD48565E816409?download)

여기서 hash table의 시간 복잡도는 key를 조회해서 값 리턴, 키 존재 확인 등을 의미

![image](https://t1.daumcdn.net/cfile/tistory/256CB448565E81621B?download)

![image](https://t1.daumcdn.net/cfile/tistory/22518148565E816636?download)

![image](https://t1.daumcdn.net/cfile/tistory/277B0F48565E81680F?download)

# 다시 풀 문제 

1. [reorder log files](https://leetcode.com/problems/reorder-data-in-log-files/)
2. [쇠막대기](https://www.acmicpc.net/problem/10799)
3. [괄호의값](https://www.acmicpc.net/problem/2504)
4. (나중에) [logest palindrome substring](https://leetcode.com/problems/longest-palindromic-substring/) 
5. [remove duplicate letters](https://leetcode.com/problems/remove-duplicate-letters/)
6. [daily temperatures](https://leetcode.com/problems/daily-temperatures/)
7. [Next Greater Element I](https://leetcode.com/problems/next-greater-element-i/) 
8. [Course Schedule](https://leetcode.com/problems/course-schedule/)
9. [섬의 개수](https://leetcode.com/problems/number-of-islands/)
10. [이진 트리의 최대 깊이](https://leetcode.com/problems/maximum-depth-of-binary-tree/)
11. [이진 트리의 직경](https://leetcode.com/problems/diameter-of-binary-tree)
