import itertools
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
def plot_dynamic(x,y,name):
    fig = plt.figure()
    plt.ylim(-10000,250000)
    plt.xlim(-100,200)
    xx = []
    yy = []
    def data_gen():
        for i in range(len(x)):
            data_x = x[i]
            data_y = y[i]
            yield [data_x, data_y]
    def updata(a):
        xx.append(a[0])
        yy.append(a[1])
        plt.plot(xx,yy)
    ani = animation.FuncAnimation(fig, updata, frames=data_gen,interval=10,repeat=False,blit=False)
    ani.save(name, writer='pillow')