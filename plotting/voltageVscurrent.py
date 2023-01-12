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
    plt.figure(ifig)
    plt.plot(x,y,color=col)
    plt.yticks(fontsize=12)
    plt.xticks(np.linspace(min(x),max(x),5),fontsize=12)
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

    makePlot(C,V,"cornflowerblue","Current monitor (A)","Voltage monitor (V)",1)
    plt.figure(1)
    plt.axhline(y=0,linestyle='--',color='black')
    plt.axvline(x=0,linestyle='--',color='black')
    plt.savefig(str(filename.strip().split("/")[-1].split("_")[0])+".pdf",bbox_inches='tight')
    #plt.savefig('standard_degauss_z.pdf',bbox_inches='tight')
    #plt.savefig('xsyczc_degauss.pdf',bbox_inches='tight')
    #makePlot(Ind,C,"cornflowerblue","Step index (a.u.)","Current monitor (A)",2)



    plt.show()


if __name__ == "__main__":
    main()
