'''''**********task.jpg任务求解***************
Name:Wang Junhe
Time:2022,05,17
Method:momentum
Language:python
Email:1619356172@qq.com
**********************************************'''''
from plot_fun_files.plot_static import plot_static
from plot_fun_files.plot_dynamic import plot_dynamic
from plot_fun_files.plot_contour import plot_contour
from model_files.program import train
def P1_1():
    x,_,_,_,_ = train(1)
    plot_contour(data_x=x[:,0],data_y=x[:,1],name='data_files/P1_1_x')
def P1_2_1():
    x,y,g,t,tg = train(2)
    plot_static(t, y, 1, 'data_files/P1_2_y')
    plot_static(tg, g, 7, 'data_files/P1_2_g')
    print(x[-1])
def P1_2_2():
    x,y,g,t,tg = train(2)
    plot_dynamic(t,y,'data_files/P1_2_y.gif')
def P2():
    for i in range(5):
        x,y,g,t,tg = train(3+i)
        plot_contour(data_x=x[:,0],data_y=x[:,1],name=f'data_files/P2_x_{i}')
if __name__=='__main__':
    P1_1()
    P1_2_1()
    P1_2_2()
    P2()