class Calc:
    my_name = "'I'm Calc Module!"
    scale = 0

    def __init__(self, scale=1):
        self.scale = scale

    def __del__(self):
        self.scale = 1
        print("Scale is reset to 1.")

    def add(self, a, b):
        result = a + b
        print("{0:f} + {1:f} = {2:f}".format(a,b,result))
    def sub(self, a, b):
        result = a - b
        print("{0:f} - {1:f} = {2:f}".format(a,b,result))
    def mul(self, a, b):
        result = a * b
        print("{0:f} * {1:f} = {2:f}".format(a,b,result))
    def div(self, a, b):
        if b != 0:
            result = a / b
            print("{0:f} / {1:f} = {2:f}".format(a,b,result))
        else:
            print("Devided by zero!")
