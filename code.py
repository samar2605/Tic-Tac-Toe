print("Welcome to Tic-Tac-Toe!")
flag=0
a=[' ',' ',' ',' ',' ',' ',' ',' ',' ']
pos=[True,True,True,True,True,True,True,True,True]
def print_line(a):
    for i in range(0,9,3):
         print(a[i],"|",a[i+1],"|",a[i+2])
         if(i<6):
            print("----------")

print_line(a)

def ask_user():
    print("choose the position from below")
    k=1
    for i in range(1,4):
        for j in range(1,4):
            print(k,":",i,j)
            k+=1
    num=int(input("Enter choice no:"))
    if pos[num-1]==True:
        del a[num-1:num]
        if counter%2==0:
            a.insert(num-1,0)
            print("Turn for first player")
        else:
            a.insert(num-1,1)
            print("Turn for second player")
        print_line(a)
        pos[num-1]=False
    else:
        print("Space already filled!")
        print("Repeat!")
        ask_user()    


def check(a):
    if a[0]==1:
        if a[1]==1 and a[2]==1:
            print("Player one won the game")
            return 1
        if a[3]==1 and a[6]==1:
            print("Player one won the game")
            return 1
        if a[4]==1 and a[8]==1:
            print("Player one won the game")
            return 1
    if a[0]==0:
        if a[1]==0 and a[2]==0:
            print("Player two won the game")
            return 1
        if a[3]==0 and a[6]==0:
            print("Player two won the game")
            return 1
        if a[4]==0 and a[8]==0:
            print("Player two won the game")
            return 1
    if a[1]==1:
        if a[4]==1 and a[7]==1:
            print("Player one won the game")
            return 1
    if a[1]==0:
        if a[4]==0 and a[7]==0:
            print("Player two won the game")
            return 1
    if a[2]==1:
        if a[5]==1 and a[8]==1:
            print("Player one won the game")
            return 1
        if a[4]==1 and a[6]==1:
            print("Player one won the game")
            return 1
    if a[2]==0:
        if a[5]==0 and a[8]==0:
            print("Player two won the game")
            return 1
        if a[4]==0 and a[6]==0:
            print("Player two won the game")
            return 1
    if a[3]==1:
        if a[4]==1 and a[5]==1:
            print("Player one won the game")
            return 1
    if a[3]==0:
        if a[4]==0 and a[5]==0:
            print("Player two won the game")
            return 1
    else:
        return 0

counter=1
while counter<10:
    ask_user()
    flag=check(a)
    if flag==1:
        break
    counter+=1
