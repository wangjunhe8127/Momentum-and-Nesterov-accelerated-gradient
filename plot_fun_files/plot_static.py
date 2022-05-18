import matplotlib.pyplot as plt
def plot_static(x,y,num,name):
    for i in range(num):
        plt.plot(x,y[:,i])
    plt.savefig(name)
    plt.show()
    plt.close()