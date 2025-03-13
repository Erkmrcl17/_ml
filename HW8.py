import torch

x = torch.tensor(0.0, requires_grad=True)
y = torch.tensor(0.0, requires_grad=True)
z = torch.tensor(0.0, requires_grad=True)

lr= 0.01

def loss_function(x, y, z):
    return (x - 1) ** 2 + (y - 2) ** 2 + (z - 3) ** 2  

for _ in range(10000):
    loss = loss_function(x, y, z)  
    loss.backward()  

    with torch.no_grad():
        x -= lr * x.grad
        y -= lr * y.grad
        z -= lr * z.grad
        x.grad.zero_()
        y.grad.zero_()
        z.grad.zero_()

print(f"x = {x.item():.4f}, y = {y.item():.4f}, z = {z.item():.4f}")