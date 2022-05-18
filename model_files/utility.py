# 计算第一题梯度
def com_gradient1(gradient, x):
    res = gradient
    for i in range(len(x)):
        if i == 0:
            res[i] = -2*(1-x[i])+200*(x[i+1]-pow(x[i],2))*(-2)*x[i]
        elif i == len(x)-1:
            res[i] = 200*(x[i]-pow(x[i-1],2))
        else:
            res[i] = -2*(1-x[i])+200*(x[i+1]-pow(x[i],2))*(-2)*x[i]+200*(x[i]-pow(x[i-1],2))
    return res
# 计算第一题y
def com_y1(x):
    res = 0
    # 由于函数下标为1，因此N最小为2，即不需要考虑len(x)-1等于0的情况
    for i in range(len(x)-1):
        res += pow((1-x[i]),2)[0]+100*pow((x[i+1]-pow(x[i],2)),2)[0]
    return res
# 计算第二题梯度
def com_gradient2(gradient, x):
    res = gradient
    res[0] = 0.2*x[0]
    res[1] = 4*x[1]
    return res
# 计算第二题y
def com_y2(x):
    res = 0.1*pow(x[0],2)+2*pow(x[1],2)
    return res