
import sys
import numpy as np
import matplotlib.pyplot as plt
def main():
    n=10000
    E = np.ndarray((n,1))
    w1 = 0.1
    w2 = 0.1
    b = 0.4
    x1 = 0
    x2 = 0
    for i in range (0, n):
        for j in range (1,5):
           x1 = j
           r = 0.3 * x1 + 2
           s = 0.1
           for k in range (0 , 2):
               x2 = r - s
               newW1 = newWeight1(x1, x2, w1, w2, b)
               newW2 = newWeight2(x1, x2, w1, w2, b)
               newb = newBias(x1, x2, w1, w2, b)
               w1 = newW1
               w2 = newW2
               b = newb
               s = s * -1
        E[i,0] = FindError(x1,x2,w1,w2,b)
    print("w1 = " + str(w1) + "\n w2 = " + str(w2) + "\n b =" + str(b))
    res1 = w1* 1.5 + w2 * 2.4 + b
    res2 = w1* 1.5 + w2 * 2.5 + b
    res3 = w1* 2.5 + w2 * 2.7 + b
    res4 = w1* 2.5 + w2 * 2.8 + b
    print("Testing results:  \n" + " (1.5 , 2.4) ---> y =  " + str(res1) + "\n (1.5 , 2.5) ---> y =  " + str(res2) + "\n (2.5 , 2.7) ---> y =  " + str(res3) + "\n (2.5 , 2.8) ---> y =  " + str(res4))
    DrawErrorFunc(E, n)
    #testing the results:
    while True:
       Task= input("If you want to test data type T, if you want to quit type Q")
       if Task == "T":
          TestX = input("Enter a test point: \n X: " )
          TestY = input("Enter a test point: \n Y: " )
          res = w1* float(TestX) +w2 * float(TestY) + b
          if res < 0.5:
              result = 0
          elif res > 0.5:
              result =1
          print("Result is " +str(result))
       elif Task == "Q":
           break
def newWeight1(x1, x2, w1, w2, b):
    y = 0
    a = w1 * x1 + w2 * x2 + b
    q = 0.3 * x1 + 2
    if x2 == q - 0.1:
        y = 0
    if x2 == q + 0.1:
        y = 1
    gradw1 = -1 * (y - a) * x1
    w1 = w1 - 0.05 * gradw1
    return w1

def newWeight2(x1, x2, w1, w2, b):
    y = 0
    a = w1 * x1 + w2 * x2 + b
    q = 0.3 * x1 + 2
    if x2 == q - 0.1:
        y = 0
    if x2 == q + 0.1:
        y = 1
    gradw2 = -1 * (y - a) * x2
    w2 = w2 - 0.05 * gradw2
    return w2

def newBias(x1, x2, w1, w2, b):
    y = 0
    a = w1 * x1 + w2 * x2 + b
    q = 0.3 * x1 + 2
    if x2 == q - 0.1:
        y = 0
    if x2 == q + 0.1:
        y = 1
    gradwb = -1 * (y - a) * 1
    b = b - 0.05 * gradwb
    return b

def FindError(x1, x2, w1, w2, b):
    y = 0
    a = w1 * x1 + w2 * x2 + b
    q = 0.3 * x1 + 2
    if x2 == q - 0.1:
        y = 0
    if x2 == q + 0.1:
        y = 1
    Err = 0.5 * (y - a) * (y - a)
    return Err

def DrawErrorFunc(E, n):
     x=np.ndarray((n,1))
     y=np.ndarray((n,1))
     for m in range (0 , n):
         x[m, 0] = m
     area = 10
     colors =['black']
     plt.scatter(x, y, s=area, c=colors, alpha=0.5, linewidths=2)
     plt.title('Error Function')
     plt.xlabel('epoch')
     plt.ylabel('Error')
     #plot the fitted line
     plt.plot(x, E, '--', linewidth=3) #line plot
     #line.set_color('red')
     plt.show()
if __name__ == "__main__":
    sys.exit(int(main() or 0))


