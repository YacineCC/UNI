import sys

def decoupemot():
    l = []
    lettre = 0
    while(lettre < len(ch)):
        mot = ""
        while(ch[lettre] != ' '):
            mot += ch[lettre]
            lettre += 1
        L += [mot]
    return L

def lexer(ch):
    lul = []
    types = ["int","char","float"]
    OP = ['+','-','*','/']
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
        #elif ch[i] == '*':
        #    lul.append(("PTR",'*'))
        #    i += 1
        elif ch[i] in OP:
            lul.append(("OP",ch[i]))
            i += 1
        
        elif ch[i].isdigit():
            nb=""
            j = i
            while j < len(ch) and ch[j].isdigit():
                nb += ch[j]
                j += 1
            lul.append(("NB",nb))
            i = j
            #i += 1
        else:
            mot = ""
            j = i
            while j < len(ch) and ch[j] != ' ':
                mot += ch[j]
                j += 1
            if mot in types:
                lul.append(("TYPE",mot))
            elif mot != "":
                lul.append(("ID",mot))
            i = j
            i += 1
    return lul

if __name__=="__main__":
    ch = sys.argv[1]
    i = 0
    print(lexer(ch))
