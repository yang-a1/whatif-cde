import torch
from torchdiffeq import odeint
from models.ode_model import ODEFunc

def main():
    x0 = torch.tensor([[1.0, 0.0]])
    t = torch.linspace(0, 25, 100)
    ode_func = ODEFunc(dim=2)

    out = odeint(ode_func, x0, t)
    print("ODE output shape:", out.shape)

if __name__ == "__main__":
    main()
