import sys

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

def F():
    global i,lex,ps

    if((i < len(lex)) and (lex[i][1].isdigit())):
        ps += [lex[i][1]]
        i = i + 1
    elif((i < len(lex)) and (lex[i][0] == 'PO')):
        i = i +1
        E()
        
        if((i < len(lex)) and (lex[i][0] != 'PF')):
            print("erreur syntaxe")
            exit()
        
        else:
            i+= 1
        
    elif((i < len(lex)) and (lex[i][1] == '-')):
        i = i + 1
        F()
        ps += ['~']
    else:
        print("erreur synstaxe")
        exit()

def T1():
    global i,lex,ps
    if((i < len(lex)) and (lex[i][1]=='*')):
        i+=1 #reconnu le *
        F()
        ps += ['*']
        T1()
    elif((i < len(lex)) and (lex[i][1]=='/')):
        i+=1 #reconnu le *
        F()
        ps += ['/']
        T1()

    else:
        pass #production epsilon

def T():
    F()
    T1()
    



def E1():
    global i,lex,ps
    if((i < len(lex)) and (lex[i][1]=='+')):
        i+=1 #reconnu le +
        T()
        ps += ['+']
        E1()
    elif((i < len(lex)) and (lex[i][1]=='-')):
        i+=1 #reconnu le -
        T()
        ps += ['-']
        E1()

def E():
    T()
    E1()


def codeRam():
    i = 0
    sommet = 1
    print("LOAD #0;")
    print("STORE 1;")
    while i < len(ps):
        if ps[i].isdigit():
           
            print("LOAD #"+ps[i]+';')
            print("STORE "+str(sommet)+';')
            sommet += 1
            
            
            
            
        

        elif ps[i] == '*':
            
            print("LOAD "+str(sommet-2)+';')
            
            print("MUL "+str(sommet-1)+';')
            print("STORE "+str(sommet-2)+';')
            sommet -= 1
        
                
        elif ps[i] == '/':
        
            print("LOAD "+str(sommet-2)+';')
            print("DIV "+str(sommet-1)+';')
            print("STORE "+str(sommet-2)+';')
            sommet -= 1
            
            
            

        elif ps[i] == '+':
            
            print("LOAD "+str(sommet-2)+';')
            print("ADD "+str(sommet-1)+';')
            print("STORE "+str(sommet-2)+';')
            sommet -= 1

            
            
            
            
            
        elif ps[i] == '-':
            
            print("LOAD "+str(sommet-2)+';')
            print("SUB "+str(sommet-1)+';')
            print("STORE "+str(sommet-2)+';')
            sommet -= 1
           
            
        
        elif ps[i] == '~':
            print("LOAD "+str(sommet-1)+';')
            print("MUL #-1"+';')
            print("STORE "+str(sommet-1)+';')
            
            
            
        
        i += 1
    print("LOAD 0;")
    print("WRITE;")
    print("STOP;")
    #return res

if __name__=="__main__":
    ch=(sys.argv[1])
    i = 0
    lex = lexer(ch)
    #print(lex)
    ps = []
    
    E()
    #print(ps)
    (codeRam())
