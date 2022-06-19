from event import PyObserver

observer = None

if observer is None:
    print("Observer initialized")
    observer = PyObserver()
    observer.start()
