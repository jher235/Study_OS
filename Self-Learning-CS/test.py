from multiprocessing import Process
import os


# print("my pid is: ", os.getpid()) #프로세스의 pid 값을 출력함. 그때 그때 운영체제에서 부여해주는 값이기 때문에 실행할 때마다 값이 달라진다. 


# def foo(): #foo는 
#     print('foo: child process: ', os.getpid()) #foo를 실행해주는 자식 프로세스의 pid를 찍어주고 
#     print('foo: parent process: ', os.getppid()) #부모 프로세스의 pid를 출력 

# if __name__ == '__main__':
#     print('parent process', os.getpid()) # 먼저 이 파이썬 코드 자체의 프로세스 pid가 출력됨 
#     child = Process(target=foo).start() # 자식 프로세스를 생성함. 이 자식 프로세스는 foo를 실행해주는 프로세스. 
#     child2 = Process(target=foo).start() # 자식 프로세스를 생성, 이 때 실행되는 foo의 부모 프로세스는 동일함 
#     child3 = Process(target=foo).start() # 자식 프로세스를 생성, 이 때 실행되는 foo의 부모 프로세스는 동일함


def foo():
    print('foo executed!')

def bar(): 
    print('bar executed!')

def baz():
    print('baz executed!')

if __name__ == '__main__': #동시에 수행해야 하는 각기 다른 작업을 아래와 같이 프로세서를 실행해서 할 수 있다. 
    child = Process(target=foo).start() # 자식 프로세스를 생성함. 이 자식 프로세스는 foo를 실행해주는 프로세스. 
    child2 = Process(target=bar).start() # 자식 프로세스를 생성, bar 함수 실행
    child3 = Process(target=baz).start() # 자식 프로세스를 생성, baz 함수 실행 