import sys
import numpy as np
import matplotlib.pyplot as plt
def main():
    x = np.ndarray((6,1))
    y = np.ndarray((6,1))
    x[0,0] = 1
    x[1,0] = 2
    x[2,0] = 3
    x[3,0] = 4
    x[4,0] = 5
    x[5,0] = 6
    y[0,0] = 3.2
    y[1,0] = 6.4
    y[2,0] = 10.5
    y[3,0] = 17.7
    y[4,0] = 28.1
    y[5,0] = 38.5
    A = np.ndarray((3,3))
    z = np.ndarray((3,1))
    for i in range (0,6):
        A[0,0]+= 2 * x[i,0] ** 4
        A[0,1]+= 2 * x[i,0] ** 3
        A[0,2]+= 2 * x[i,0] ** 2
        z[0,0]+= 2 * x[i,0] ** 2 * y[i,0]
    for i in range (0,6):
        A[1,0]+= 2 * x[i,0] ** 3
        A[1,1]+= 2 * x[i,0] ** 2
        A[1,2]+= 2 * x[i,0]
        z[1,0]+= 2 * x[i,0] * y[i,0]
    for i in range (0,6):
        A[2,0]+= 2 * x[i,0] ** 2
        A[2,1]+= 2 * x[i,0]
        A[2,2]+= 2
        z[2,0]+= 2 * y[i,0]
    for i in range (0,3):
        print(A[0,i])
        print(A[1,i])
        print(A[2,i])
        print(z[i,0])
    ainv = np.linalg.inv(A)

    res = np.dot(ainv,z) # a = res[0,0] and b=[1,0]
    print(res)
    # do a scatter plot of the data
    area = 10
    colors =['black']
    plt.scatter(x, y, s=area, c=colors, alpha=0.5, linewidths=8)
    plt.title('Linear Least Squares Regression')
    plt.xlabel('x')
    plt.ylabel('y')
    #plot the fitted line
    yfitted = x*x * res[0,0] + x * res[1,0] + res[2,0]
    line,=plt.plot(x, yfitted, '--', linewidth=2) #line plot
    line.set_color('red')
    plt.show()

if __name__ == "__main__":
    sys.exit(int(main() or 0))
