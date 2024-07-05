import time
class Base:
    def __str__(self):
        return str(self.__dict__)
    def __getitem__(self, item):
        return list(self.__dict__)[item]
class timer():
    def start_record_time(self):
        self.start_time=time.time_ns()
    def end_record_time(self):
        self.end_time=time.time_ns()
    def get_time(self):
        return self.end_time-self.start_time