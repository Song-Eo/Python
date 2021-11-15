class Polynomial:
    def __init__(self):
        self.poly = []

    def degree(self):
        return len(self.poly)

    def eval(self, x):
        total = 0
        for i in range(len(self.poly)):
            total += self.poly[i] * x ** i
        return total

    def add(self, rhs):
        cge = 0
        c = Polynomial()
        if self.degree() < rhs.degree():
            self.poly, rhs.poly = rhs.poly, self.poly
            cge = 1

        c.poly = self.poly

        for i in range(rhs.degree()):
            c.poly[i] += rhs.poly[i]


        if cge == 1:
            self.poly, rhs.poly = rhs.poly, self.poly

        return c

    def sub(self, rhs):
        cge = 0
        c = Polynomial()
        if self.degree() < rhs.degree():
            self.poly, rhs.poly = rhs.poly, self.poly
            cge = 1

        c.poly = self.poly

        for i in range(rhs.degree()):
            c.poly[i] -= rhs.poly[i]


        if cge == 1:
            self.poly, rhs.poly = rhs.poly, self.poly

        return c

    def mul(self, rhs):
        c = Polynomial()
        c.poly = [0 for i in range(self.degree()+rhs.degree()-1)]
        for i in range(self.degree()):
            for j in range(rhs.degree()):
                c.poly[i+j] += (self.poly[i] * rhs.poly[j])

        return c

    def display(self, string):
        print(string, end="")
        for i in range(self.degree()-1, -1, -1):
            if i == 0:
                print(self.poly[i])
            else:
                print(self.poly[i],"x^%d +"%i, end="")

        
                
        
        


def read_poly():
    ls = Polynomial()
    n = int(input("다항식의 최고 차수를 입력하시오:"))
    for i in range(n, -1, -1):
        num = float(input(("x^%d의 계수 :"%i)))
        ls.poly.insert(0,num)
    return ls

a = read_poly()
b = read_poly()
c = a.mul(b)
c.display("C =")
