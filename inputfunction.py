import matplotlib.pyplot as plt
import numpy as np
import sympy as sym
import frechetcalcu

# this class is the main class
# use for input P,Q by user
# use frechetcalcu to calculate the distance

# function draw
# can use for all P matrix
# do not forget to use plt.show() after using this function!
def functionDraw(P,color): # P matrix size 2 x n #color = tab:green
    n = len(P)
        for i in range(1,n):
            plt.plot([P[i-1][0],P[i][0]],[P[i-1][1],P[i][1]],c=color)



if __name__ == '__main__':
# example 1:
    P =
[[12.8289,228.248],[24.0543,253.104],[46.8761,257.56],[46.3385,242.50
8],[85.4033,257.023],[97.2302,254.693],[95.6174,215.27],[104.502,233.
594],[105.571,215.419]]

    Q =
[[47.2345,215.27],[48,240],[89.8827,249.659],[67.6065,215.331],[84.96
82,200.029],[102.413,190.692],[176.614,216.736],[112.902,213.953]]
# example 1:
    #P = [[0,0],[1,1],[2,2],[3,3]]
    #Q = [[0,0.25],[1,1.25],[2,2.25],[3,3.25]]
    functionDraw(P,'tab:blue')
    functionDraw(Q,'tab:red')
    # frechet diatance for 2 curves
    frec_P_Q = frechetcalcu.frechetDist(P,Q) # frec[0] is the leash length frec[1] is the distance matrix

    plt.title(frec_P_Q[0])
    plt.suptitle('frechet distance between P&Q=')
    plt.show()

P =
[[12.8289,228.248],[24.0543,253.104],[46.8761,257.56],[46.3385,242.508],[85.4033,257.0
23],[97.2302,254.693],[95.6174,215.27],[104.502,233.594],[105.571,215.419]]
Q =
[[47.2345,215.27],[48,240],[89.8827,249.659],[67.6065,215.331],[84.9682,200.029],[102.
413,190.692],[176.614,216.736],[112.902,213.953]]
R =
[[27.25,300.27],[41,320],[60.8827,352.65],[40.6,300.3],[60,300.02],[89.4,370],[101.1,3
04.7],[107.9,342.953]]
#P = [[0,0],[1,1],[2,2],[3,3]]
#Q = [[0,0.25],[1,1.25],[2,2.25],[3,3.25]]
#R = [[0,0.5],[1,1.5],[2,2.5],[3,3.5]]
#example 1/2:
functionDraw(P,'tab:blue')
functionDraw(Q,'tab:red')
functionDraw(R,'tab:green')
# frechet diatance for 3 curves
plt.title(frechetcalcu.multiple_frechetDist_new([P,Q,R])[0])
plt.suptitle('frechet distance between P&Q&R=')
print(frechetcalcu.multiple_frechetDist_new([P,Q,R])[0])
print(frechetcalcu.multiple_frechetDist(P,Q,R)[0])
plt.figure()
#example 3:
functionDraw(P,'tab:blue')
functionDraw(Q,'tab:red')
functionDraw(R,'tab:green')
functionDraw(T,'tab:brown')
# frechet diatance for 4 curves
plt.title(frechetcalcu.multiple_frechetDist_new([P,Q,R,T])[0])
plt.suptitle('frechet distance between P&Q&R&T=')
plt.show(