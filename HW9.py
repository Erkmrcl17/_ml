import torch
import matplotlib.pyplot as plt

x = torch.empty(100, 1).uniform_(0, 10)
noise = torch.empty(100, 1).uniform_(-2.5, 2.5)
y = -x + noise

w = torch.randn(1, requires_grad=True)
b = torch.randn(1, requires_grad=True)
lr = 0.01

for epoch in range(1000):
    pred = x * w + b
    loss = ((pred - y) ** 2).mean()
    loss.backward()

    with torch.no_grad():
        w -= lr * w.grad
        b -= lr * b.grad
    w.grad.zero_()
    b.grad.zero_()

    if (epoch + 1) % 100 == 0:
        print(f"{epoch+1}/1000, Loss: {loss.item()}")
        
with torch.no_grad():
    y_pred = x * w + b

plt.plot(x, y, 'ro', label='Original data')
plt.plot(x, y_pred, label='Fitted line')
plt.legend()
plt.show()