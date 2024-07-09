import os
import threading 

def foo():
    print('foo: thread id: ', threading.get_native_id()) #get_native_id를 통해 고유한 스레드의 번호를 받아올 수 있다.
    print('foo: my pid is: ', os.getpid()) #이 pid값은 이전에 main에서 출력한 pid 값과 동일하다.(여러 스레드에서 이 메소드를 각각 실행하더라도 같다.) -> 스레드는 프로세스의 자원을 공유하고 있는 흐름이므로 

def bar():
    print('bar: thread id: ', threading.get_native_id()) 
    print('bar: my pid is: ', os.getpid()) 

def baz():
    print('baz: thread id: ', threading.get_native_id()) 
    print('baz: my pid is: ', os.getpid()) 


if __name__ == '__main__':
    print('my pid is: ', os.getpid())
    thread1 = threading.Thread(target=foo).start() #스레드를 생성. 이 스레드에서는 foo함수를 실행함 
    thread2 = threading.Thread(target=bar).start()
    thread3 = threading.Thread(target=baz).start()


