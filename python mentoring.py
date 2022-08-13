'''
참고 : https://peps.python.org/pep-0008/
problem_ex
1. 파이썬 개발자는 PEP 8을 준수해야 할까요? 만약 그렇다면 왜 준수해야 할까요?
2. 아래의 코드에는 'PEP 8'의 가이드라인에 어긋난 부분이 존재합니다. 어떤 부분이 어긋났고 어떻게 수정하면 될까요?
3. 아래 코드는 무엇을 하는 코드일까요? 이 코드를 실행하면 어떤 결과를 얻게 될까요?
answer_ex

1.가독성을 해친다,일관된 코드를 작성해야만 다른 사람이 코드를 읽기 쉽고 코드의 오해를 줄이는데 도움이 된다.
2.32줄 들여쓰기를 네개의 스페이스 또는 탭을 사용해야한다.
3.2 5 1 3   
  2:두개의 값이 Q에 들어가있기 때문에 2가 출력된다.
  5:Q는 선입선출에 구조를 가지고 있기 때문에 오래된 데이터인 5가 출력된다.
  1:Q의  저장공간에 있는  데이터의 개수 출력
  3:저장공간에 있는 가장 오래된 데이터 출력 


'''
class Empty(Exception):
    pass

class ArrayQueue:

    def __init__(self):
        self._data = []

    
    def __len__(self):
        return len(self._data)
    
    def is_empty(self):
        if len(self._data):
            return False
        else:
            return True


    def first(self):
        if len(self._data) == False:
            raise Empty("error")
        else:
            return self._data[0]

    def dequeue(self):
        if len(self._data) == False:
            raise Empty("error")

        val = self._data[0]
        del self._data[0]
        return val


    def enqueue(self, e):
        self._data.append(e)


Q = ArrayQueue()
Q.enqueue(5)
Q.enqueue(3)        
print(len(Q))
print(Q.dequeue())
print(len(Q))
print(Q.first())
