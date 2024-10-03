import dis
import time

def hello():
        print('Hello World!')

def testif1(a):
 
        if(a == 0):
                print("zaza")
        elif(a > 0):
                print("zozo")
        else:
                print("bonjour")

def testif2(a):
 
        if(a == 0):
                print("zaza")
        else:
                if(a > 0):
                    print("zozo")
                else:
                    print("bonjour")

def testfor():
        a = 0
        for i in range(10):
                a = a+i
        return a

def testwhile():
        a = 0
        i = 0
        while(i < 10):
                a = a + i
                i += 1
        return a

def testliste(n):

        Liste = []
        for i in range(n):
                Liste += [i]
        return Liste

def testappend():

        Liste = []
        for i in range(n):
                Liste.append(i)
        return Liste

def testcompr():

        Liste = [x for x in range(n)]
        return Liste
