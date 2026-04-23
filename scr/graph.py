import matplotlib.pyplot as plt 

def graph(x, y, name):
    plt.plot(x, y) 
    plt.xlabel('Time, ms')
    plt.ylabel(name)
    plt.show()