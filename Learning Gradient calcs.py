import torch
import numpy as np
import sys
from Functions import *

x = torch.tensor(1.0)
y = torch.tensor(2.0)

w = torch.tensor(1.0, requires_grad=True)

# Forward pass and compute loss

y_hat = w * x
loss = (y_hat - y)**2

print(loss)

loss.backward()  # dl/dw
print(w.grad)

# Update weights > w.grad.zero_()
# Next forward and backward pass

"""
dl/dw = lim| loss(y_hat + dw) - loss(y_hat)/dw

dl/dw = lim| loss(-1 + dw)^2 - 1/dw

dl/dw = lim| dw^2 - 2dw + 1 - 1/dw

dl/dw = lim| -2dw + dw^2/dw

dl/dw = -2

"""