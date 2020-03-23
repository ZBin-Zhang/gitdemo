import random

def main():
    printIntro()
    probA,probB,n=getInputs()
    winsA,winsB=simNGames(n, probA, probB)
    printSummary(winsA,winsB)
def printIntro():
    print('这个程序模拟两个选手A和B的某种竞技比赛')
    print('程序运行需要A和B的能力值（以0到1之间的小数表示）')
def getInputs():
    a = eval(input("请输入选手A的能力值(0-1): ")) 
    b = eval(input("请输入选手B的能力值(0-1): ")) 
    n = eval(input("模拟比赛的场次: ")) 
    return a, b, n
def simNGames(n,probA,probB):
    winsA=winsB=0
    for i in range(n):
        scoreA,scoreB=simOneGames(probA,probB)
        if scoreA>scoreB:
            winsA+=1
        else:
            winsB+=1
    return winsA,winsB