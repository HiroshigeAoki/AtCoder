import time

class elapsedTime:
    def __init__(self, name, func=None):
        self.name = name
        self.func = func
    def __call__(self, *args):
        if self.func == None:
            raise ValueError()
        start = time.perf_counter()
        self.func(*args)
        print(f'{self.name}: {time.perf_counter() - start}')
    def start(self):
        self.start = time.perf_counter()
    def end(self):
        print(f'{self.name}: {time.perf_counter() - self.start}')
        
        