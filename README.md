# Algorithms
Study for Coding Test & Interview 

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

## Python


```
graph = collections.defaultdict(list)
for x in list(graph):
```
키가 없는 딕셔너리에 대해서 조회시 Null오류가 발생하지 않도록 `defaultdict`로 처리했다. 하지만 오류를 내지 않기 위해 항상 디폴트를 생성하므로 반복문에서 graph 값이 변경된다는 오류가 발생한다. 따라서 `list()`로 묶어서 처리해야 한다. 


# 시간 복잡도 

![image](https://t1.daumcdn.net/cfile/tistory/2302AD48565E816409?download)

![image](https://t1.daumcdn.net/cfile/tistory/256CB448565E81621B?download)

![image](https://t1.daumcdn.net/cfile/tistory/22518148565E816636?download)

![image](https://t1.daumcdn.net/cfile/tistory/277B0F48565E81680F?download)
