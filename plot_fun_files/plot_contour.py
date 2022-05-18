# 第一个任务：n=2时最优解 x1 = 1, x2 = 1
# 第二个任务：最优解x1 = 0, x2 =0
import numpy as np
import matplotlib.pyplot as plt
# 绘制等高线和变化曲线
def plot_contour(data_x,data_y,name,center_x=0,center_y=0):
    x = np.arange(-6, 3, 0.01)
    y = np.arange(-3, 9, 0.01)
    X, Y = np.meshgrid(x, y)
    Z = (X-center_x)**2 + (Y-center_y)**2
    plt.contour(X, Y, Z, 10)
    plt.plot(data_x,data_y)
    plt.savefig(name)
    plt.show()
    plt.close()