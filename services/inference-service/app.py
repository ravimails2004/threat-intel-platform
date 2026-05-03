from fastapi import FastAPI
import torch

app = FastAPI()

# Dummy model
model = torch.nn.Linear(5, 1).cuda()

@app.post("/infer")
def infer(data: dict):
    x = torch.randn(5).cuda()
    score = model(x).item()
    return {"risk_score": float(score)}
