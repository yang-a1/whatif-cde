import torch
import torch.nn as nn

class ODEFunc(nn.Module):
    def __init__(self, dim):
        super().__init__()
        # Updated model: added dropout for uncertainty
        self.net = nn.Sequential(
            nn.Linear(dim, 64),
            nn.Tanh(),
            nn.Dropout(0.1),
            nn.Linear(64, dim)
        )

    def forward(self, t, x):
        return self.net(x)
