import sys

def lexer(ch):
    lul = []
    types = ["int","char","float"]
    i = 0
    while i < len(ch):
        if ch[i] == '(':
            lul.append(("PO",'('))
            i += 1
        elif ch[i] == ')':
            lul.append(("PF",')'))
            i += 1

        elif ch[i] == '[':
            lul.append(("CO",'['))
            i += 1

        elif ch[i] == ']':
            lul.append(("CF",']'))
            i += 1
        elif ch[i] == '*':
            lul.append(("PTR",'*'))
            i += 1
        elif ch[i].isdigit():
            nb=""
            j = i
            while j < len(ch) and ch[j].isdigit():
                nb += ch[j]
                j += 1
            lul.append(("NB",nb))
            i = j
        elif ch[i] == ' ':
            i += 1
        else:
            mot = ""
            j = i
            while j < len(ch) and ch[j] not in ['*','[','(',' ']:
                mot += ch[j]
                j += 1
            if mot in types:
                lul.append(("TYPE",mot))
            elif mot != "":
                lul.append(("ID",mot))
            i = j
        
    return lul

def Declaration():
    t = Type()
    Decla()
    print(t)

def Type():
    global i
    if i < len(lul) and lul[i][0] == "TYPE":
        t = lul[i][1]
        i += 1
        return t
    else:
        print("erreur")

def Pointeur():
    global i
    if i < len(lul) and lul[i][0] == "PTR":
        i += 1
        print("Pointeur sur ",end='')
        return Pointeur() + 1
    else:
        return 0

def Decla():
    Dabs()
    Pointeur()
    #print("de",lul[i][1],"pointeurs sur ",end='')

def Dabs():
    Final()
    print("est un tableau de ",end='')
    Tableau()

def Tableau():
    global i
    if ch[i] == '[':
        nb = ""
        j = i
        j += 1
        while ch[j] != ']':
            nb += ch[j]
            print(nb)
            j += 1
        
        i = j
        print(nb,end=" ")
        Tableau()
    else:
        pass



def Final():

    global i,decal
    if i < len(ch) and ch[i]=='(':
        i = i+1
        Decla()
        if i < len(ch) and ch[i] != ')':
            print("erreur syntax")
            exit()
    elif lul[i][0] == "ID":
        print(lul[i][1],end=' ')

if __name__=="__main__":
    ch = sys.argv[1]
    lul = lexer(ch)
    i = 0
    print(ch)
    print(lul)
    Declaration()

