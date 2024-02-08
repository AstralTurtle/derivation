from matplotlib import pyplot as plt
import numpy as np
import uuid

def makeImages(toPlot, uuid):
    plot_id = uuid
    x = np.array(range(-10, 11))
    # plot the function
    plt.grid()
    plt.plot(x,toPlot(x))
    plt.savefig(f'plots/{plot_id}.png')
    # clear
    plt.clf()
    # plot the derivative
    plt.grid()
    prime = toPlot.deriv()
    plt.plot(x,prime(x))    
    plt.savefig(f'plots/{plot_id}_prime.png')
    # clear
    plt.clf()
    # plot double prime
    plt.grid()
    double_prime = prime.deriv()
    plt.plot(x,double_prime(x))
    plt.savefig(f'plots/{plot_id}_double_prime.png')
    print(f'Plots saved as {plot_id}.png, {plot_id}_prime.png, and {plot_id}_double_prime.png')
    return[f'plots/{plot_id}.png', f'plots/{plot_id}_prime.png', f'plots/{plot_id}_double_prime.png']

    


if __name__ == '__main__':
    # generate a uuid for the plot
    plot_id = uuid.uuid4()
    # plot the function
    # test is x^2 
    test = np.poly1d([1, 1, 0])
    x = np.array(range(-10, 11))
    prime = test.deriv()
    # plot the function
    plt.plot(x,test(x))
    plt.savefig(f'plots/{plot_id}.png')
    # clear 
    plt.clf()
    # plot the derivative
    plt.plot(x,prime(x))
    plt.savefig(f'plots/{plot_id}_prime.png')
    # clear
    plt.clf()
    # plot double prime
    double_prime = prime.deriv()
    plt.plot(x,double_prime(x))
    plt.savefig(f'plots/{plot_id}_double_prime.png')


    
    # print(f'Plots saved as {plot_id}.png, {plot_id}_prime.png, and {plot_id}_double_prime.png')


    