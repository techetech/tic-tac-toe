def game(xtate,ystate):
    zero={"X" if xtate[0] else("O" if ystate[0] else 0)}
    one={"X" if xtate[1] else("O" if ystate[1] else 1)}
    two={"X" if xtate[2] else("O" if ystate[2] else 2)}
    three={"X" if xtate[3] else("O" if ystate[3] else 3)}
    four={"X" if xtate[4] else("O" if ystate[4] else 4)}
    five={"X" if xtate[5] else("O" if ystate[5] else 5)}
    six={"X" if xtate[6] else("O" if ystate[6] else 6)}
    seven={"X" if xtate[7] else("O" if ystate[7] else 7)}
    eight={"X" if xtate[8] else("O" if ystate[8] else 8)}
    print(f"{zero}|{one}|{two}")
    print(f"__|___|__")
    print(f"{three}|{four}|{five}")
    print(f"__|___|__")
    print(f"{six}|{seven}|{eight}")

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
        
        turn=1-turn

    