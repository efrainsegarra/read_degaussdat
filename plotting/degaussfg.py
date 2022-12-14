import numpy as np
import matplotlib.pyplot as plt
import sys

def readParsedFile(filename):
    V = []
    C = []
    Ind = []
    read = False
    with open(filename,"r") as f:
        for line in f:
            parse = line.strip().split()
            ind = int(parse[0])
            v = float(parse[1])
            c = float(parse[2])
            #if not read and v > -0.0029 and v < -0.0021:
            #    continue
            #if v < -0.0029 or v > -0.0021:
            #    read = True
            #if read:
            V.append(v)
            C.append(c)
            Ind.append(ind)
    return V,C,Ind

def makePlot(x,y,col,xlab,ylab,ifig):
    x = np.asarray(x)
    #x = np.asarray(x)/20/5 - 1000 + 5
    plt.figure(ifig)
    plt.plot(x,y,color=col)
    plt.yticks(fontsize=12)
    #plt.xlim([0,90])
    #plt.xticks(np.linspace(min(x),max(x),5),fontsize=12)
    plt.xlabel(xlab,fontsize=15)
    plt.ylabel(ylab,fontsize=15)
    plt.tight_layout()

def main():

    if len(sys.argv) != 2:
        print("Incorrect number of arguments. Please instead use:")
        print("\tpython3 code.py [parsed degauss file]")
        exit()

    filename = sys.argv[1]
    V,C,Ind = readParsedFile(filename)

    '''AVG_V = []
    AVG_Inds = []
    i = 0
    j = 0
    aver = 1
    while i < len(V)-aver:
        avg_v = np.average(V[i:i+aver])
        AVG_V.append(avg_v)
        AVG_Inds.append(j)
        i = i+aver
        j = j+1'''

    makePlot(Ind,V,"cornflowerblue",r"$t$ (s)","Voltage monitor (V)",1)
    makePlot(Ind,C,"cornflowerblue",r"$t$ (s)","Current monitor (A)",2)

    plt.figure(1)
    plt.savefig('voltage_test.pdf',bbox_inches='tight')

    plt.figure(2)
    plt.savefig('current_test.pdf',bbox_inches='tight')


    #plt.figure(2)
    #plt.xlim([5,20])
    #plt.ylim([-0.4,0.4])
    #plt.savefig('current_zoomed.pdf',bbox_inches='tight')

    plt.show()


if __name__ == "__main__":
    main()
