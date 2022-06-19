import time
import threading
from typing import Callable, Union

class PyEvent:
    id: "str"

    def __init__(self, id) -> None:
        self.id = id

class PyEventQueue:
    event_list: "list[PyEvent]"

    def __init__(self) -> None:
        self.event_list = []


    def push(self, event):
        self.event_list.append(event)


    def pop(self) -> Union[PyEvent, None]:
        if len(self.event_list) == 0:
            return None

        return self.event_list.pop(0) 


class PyObserver:
    event_queue: PyEventQueue
    events_map: "dict[str, Callable]"
    observing: bool

    def __init__(self) -> None:
        self.event_queue = PyEventQueue()
        self.events_map = dict()
        self.observing = False


    def push(self, event: PyEvent):
        self.event_queue.push(event)


    def __pop(self) -> Union[PyEvent, None]:
        return self.event_queue.pop()


    def register(self, event: PyEvent, function: Callable):
        self.events_map[event.id] = function


    def start(self):
        if self.observing:
            return
        
        self.observing = True
        threading.Thread(target=self.__observe, daemon=True).start()


    def stop(self):
        self.observing = False


    def __observe(self):
        while self.observing:
            evt = self.__pop()

            if evt is None:
                time.sleep(1)
                continue

            handler = self.events_map[evt.id]

            if handler is not None:
                handler()

