import sys

def F():
    global i,ch

    #if((i <= len(ch) and ch[i] in list(range(10)))):
    #    print(ch[i])
    if((i < len(ch)) and (ch[i].isdigit())):
        print(ch[i],end='')
        i = i+1
    elif((i < len(ch)) and (ch[i] == '(')):
        i = i +1
        E()
        if((i < len(ch)) and (ch[i] != ')')):
            print("erreur syntaxe")
            exit()
        else:
            i+= 1
    elif((i < len(ch)) and (ch[i] == '-')):
        i = i + 1
        E()
        print('~',end="")
    else:
        print("erreur synstaxe")
        exit()

def T1():
    global i,ch
    if((i < len(ch)) and (ch[i]=='*')):
        i+=1 #reconnu le *
        F()
        print('*',end='')
        T1()
    elif((i < len(ch)) and (ch[i]=='/')):
        i+=1 #reconnu le *
        F()
        print('/',end='')
        T1()

    else:
        pass #production epsilon

def T():
    F()
    T1()
    



def E1():
    global i,ch
    if((i < len(ch)) and (ch[i]=='+')):
        i+=1 #reconnu le +
        T()
        print('+',end='')
        E1()
    elif((i < len(ch)) and (ch[i]=='-')):
        i+=1 #reconnu le +
        T()
        print('-',end='')
        E1()

def E():
    T()
    E1()


if __name__=="__main__":
    ch=(sys.argv[1])
    i = 0
    E()
    if(i != len(ch)):
        print()
        print("erreur")
    else:
        print()
        print("succes")

