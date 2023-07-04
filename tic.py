def game(xtate,ystate):
    zero="X" if xtate[0] else("O" if ystate[0] else 0)
    one="X" if xtate[1] else("O" if ystate[1] else 1)
    two="X" if xtate[2] else("O" if ystate[2] else 2)
    three="X" if xtate[3] else("O" if ystate[3] else 3)
    four="X" if xtate[4] else("O" if ystate[4] else 4)
    five="X" if xtate[5] else("O" if ystate[5] else 5)
    six="X" if xtate[6] else("O" if ystate[6] else 6)
    seven="X" if xtate[7] else("O" if ystate[7] else 7)
    eight="X" if xtate[8] else("O" if ystate[8] else 8)
    print(f"{zero}|{one}|{two}")
    print(f"__|___|__")
    print(f"{three}|{four}|{five}")
    print(f"__|___|__")
    print(f"{six}|{seven}|{eight}")

def sum(a,b,c):
    return a+b+c

def checkwin(xstate,ystate):
    win=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for i in win:
        if sum(xstate[win[0]], xstate[win[1]], xstate[win[2]] )==3:
            print("X won the match")
            return 1
        if sum(ystate[win[0]], ystate[win[1]], ystate[win[2]] )==3:
            print("O won the match")
            return 0
    return -1

if __name__=="__main__":
    xstate=[0,0,0,0,0,0,0,0,0]
    ystate=[0,0,0,0,0,0,0,0,0]
    print("Welcome To Tic-Tac-Toe")
    turn=1
    while True:
        game(xstate,ystate)
        if turn==1:
            print(X's chance)
            value= int(input("in which slot you want to deploy: "))
            if value>=0 and value<=8:
                xstate[value]=1
            else:
                print("please give a valid slot number.")
            
        else:
            print(O's chance)
            value= int(input("in which slot you want to deploy: "))
            if value>=0 and value<=8:
                ystate[value]=1
            else:
                print("please give a valid slot number.")
        c=checkwin(xstate,ystate)
        if c!=-1:
            print("Match Over")
            break
        turn=1-turn

    