import tkinter as tk
from random import randrange
from bbr import bbr

PAUSE = 1000
COTE = 50
NBC = 15
HA, LA = COTE+1, (NBC)*COTE+1,
ETAT_OFF = 0
ETAT_ONE = 1
ETAT_TWO = 2

class Canevas(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.root = parent
        self.cote = COTE
        self.nbc = NBC
        self.la = LA
        self.ha = HA
        self.canevas = tk.Canvas(self, 
                                 width=self.la,
                                 height=self.ha,
                                 bg='white')
        self.canevas.pack(padx=10,pady=10,expand=True)
        self.tableau=[] 
        self.init_tableau()
        self.canevas.bind("<Button-1>", self.click)
        
    def delete_matrix(self):
        for ligne in self.matrix:
            for case in ligne:
                self.canevas.delete(case)
        
    def init_tableau(self):
        self.tableau = []
        self.essaies = 0
        self.etat = ETAT_OFF
        self.allume = None
        for i in range(self.nbc):
            self.tableau.append(self.canevas.create_rectangle(i*COTE+1, 1, 
                                                              (i+1)*COTE+1, COTE+1))
        
    
    def gen_tableau(self):
        color=['blue','white','red']
        TT=[color[randrange(3)] for i in range(self.nbc)]
        T = TT[:]
        b,w,r = 0,0,len(T)-1
        sol = 0
        while w <= r:
            if T[w]=="blue":
                if T[b]!=T[w]:
                    sol += 1
                    T[b],T[w] = T[w],T[b]
                b += 1
                w += 1
            elif T[w]=="white":
                w += 1
            else:
                if T[r]!=T[w]:
                    sol += 1
                    T[w],T[r] = T[r],T[w]
                r -= 1
        self.root.info.var_max.set(str(sol))
        return TT

    def fill_tableau(self):
        self.init_tableau()
        self.T = self.gen_tableau()
        self.balle = []
        for i in range(len(self.T)):
            self.balle.append(self.canevas.create_oval(i*COTE+5, 6, 
                                                       (i+1)*COTE-4, COTE-4,
                                                       fill=self.T[i]))

    def allume_case(self,i):
        self.canevas.itemconfig(self.tableau[i], fill = 'LightGreen')

    def eteint_case(self,i):
        self.canevas.itemconfig(self.tableau[i], fill = 'white')

    def echange_case(self, i ,j):
        color1 = self.canevas.itemcget(self.balle[i], "fill")
        color2 = self.canevas.itemcget(self.balle[j], "fill")
        self.canevas.itemconfig(self.balle[i], fill = color2)
        self.canevas.itemconfig(self.balle[j], fill = color1)
        self.essaies += 1
        self.root.info.var_essaie.set(str(self.essaies))

    def num_case(self,event):
        return event.x//COTE
        
    def click(self,event):
        ncase = self.num_case(event)
        if self.etat == ETAT_OFF:
            self.allume_case(ncase)
            self.etat = ETAT_ONE
            self.allume = ncase 
        elif self.etat == ETAT_ONE:
            if ncase != self.allume:
                self.allume_case(ncase)
                self.echange_case(ncase,self.allume)
                self.eteint_case(ncase)
            self.eteint_case(self.allume)
            self.allume = None
            self.etat = ETAT_OFF

    def bbr(self):
        T=self.T[:]
        self.l_indice=bbr(T)
        self.w = 0
        self.i = 0
        self.etat = ETAT_OFF
        self.dessine()
        
    def dessine(self):
        if self.i >= len(self.l_indice):
            return
        self.ind=self.l_indice[self.i]
        if self.etat == ETAT_OFF:
            self.allume_case(self.w)
            self.etat= ETAT_ONE
            self.after(PAUSE, self.dessine)
        elif self.etat == ETAT_ONE:
            if self.w==self.ind[0]:
                self.allume_case(self.ind[1])
                self.etat = ETAT_TWO
                self.after(PAUSE, self.dessine)
            elif self.w==self.ind[1]:
                self.allume_case(self.ind[0])
                self.etat = ETAT_TWO
                self.after(PAUSE, self.dessine)
            else:
                self.eteint_case(self.w)
                self.w += 1
                self.etat = ETAT_OFF
                self.after(PAUSE, self.dessine)
        else:
            
            self.eteint_case(self.ind[0])
            self.eteint_case(self.ind[1])
            if self.ind[0]!=self.ind[1]:
                self.echange_case(self.ind[0],self.ind[1])
            if self.ind[0]<self.w or self.ind[1]<self.w:
                self.w +=1
            self.i += 1
            self.etat = ETAT_OFF
            self.after(PAUSE, self.dessine)
             
class Info(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.root = parent
        self.bouton = tk.Button(self, text="Restart",
                                 command=self.restart,
                                 width=10, height=3)
        self.bot = tk.Button(self, text="tri",
                                 command=self.bbr,
                                 width=10, height=3)
        self.label = tk.Label(self, text="Cpt:", font=("Helvetica", 16))
        
        self.var_essaie = tk.StringVar()
        self.var_max = tk.StringVar()
        self.var_essaie.set(str(self.root.canevas.essaies))
        
        self.cpt = tk.Label(self, textvariable=self.var_essaie, font=("Helvetica", 16))
        self.bar = tk.Label(self,text=" / ", font=("Helvetica", 16))
        self.maxi = tk.Label(self, textvariable=self.var_max, font=("Helvetica", 16))
        self.bouton.pack(side="bottom", expand=False)
        self.bot.pack(side="bottom",expand=False)
        self.maxi.pack(side="right",expand=False)
        self.bar.pack(side="right", expand=False)
        self.cpt.pack(side="right", expand=False)
        self.label.pack(side="right", padx=20, expand=False)
        


    def restart(self):
        self.root.canevas.fill_tableau()
        self.var_essaie.set(str(self.root.canevas.essaies))

    def bbr(self):
        self.root.canevas.bbr()

class MainApp(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.root = parent
        self.root.title("Tri bleu blanc rouge")
        self.canevas = Canevas(self)
        self.canevas.pack(side="right", padx=10, pady=10, fill="both", expand=False)
        self.info = Info(self)
        self.info.pack(side="right",padx=10,pady=10,fill="both",expand=False)

    def mainloop(self):
        self.root.mainloop()

if __name__=='__main__':
    App = MainApp(tk.Tk())
    App.pack(side="top", fill="both", expand=False)
    App.mainloop()


