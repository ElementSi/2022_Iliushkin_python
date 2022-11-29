class Clock:
    def __init__(self):
        self.hours = 0
        self.minutes = 0

    def tick(self, minutes):
        if minutes < 0:
            raise Exception('RuntimeError')

        self.minutes += minutes

        if self.minutes >= 60:
            self.hours += self.minutes // 60
            self.minutes -= (self.minutes // 60) * 60

        if self.hours >= 24:
            self.hours -= (self.hours // 24) * 24

    def get_time(self):
        time_tuple = (self.hours, self.minutes)
        return time_tuple


c = Clock()
print(c.get_time())
c.tick(1380)
print(c.get_time())
c.tick(30)
print(c.get_time())
c.tick(30)
print(c.get_time())
c.tick(30)
print(c.get_time())
