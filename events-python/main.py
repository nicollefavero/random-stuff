import engine
import time
import test
from event import PyEvent

if __name__=="__main__":
    def handler1():
        print("1")

    def handler2():
        print("2")

    def handler3():
        print("3")

    test.teste()

    engine.observer.register(PyEvent("button1"), handler1)
    engine.observer.register(PyEvent("button2"), handler2)
    engine.observer.register(PyEvent("button3"), handler3)

    engine.observer.push(PyEvent("button3"))
    engine.observer.push(PyEvent("button2"))
    engine.observer.push(PyEvent("button1"))

    time.sleep(3)

    engine.observer.push(PyEvent("button2"))

    time.sleep(3)
