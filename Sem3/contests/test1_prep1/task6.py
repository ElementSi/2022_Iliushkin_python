class GasStation:
    def __init__(self, capacity):
        self.m_capacity = capacity
        self.m_fuel = 0

    def fill(self, n):
        if self.m_fuel + n > self.m_capacity:
            raise()
        else:
            self.m_fuel += n

    def tank(self, n):
        if self.m_fuel < n:
            raise()
        else:
            self.m_fuel -= n

    def get_limit(self):
        return self.m_fuel
