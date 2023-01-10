import torch
import numpy as np
import sys
from Functions import *


# Creating and studying tensors
x = torch.rand(3, 3, dtype=torch.float16)
print(x)
print(x.size())
print()

y = torch.empty(3, 3)
print(y)
print()

x1 = torch.tensor([3, 6])
print(x1)
print()

z = x - y
z1 = torch.div(x, y)
y.add_(x)
print(z1)
print(x[0, :])
print(x[:, 0])
print()

ten1 = torch.rand(2, 2, 1)
print(ten1)
print()
ten2 = torch.empty(1)
print(ten2.item())
print()
ten3 = torch.rand(4, 4)
print(ten3)
print()
t = ten3.view(2, 8)
print(t)
print(t.size())
print()
print()


# Converting numpy array to torch tensors

ten4 = torch.ones(5)
print(ten4, type(ten4))
n = ten4.numpy()
n1 = torch.from_numpy(n)
print(n, type(n))
print(n1, type(n1))

print()

ten4.add_(1)
print(ten4)
print(n)
print()

if torch.cuda.is_available():
    gpu = torch.device('cuda')
    print(gpu, "GTX")
    g = torch.ones(5, device=gpu)
    g1 = torch.ones(5)
    g1.add_(1)
    print('g1', g1, 'cpu')
    g1 = g1.to(gpu)
    ten5 = g + g1
    print(g)
    print('g1', g1, 'gpu')
    print('ten5', ten5, 'gpu')
    ten5 = ten5.to('cpu')
    ten5 = ten5.numpy()
    print('ten5', ten5, 'cpu')
else:
    print("That's a problem!")
print()

x4 = torch.rand(5, requires_grad=True)
print(x4)
