'''''Momentum and Nesterov Accelerated Gradient求解
Name:Wang Junhe
Time:2022,05,17
Method:momentum
Language:python
Email:1619356172@qq.com
**********************************************'''''
import numpy as np
import copy
import os
from .Params import PARAMS
from .utility import com_gradient1, com_gradient2, com_y1, com_y2
#使用python闭包技巧，将一次学习的学习率以及维度固定;同时定义gradient以及x的初始值，并使其可以作为MG的临时变量一直存在，最后保存中间值
def MG(alpha, beta, x, gradient):
    all_x = [x]
    all_y = []
    all_gradient = [gradient]
    all_steps = []
    def update_gradient(t):
        nonlocal gradient, x, all_x, all_y, all_gradient, all_steps
        gradient = com_mg_gradient(gradient, beta, x)
        x = x - alpha*gradient
        y = com_y1(x)
        all_x.append(x.tolist())
        all_y.append(y)
        all_gradient.append(gradient.tolist())
        all_steps.append(t)
        return all_x, all_y, all_gradient, all_steps
    return update_gradient
# 计算mg梯度
def com_mg_gradient(perior_gradient, beta, x):
    # 以下两行主要算法
    now_gradient = com_gradient1(perior_gradient, x)
    res = beta*perior_gradient+(1-beta)*now_gradient
    return res
# 计算NAG梯度
def NAG(alpha, beta, x, gradient):
    all_x = [x]
    all_y = []
    all_gradient = [gradient]
    all_steps = []
    def update_gradient(t):
        nonlocal gradient, x, all_x, all_y, all_gradient, all_steps
        gradient = com_nag_gradient(gradient, alpha, beta, x)
        x = x - alpha*gradient
        y = com_y2(x)
        all_x.append(x.tolist())
        all_y.append(y)
        all_gradient.append(gradient.tolist())
        all_steps.append(t)
        return all_x, all_y, all_gradient, all_steps
    return update_gradient
# 计算nag梯度
def com_nag_gradient(perior_gradient, alpha, beta, x):
    # 以下两行主要算法
    now_gradient = com_gradient2(perior_gradient, x - alpha*beta*perior_gradient)
    res = beta*perior_gradient+now_gradient
    return res

# 训练主函数
def train(target):
    # 定义初始参数
    dimension = PARAMS(target)['dimension']
    alpha = PARAMS(target)['alpha']
    beta = PARAMS(target)['beta']
    init_gradient = np.array([0.0]*dimension,dtype=float).reshape(dimension,1)
    init_x = PARAMS(target)['init_x'].reshape(dimension,1)
    # 构建模型
    model = MG(alpha, beta, init_x, init_gradient) if PARAMS(target)['MG'] else NAG(alpha, beta, init_x, init_gradient)
    # 开始训练
    steps = PARAMS(target)['steps']
    for i in range(steps):
        model(i)
    # 再执行一步得到对应结果
    x, y, g, t = model(steps)
    tg = copy.deepcopy(t)
    tg.append(steps+1)
    return [np.array(x).reshape(steps+2,dimension),
           np.array(y,dtype=object).reshape(steps+1,1),
           np.array(g).reshape(steps+2,dimension),
           np.array(t,dtype=object).reshape(steps+1,1),
           np.array(tg,dtype=object).reshape(steps+2,1)]
