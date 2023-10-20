class CGP:
    def __init__(self):
        self.math = None
        self.physics = None
        self.english = None
    def calculate(self):
        m = float(self.math)
        p = float(self.physics)
        e = float(self.english)
        total = (m+p+e)/3
        print(total)

if __name__ =='__main__':
    cal = CGP()
    cal.math = input('Please input your math point: ')
    cal.physics = input('Please input your physics point: ')
    cal.english = input('Please input your english point: ')
    cal.calculate()