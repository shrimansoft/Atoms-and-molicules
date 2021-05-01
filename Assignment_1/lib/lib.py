import numpy as np 
from numpy import linalg as LA
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def eigenValues(n,eEven,eOdd,B):
    H = np.eye(n,n)
    for i in range(n):
        for j in range (n):
            if abs(i-j)==1:
                H[i][j] = B
            if i==j:
                if i%2:
                    H[i][j] = eEven
                else:
                    H[i][j] = eOdd

    
    w, _ = LA.eig(H)
    return w


def eigenValues2(n,eEven,eOdd,B):
    H = np.eye(n,n)
    for i in range(n):
        for j in range (n):
            
            if abs(i-j)==1 or abs(i-j)==n-1:
                H[i][j] = B
            if i==j:
                if i%2:
                    H[i][j] = eEven
                else:
                    H[i][j] = eOdd

    
    w, _ = LA.eig(H)
    return w


def prepare_animation(bar_container,HIST_BINS,dataFunction):

    def animate(frame_number):
        # simulate new data coming in
        # data = eigenValues(frame_number*10+50,2,1)
        data = dataFunction(frame_number)
        n, _ = np.histogram(data, HIST_BINS)
        for count, rect in zip(n, bar_container.patches):
            rect.set_height(count)
        return bar_container.patches
    return animate


def myPlot(yLimit,left,right,sepration,dataFunction):
    fig, ax = plt.subplots()

    HIST_BINS = np.linspace(left,right, sepration)
    data = eigenValues(1,2,2,1)
    _, _, bar_container = ax.hist(data, HIST_BINS, lw=1, ec="red", fc="red", alpha=0.25)
    ax.set_ylim(top=yLimit) 
    ani = animation.FuncAnimation(
        fig,
        prepare_animation(bar_container,HIST_BINS,dataFunction),
        50,
        repeat=False,
        blit=True,
        )
    ax.set_xlabel('Eigenvalue')
    ax.set_ylabel('Density')
    ax.set_title(r'Density of eigenstates, increasing n')

    plt.show()
