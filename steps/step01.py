import numpy as np

class Variable:
    def __init__(self, data):
        self.data = data

class Function:
    def __call__(self, input):
        x = input.data
        y = self.forward(x)
        output = Variable(y)
        return output

    def forward(self, x):
        raise NotImplemetedError()

class Square(Function):
    def forward(self, x):
        return x ** 2

class Sigmoid(Function):
    def forward(self, x):
        return 1/ (1 + np.exp(-x))

class Exp(Function):
    def forward(self, x):
        return np.exp(x)

data = np.array(10)
x = Variable(data)
#f = Square()
f = Sigmoid()
y = f(x)
print(type(y))
print(y.data)