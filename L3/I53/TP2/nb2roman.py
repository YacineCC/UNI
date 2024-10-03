import sys

def traduct(i, un, cinq, dix):
    if 1 <= int(i) <= 3:
        print(int(i) * un,end='')
    elif int(i) == 4:
        print(un + cinq,end='')
    elif 5 <= int(i) <= 8:
        print(cinq + (int(i) - 5) * un,end='')
    elif int(i) == 9:
        print(un + dix,end='')
def N():
    global i
    if len(ch) >= 2:
        D()
        i += 1
    traduct(ch[i], "I", "V", "X")

def D():
    global i
    if len(ch) >= 3:
        C()
        i += 1
    traduct(ch[i], "X", "L", "C")


def C():
    global i
    if len(ch) >= 4:
        M()
        i += 1
    traduct(ch[i], "C", "D", "M")


def M():
    global i
    print(int(ch[i]) * "M",end='')

"""

def traduct():
    if 1 <= int(ch[i]) <= 3:
        print('I' * int(ch[i]),end='')
    elif int(ch[i]) == 4:
        print("IV",end='')
    elif 5 <= int(ch[i]) <= 8:
        print('V'+(int(ch[i])-5)*'I')
    elif int(ch[i]) == 9:
        print("IX",end='')
    else:
        print("erreur")
        exit()

def N():
    global i
    if len(ch) >= 2:
        D()
        i+=1
    traduct()
def D():
    global i
    if len(ch) >= 3:
        C()
        i += 1
    traduct()
def C():
    global i
    if len(ch) >= 4:
        M()
        i += 1
    traduct()
def M():
    global i
    print(int(ch[i]) * 'M',end='')
"""



if __name__ == "__main__":
    ch=(sys.argv[1])
    i=0
    N()
    print()
