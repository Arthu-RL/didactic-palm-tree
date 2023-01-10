import torch

x = torch.randn(3, requires_grad=True)
print(x)

y = x+2
z = y*y*2
z = z.mean()
print(y)
print(z)
print()

v = torch.tensor([1, 0.1, 0.001], dtype=torch.float32)
x.backward(v)  # dx/dv, This calculates the gradient
print(x.grad, type(x))

# Make sure pytorch is not tracking the gradients history when you are in a training loop,
# Which will need you to update the weights.

# x.requires_grad_(False)
# y1 = x.detach()
with torch.no_grad():
    y = x + 2
    print(y)
print()

weights = torch.ones(4, requires_grad=True)

for epoch in range(3):
    model_output = (weights*3).sum()
    model_output.backward()  # dmo/dw
    print(weights.grad)

    weights.grad.zero_()

# optimizer = torch.optim.SGD(weights, lr=0.01)
# optimizer.step()
# optimizer.zero_grad()

