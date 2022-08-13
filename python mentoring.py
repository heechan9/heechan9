'''
참고 : https://peps.python.org/pep-0008/
problem_ex
1. 파이썬 개발자는 PEP 8을 준수해야 할까요? 만약 그렇다면 왜 준수해야 할까요?
2. 아래의 코드에는 'PEP 8'의 가이드라인에 어긋난 부분이 존재합니다. 어떤 부분이 어긋났고 어떻게 수정하면 될까요?
3. 아래 코드는 무엇을 하는 코드일까요? 이 코드를 실행하면 어떤 결과를 얻게 될까요?
answer_ex

1.가독성을 해친다,일관된 코드를 작성해야만 다른 사람이 코드를 읽기 쉽고 코드의 오해를 줄이는데 도움이 된다.
2.
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