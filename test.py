import matplotlib.pyplot as plt
import numpy as np
from matplotlib.gridspec import GridSpec
import math

#t = 0.9
#name = '0001'
def plot(t,name):
    T = 2
    amplitude = 0.05
    y = 0.4 + amplitude*math.sin(2*math.pi*t/T)
    print(y)
    ttt = np.arange(t, t+T, 0.02)
    y1 = amplitude*np.sin(2*math.pi*ttt/T)


    # 创建空白画布
    plt.figure(figsize=(16,9),facecolor="white")

    # 修改散点图背景颜色
    #plt.rcParams["axes.facecolor"] = "#0D0434"

    # 调整子图之间的间隔
    plt.subplots_adjust(hspace=0.4,wspace=0.6)

    # 分割画布，将画布分割为小单元
    # 将画布划分为5行4列
    gs = GridSpec(9,16)

    # 添加第一个子图
    plt.subplot(gs[0:9,0:8])
    #a = Wedge((.5, .5), .5, 0, 360, width=.25, color='red')
    silicon_L = plt.Rectangle((0.05, 0.0), 0.20, 0.41, color='#BFBFBF')
    silicon_R = plt.Rectangle((0.75, 0.0), 0.20, 0.41, color='#BFBFBF')
    glass = plt.Rectangle((0.0, 0.0), 1.0, 0.15, color='#2F5597')
    permalloy = plt.Rectangle((0.425, y), 0.15, 0.01, color='#FF5050')
    su8_mid = plt.Rectangle((0.425-0.01, y-0.01), 0.15+0.02, 0.03, color='#0ED2FF')
    su8_L = plt.Rectangle((0.05, 0.41), 0.20, 0.04, color='#0ED2FF')
    sio_L = plt.Rectangle((0.05, 0.41), 0.20, 0.015, color='#B669E1')
    su8_L_0 = plt.Rectangle((0.075, 0.39), 0.025, 0.05, color='#0ED2FF')
    su8_L_1 = plt.Rectangle((0.125, 0.39), 0.025, 0.05, color='#0ED2FF')
    su8_L_2 = plt.Rectangle((0.175, 0.39), 0.025, 0.05, color='#0ED2FF')
    su8_L_3 = plt.Rectangle((0.225, 0.39), 0.025, 0.05, color='#0ED2FF')

    su8_R = plt.Rectangle((1-0.05-0.20, 0.41), 0.20, 0.04, color='#0ED2FF')
    sio_R = plt.Rectangle((1-0.05-0.20, 0.41), 0.20, 0.015, color='#B669E1')
    su8_R_0 = plt.Rectangle((1-0.075-0.025, 0.39),0.025, 0.05, color='#0ED2FF')
    su8_R_1 = plt.Rectangle((1-0.125-0.025, 0.39),0.025, 0.05, color='#0ED2FF')
    su8_R_2 = plt.Rectangle((1-0.175-0.025, 0.39),0.025, 0.05, color='#0ED2FF')
    su8_R_3 = plt.Rectangle((1-0.225-0.025, 0.39),0.025, 0.05, color='#0ED2FF')

    line_L = plt.Line2D([0.05+0.20, (1-0.15-0.02)/2], [0.44, y+0.01], lw=5,color='#0ED2FF')
    line_R = plt.Line2D([1-0.05-0.20, 1-(1-0.15-0.02)/2], [0.44, y+0.01], lw=5,color='#0ED2FF')
    #plt.annotate('light',xy=(0,0),xytext=(1,1),arrowprops=dict(arrowstyle="->",connectionstyle="arc3"))

    plt.gca().add_patch(silicon_L)
    plt.gca().add_patch(silicon_R)
    plt.gca().add_patch(glass)
    plt.gca().add_patch(su8_mid)
    plt.gca().add_patch(permalloy)
    plt.gca().add_patch(su8_L)
    plt.gca().add_patch(sio_L)
    plt.gca().add_patch(su8_L_0)
    plt.gca().add_patch(su8_L_1)
    plt.gca().add_patch(su8_L_2)
    plt.gca().add_patch(su8_L_3)
    plt.gca().add_patch(su8_R)
    plt.gca().add_patch(sio_R)
    plt.gca().add_patch(su8_R_0)
    plt.gca().add_patch(su8_R_1)
    plt.gca().add_patch(su8_R_2)
    plt.gca().add_patch(su8_R_3)
    plt.gca().add_line(line_L)
    plt.gca().add_line(line_R)
    x0=0.2
    y0=0.72
    yt=y+0.025
    xt=x0+y0-yt
    yout=0.8
    xout=xt+yout-yt
    #plt.annotate('', xy=(xt, yt), xytext=(x0, y0),
    #            xycoords='data',
    #            arrowprops=dict(facecolor='black', shrink=0.1)
    #            )
    y_ruler = yout+0.01
    plt.arrow(x0, y0, xt-x0, yt-y0,
                length_includes_head=True,# 增加的长度包含箭头部分
                head_width=0.025, head_length=0.04,width=0.005, fc='black', ec='black')
    plt.arrow(xt+0.005, yt+0.005, xout-xt-0.005, yout-yt-0.005,
                length_includes_head=True,# 增加的长度包含箭头部分
                head_width=0.025, head_length=0.04,width=0.005, fc='black', ec='black')
    #plt.gca().add_patch(plt.Rectangle((0.0,0.0),1.0,1.0), color='red')
    ruler = plt.Line2D([0,1], [y_ruler, y_ruler], lw=2,color='#000000')
    range0 = plt.Line2D([x0+y0+y_ruler-2*(0.4+amplitude+0.025),x0+y0+y_ruler-2*(0.4-amplitude+0.025)], [y_ruler, y_ruler], lw=3,color='r')
    plt.gca().add_line(ruler)
    plt.gca().add_line(range0)



    plt.plot((y_ruler-yt+xt),(y_ruler), 'o', color='r',mew=5)


    plt.axis('off')


    plt.subplot(gs[0:9,9:16])
    #plt.scatter(ttt,y1,color='r')
    #ruler = plt.Line2D([t,t], [-amplitude,amplitude], lw=1,color='#000000')
    #plt.gca().add_line(ruler)
    #
    plt.yticks([-amplitude,amplitude])
    plt.xlim(t-0.25,t+T+0.25)
    plt.ylim(-amplitude-0.01,amplitude+0.01)
    
    ax=plt.gca()  #gca:get current axis得到当前轴
    #设置图片的右边框和上边框为不显示
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    
    #挪动x，y轴的位置，也就是图片下边框和左边框的位置
    ax.spines['bottom'].set_position(('data',0))  #data表示通过值来设置x轴的位置，将x轴绑定在y=0的位置
    ax.spines['left'].set_position(('axes',0.1))  #axes表示以百分比的形式设置轴的位置，即将y轴绑定在x轴50%的位置，也就是x轴的中点
    plt.scatter(ttt,y1,color='r')
    plt.plot((t),(y1[0]), 'o', color='r',mew=10)
    plt.text(t-0.44, y1[0]-amplitude*0.05, "%.3f" % y1[0],size=20,color='r')
    top = plt.Line2D([t,t+T], [amplitude, amplitude], lw=1,color='r',linestyle="dotted")
    bot = plt.Line2D([t,t+T], [-amplitude, -amplitude], lw=1,color='r',linestyle="dotted")
    plt.gca().add_line(top)
    plt.gca().add_line(bot)
    plt.rcParams['savefig.dpi'] = 100
    plt.savefig('./img/test'+"%05d" % i+'.png')
    
i = 0
while 1:
    if i >=200:
        break
    plot(i/60,str(i))
    i = i+1
