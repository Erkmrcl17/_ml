import torch
import torch.nn as nn
import torch.optim as optim

# Dataset
inputs = torch.tensor([
    [1,1,1,1,1,1,0],
    [0,1,1,0,0,0,0],
    [1,1,0,1,1,0,1],
    [1,1,1,1,0,0,1],
    [0,1,1,0,0,1,1],
    [1,0,1,1,0,1,1],
    [1,0,1,1,1,1,1],
    [1,1,1,0,0,0,0],
    [1,1,1,1,1,1,1],
    [1,1,1,1,0,1,1],
], dtype=torch.float32)

targets = torch.tensor([
    [0,0,0,0],
    [0,0,0,1],
    [0,0,1,0],
    [0,0,1,1],
    [0,1,0,0],
    [0,1,0,1],
    [0,1,1,0],
    [0,1,1,1],
    [1,0,0,0],
    [1,0,0,1],
], dtype=torch.float32)

class BinaryMLP(nn.Module):
    def __init__(self):
        super().__init__()
        self.model = nn.Sequential(
            nn.Linear(7, 32),
            nn.ReLU(),
            nn.Linear(32, 16),
            nn.ReLU(),
            nn.Linear(16, 4)  
        )

    def forward(self, x):
        return self.model(x)

model = BinaryMLP()
criterion = nn.BCEWithLogitsLoss()
optimizer = optim.Adam(model.parameters(), lr=0.01)

def accuracy(preds, targets):
    predicted = (torch.sigmoid(preds) > 0.5).float()
    correct = (predicted == targets).float().mean()
    return correct.item()

for epoch in range(1000):
    model.train()
    outputs = model(inputs)
    loss = criterion(outputs, targets)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    if epoch % 100 == 0:
        acc = accuracy(outputs, targets)
        print(f"Epoch {epoch} | Loss: {loss.item():.4f} | Accuracy: {acc:.2f}")
        
model.eval()
with torch.no_grad():
    test_outputs = torch.sigmoid(model(inputs)).round()
    for i, pred in enumerate(test_outputs):
        binary = ''.join(str(int(bit)) for bit in pred)
        print(f"{inputs[i].int().tolist()} => {binary}")
