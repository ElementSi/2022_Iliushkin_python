class Cursor:
    # Конструктор, принимающий два параметра - координаты X и Y
    def __init__(self, x, y):
        self.m_x = x
        self.m_y = y
        self.m_clickdata = []

    # Передвинуть по оси X на n и по оси Y на m
    # n, m - произвольные целые числа
    def move(self, n, m):
        self.m_x += n
        self.m_y += m

    # Клик в текущем положении курсора
    def click(self):
        self.m_clickdata.append([self.m_x, self.m_y])

    # Вернуть количество кликов в заданном прямоугольнике
    def get_click_count(self, min_x, max_x, min_y, max_y):
        res = 0
        for click in self.m_clickdata:
            if min_x <= click[0] <= max_x and min_y <= click[1] <= max_y:
                res += 1
        return res
