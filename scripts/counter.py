import time as t

class Counter():

    def __init__(self, wait_time = 0):
        self.wait_time = wait_time

    def count_down(self, wait_time):
        for i in range(self.wait_time):
            print(str(self.wait_time-i) + " seconds remaining \n")
            t.sleep(.1)