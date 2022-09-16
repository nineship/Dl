import torch
from torch.utils.data import Dataset
from torch.utils.data import DataLoader
import torch.nn as nn
from torch.nn.parameter import Parameter
import torch.nn.functional as F
import torch.optim as optim
import matplotlib.pyplot as plt
import random
import numpy as np
import math

def hook(module, input, output):
    features.append(input)
    return None

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.fc1 = nn.Linear(2, 2) 
        self.fc2 = nn.Linear(2, 2)


        #初始化权重
        w1 = torch.tensor([[0.15,0.2],[0.25,0.3]])
        b1 = torch.tensor([0.35,0.35])
        self.fc1.weight = Parameter(w1)
        self.fc1.bias = Parameter(b1)

        w2 = torch.tensor([[0.40,0.45],[0.50,0.55]])
        b2 = torch.tensor([0.6,0.6])
        self.fc2.weight = Parameter(w2)
        self.fc2.bias = Parameter(b2)
    def forward(self, x):
        x = torch.sigmoid(self.fc1(x))
        x = torch.sigmoid(self.fc2(x))
        return x
def train():
    net = Net()
    learningRate=0.5
    optimizer = torch.optim.SGD(net.parameters(), learningRate)
    loss_func = torch.nn.MSELoss()
    y_ = []
    y_test = []
    for name in net.state_dict():
            print(name)
            print(net.state_dict()[name])
    for k in range(1):
        print("----------------------)")
        inputs = torch.tensor([0.05,0.1])
        label = torch.tensor([0.01,0.99])
        prediction = net(inputs)
        print("结果",prediction)
        loss = loss_func(prediction, label)
        print("loss",loss)
        
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        for name in net.state_dict():
            print(name)
            print(net.state_dict()[name])
        
    return
def sigmoid(x):
    return 1/(1+math.exp(-x))
def cal():
    return 0
if __name__ == "__main__":
    train()
