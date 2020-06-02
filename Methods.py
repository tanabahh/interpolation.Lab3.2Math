import math
MaxIT = 1000000


class Interpolation:
    def __init__(self, count_of_dots, function):
        self.count_of_dots = count_of_dots
        self.function = function
        self.array_with_dots = []
        self.a = 0
        self.b = 10*math.pi
        self.h = (self.b - self.a)/self.count_of_dots
        i = self.a

        while i < self.b:
            self.array_with_dots.append([i, self.function(i)])
            i += self.h

    def get_value(self, x):
        return self.array_with_dots[x-1][1]

    def set_value(self, x, y):
        self.array_with_dots[x-1][1] = y

    def lagrange(self, x):
        y = 0
        for i in range(self.count_of_dots):
            L = 1
            for j in range(self.count_of_dots):
                if j != i:
                    L *= (x-self.array_with_dots[j][0])/(self.array_with_dots[i][0] - self.array_with_dots[j][0])
            y += L*self.array_with_dots[i][1]
        return y

    def get_dots_for_function(self):
        i = self.a
        array_with_answer = []
        while i <= self.b:
            array_with_answer.append([i, self.lagrange(i)])
            i += 0.1
        print(array_with_answer)
        return array_with_answer

