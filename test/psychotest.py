#!/usr/bin/python3
#!-*-encoding:Utf-8-*-

from tkinter import *
   
# La ScrollBar en class! Préparation pour l'application.
class ScrollCanvas(Frame):
    def __init__(self, boss=None):
        Frame.__init__(self, borderwidth=borderwidth, relief=relief)
        self.can=Canvas(self, width=width, height=height, bd=bd,
            bg=bg, relief=relief)
        self.frame = Frame(self.can)
        self.vsb = Scrollbar(self, orient=VERTICAL, command=self.can.yview)
        self.can.configure(yscrollcommand=self.vsb.set)
        self.vsb.pack(side=RIGHT, fill=Y)
        self.can.pack(side=LEFT, fill=BOTH, expand=YES)
        self.can.create_window((4,4), window=self.frame, anchor=NW, 
                                  tags="self.frame")
        self.frame.bind("<Configure>", self.onFrameConfigure)


# Class de la barre des menus
class MenuBar(Frame):
    """Barre menu déroulant"""
    def __init__(self, boss=None):
        Frame.__init__(self, borderwidth=5, bg='dim grey', padx=0)
        # Bouton pour page d'accueil
        FunnyButton=Button(self, text ="Page d'accueil", relief=GROOVE, fg='cyan', bg='grey15', 
                           activebackground='cyan', 
                           command=boss.page).pack(side =LEFT, padx=3)
        # Menu fichier
        fileMenu = Menubutton(self, text='Fichier', fg='white', bg='snow4', relief=GROOVE)
        fileMenu.pack(side=LEFT, padx=3)
        # Partie déroulante
        me1 = Menu(fileMenu, tearoff=0)
        me1.add_command(label='Tutorial', underline=0, background='black', activebackground='aquamarine',
                        foreground='aquamarine', activeforeground='black',
                        command=boss.showtuto)
        me1.add_command(label="Note de l'auteur", underline=0, background='black', activebackground='aquamarine',
                        foreground='aquamarine', activeforeground='black',
                        command=boss.showprea)
        me1.add_command(label='Bibliographie', underline=0, background='black', activebackground='aquamarine',
                        foreground='aquamarine', activeforeground='black',
                        command=boss.showbiblio)
        me1.add_command(label='QUITTER', underline=0, background='black', activebackground='red',
                        foreground='red', activeforeground='white',
                        command=boss.quit)
        # Intégration du menu fichier
        fileMenu.configure(activeforeground='black', activebackground='cyan', menu=me1)

        # Menu Principal
        self.cmd=Menubutton(self, text='Menu', fg='white', bg='snow4', relief=GROOVE)
        self.cmd.pack(side=LEFT, padx=3)
        # Partie déroulante du menu principal
        me1=Menu(self.cmd)
        me1.add_command(label="CLICK ON IT !", underline=0, background='black', activebackground='aquamarine',
                        foreground='aquamarine', activeforeground='black',
                        command=boss.showonit)
        me1.add_command(label='EQUIVALENCES', underline=0, background='black', activebackground='aquamarine',
                        foreground='aquamarine', activeforeground='black',
                        command=boss.showdico)
        me1.add_command(label='BENZODIAZEPINES', underline=0, background='black', activebackground='aquamarine',
                        foreground='aquamarine', activeforeground='black',
                        command=boss.showbzd)
        me1.add_command(label='Installation', background='black', activebackground='aquamarine',
                        foreground='yellow', activeforeground='black',
                        command=boss.instalpy)
        # Intégration du menu Préambule
        self.cmd.configure(activeforeground='black', activebackground='cyan', menu=me1)

        # Liste des médicaments 
        self.cmd2=Menubutton(self, text='A-K', fg='cyan', bg='snow4', relief=GROOVE)
        self.cmd2.pack(side=LEFT, padx=3)
        # Partie déroulante du menu 1
        me1=Menu(self.cmd2)
        me1.add_command(label='Abilify', background='black', activebackground='aquamarine',                      
                        foreground='aquamarine', activeforeground='black',
                        command=boss.showap6)
        me1.add_command(label='Anafranil', background='black', activebackground='aquamarine',
                        foreground='aquamarine', activeforeground='black',
                        command=boss.showatd4)
        me1.add_command(label='Anxiolit', background='black', activebackground='aquamarine',
                        foreground='aquamarine', activeforeground='black',
                        command=boss.showtrx3)
        me1.add_command(label='Atarax', background='black', activebackground='aquamarine',
                        foreground='aquamarine', activeforeground='black',
                        command=boss.showtrx5)
        me1.add_command(label='Aurorix', background='black', activebackground='aquamarine',
                        foreground='aquamarine', activeforeground='black',
                        command=boss.showatd6)
        me1.add_command(label='Benocten', background='black', activebackground='aquamarine',
                        foreground='aquamarine', activeforeground='black',
                        command=boss.showhypno3)
        me1.add_command(label='Briviact', background='black', activebackground='aquamarine',
                        foreground='aquamarine', activeforeground='black',
                        command=boss.showmae6)
        me1.add_command(label='Bromides', background='black', activebackground='aquamarine',
                        foreground='yellow', activeforeground='black',
                        command=boss.showmae5)
        me1.add_command(label='Buspar', background='black', activebackground='aquamarine',
                        foreground='yellow', activeforeground='black',
                        command=boss.showtrx5)
        me1.add_command(label='Carbamazépine', background='black', activebackground='aquamarine',
                        foreground='aquamarine', activeforeground='black',
                        command=boss.showmae5)
        me1.add_command(label='Chlorpromazine', background='black', activebackground='aquamarine',
                        foreground='yellow', activeforeground='black',
                        command=boss.showap5)
        me1.add_command(label='Clopin', background='black', activebackground='aquamarine',
                        foreground='aquamarine', activeforeground='black',
                        command=boss.showap5)
        me1.add_command(label='Clopixol', background='black', activebackground='aquamarine',
                        foreground='aquamarine', activeforeground='black',
                        command=boss.showap5)
        me1.add_command(label='Cipralex', background='black', activebackground='aquamarine',
                        foreground='aquamarine', activeforeground='black',
                        command=boss.showatd5)
        me1.add_command(label='Circadin', background='black', activebackground='aquamarine',
                        foreground='aquamarine', activeforeground='black',
                        command=boss.showhypno7)
        me1.add_command(label='(Citalopram)', background='black', activebackground='aquamarine',
                        foreground='orange', activeforeground='black',
                        command=boss.showatd5)
        me1.add_command(label='Cymbalta', background='black', activebackground='aquamarine',
                        foreground='aquamarine', activeforeground='black',
                        command=boss.showatd7)
        me1.add_command(label='Dalmadorm', background='black', activebackground='aquamarine',
                        foreground='aquamarine', activeforeground='black',
                        command=boss.showtrx4)
        me1.add_command(label='Demetrin', background='black', activebackground='aquamarine',
                        foreground='aquamarine', activeforeground='black',
                        command=boss.showtrx3)
        me1.add_command(label='Depakine', background='black', activebackground='aquamarine',
                        foreground='aquamarine', activeforeground='black',
                        command=boss.showmae5)
        me1.add_command(label='Deroxat', background='black', activebackground='aquamarine',
                        foreground='aquamarine', activeforeground='black',
                        command=boss.showatd5)
        me1.add_command(label='Detensor', background='black', activebackground='aquamarine',
                        foreground='aquamarine', activeforeground='black',
                        command=boss.showhypno3)
        me1.add_command(label='Diazépam', background='black', activebackground='aquamarine',
                        foreground='aquamarine', activeforeground='black',
                        command=boss.showmae5)
        me1.add_command(label='Distraneurin', background='black', activebackground='aquamarine',
                        foreground='aquamarine', activeforeground='black',
                        command=boss.showhypno6)
        me1.add_command(label='Dogmatil', background='black', activebackground='aquamarine',
                        foreground='aquamarine', activeforeground='black',
                        command=boss.showap6)
        me1.add_command(label='Dormicum', background='black', activebackground='aquamarine',
                        foreground='aquamarine', activeforeground='black',
                        command=boss.showmae6)
        me1.add_command(label='Efexor', background='black', activebackground='aquamarine',
                        foreground='aquamarine', activeforeground='black',
                        command=boss.showatd7)
        me1.add_command(label='Entumine', background='black', activebackground='aquamarine',
                        foreground='aquamarine', activeforeground='black',
                        command=boss.showap5)
        me1.add_command(label='(Ethosuximide)', background='black', activebackground='aquamarine',
                        foreground='orange', activeforeground='black',
                        command=boss.showmae5)
        me1.add_command(label='Floxyfral', background='black', activebackground='aquamarine',
                        foreground='aquamarine', activeforeground='black',
                        command=boss.showatd5)
        me1.add_command(label='Fluanxol', background='black', activebackground='aquamarine',
                        foreground='aquamarine', activeforeground='black',
                        command=boss.showap5)
        me1.add_command(label='Fycompa', background='black', activebackground='aquamarine',
                        foreground='aquamarine', activeforeground='black',
                        command=boss.showmae6)
        me1.add_command(label='Gabitril', background='black', activebackground='aquamarine',
                        foreground='aquamarine', activeforeground='black',
                        command=boss.showmae6)
        me1.add_command(label='Halcion', background='black', activebackground='aquamarine',
                        foreground='aquamarine', activeforeground='black',
                        command=boss.showtrx4)
        me1.add_command(label='Haldol', background='black', activebackground='aquamarine',
                        foreground='aquamarine', activeforeground='black',
                        command=boss.showap5)
        me1.add_command(label='Imovane', background='black', activebackground='aquamarine',
                        foreground='aquamarine', activeforeground='black',
                        command=boss.showtrx5)
        me1.add_command(label='Inovelon', background='black', activebackground='aquamarine',
                        foreground='aquamarine', activeforeground='black',
                        command=boss.showmae6)
        me1.add_command(label='Invega', background='black', activebackground='aquamarine',
                        foreground='aquamarine', activeforeground='black',
                        command=boss.showap6)
        me1.add_command(label='Keppra', background='black', activebackground='aquamarine',
                        foreground='aquamarine', activeforeground='black',
                        command=boss.showmae6)
        # Intégration du menu 1
        self.cmd2.configure(activeforeground='black', activebackground='cyan', menu=me1)

        # Liste des médicaments 2
        self.cmd3=Menubutton(self, text='L-S', fg='cyan', bg='snow4', relief=GROOVE)
        self.cmd3.pack(side=LEFT, padx=3)
        # Partie déroulante du menu 2
        me1=Menu(self.cmd3)
        me1.add_command(label='Lamictal', background='black', activebackground='aquamarine',
                        foreground='aquamarine', activeforeground='black',
                        command=boss.showmae6)
        me1.add_command(label='(Lamotrigine)', background='black', activebackground='aquamarine',
                        foreground='orange', activeforeground='black',
                        command=boss.showmae6)
        me1.add_command(label='Lexotanil', background='black', activebackground='aquamarine',
                        foreground='aquamarine', activeforeground='black',
                        command=boss.showtrx3)
        me1.add_command(label='Lithium', background='black', activebackground='aquamarine',
                        foreground='aquamarine', activeforeground='black',
                        command=boss.showsh4)
        me1.add_command(label='Ludiomil', background='black', activebackground='aquamarine',
                        foreground='yellow', activeforeground='black',
                        command=boss.showatd4)
        me1.add_command(label='Lyrica', background='black', activebackground='aquamarine',
                        foreground='aquamarine', activeforeground='black',
                        command=boss.showmae6)
        me1.add_command(label='Melatonine', background='black', activebackground='aquamarine',
                        foreground='aquamarine', activeforeground='black',
                        command=boss.showhypno7)
        me1.add_command(label='(Midazolam)', background='black', activebackground='aquamarine',
                        foreground='orange', activeforeground='black',
                        command=boss.showmae6)
        me1.add_command(label='Moclamine', background='black', activebackground='aquamarine',
                        foreground='aquamarine', activeforeground='black',
                        command=boss.showatd6)
        me1.add_command(label='Mysoline', background='black', activebackground='aquamarine',
                        foreground='aquamarine', activeforeground='black',
                        command=boss.showmae5)
        me1.add_command(label='Neurontin', background='black', activebackground='aquamarine',
                        foreground='aquamarine', activeforeground='black',
                        command=boss.showmae6)
        me1.add_command(label='Noctamid', background='black', activebackground='aquamarine',
                        foreground='aquamarine', activeforeground='black',
                        command=boss.showtrx4)
        me1.add_command(label='Nozinan', background='black', activebackground='aquamarine',
                        foreground='aquamarine', activeforeground='black',
                        command=boss.showap5)
        me1.add_command(label='(Olanzapine)', background='black', activebackground='aquamarine',
                        foreground='orange', activeforeground='black',
                        command=boss.showap6)
        me1.add_command(label='Orap', background='black', activebackground='aquamarine',
                        foreground='yellow', activeforeground='black',
                        command=boss.showap6)
        me1.add_command(label='(Paroxetine)', background='black', activebackground='aquamarine',
                        foreground='orange', activeforeground='black',
                        command=boss.showatd5)
        me1.add_command(label='Phénergan', background='black', activebackground='aquamarine',
                        foreground='aquamarine', activeforeground='black',
                        command=boss.showhypno3)
        me1.add_command(label='Petinimid', background='black', activebackground='aquamarine',
                        foreground='aquamarine', activeforeground='black',
                        command=boss.showmae5)
        me1.add_command(label='Phénobarbital', background='black', activebackground='aquamarine',
                        foreground='aquamarine', activeforeground='black',
                        command=boss.showmae5)
        me1.add_command(label='Phénytoïne', background='black', activebackground='aquamarine',
                        foreground='aquamarine', activeforeground='black',
                        command=boss.showmae5)
        me1.add_command(label='Prozac', background='black', activebackground='aquamarine',
                        foreground='aquamarine', activeforeground='black',
                        command=boss.showatd5)
        me1.add_command(label='(Quétiapine)', background='black', activebackground='aquamarine',
                        foreground='orange', activeforeground='black',
                        command=boss.showap6)
        me1.add_command(label='Regitine', background='black', activebackground='aquamarine',
                        foreground='yellow', activeforeground='black',
                        command=boss.showatd6)
        me1.add_command(label='Remeron', background='black', activebackground='aquamarine',
                        foreground='aquamarine', activeforeground='black',
                        command=boss.showatd7)
        me1.add_command(label='Risperdal', background='black', activebackground='aquamarine',
                        foreground='aquamarine', activeforeground='black',
                        command=boss.showap6)
        me1.add_command(label='Rivotril', background='black', activebackground='aquamarine',
                        foreground='aquamarine', activeforeground='black',
                        command=boss.showtrx3)
        me1.add_command(label='Rohypnol', background='black', activebackground='aquamarine',
                        foreground='aquamarine', activeforeground='black',
                        command=boss.showhypno4)
        me1.add_command(label='Sabril', background='black', activebackground='aquamarine',
                        foreground='yellow', activeforeground='black',
                        command=boss.showmae6)
        me1.add_command(label='Saroten', background='black', activebackground='aquamarine',
                        foreground='aquamarine', activeforeground='black',
                        command=boss.showatd4)
        me1.add_command(label='Semap', background='black', activebackground='aquamarine',
                        foreground='yellow', activeforeground='black',
                        command=boss.showap6)
        me1.add_command(label='Seresta', background='black', activebackground='aquamarine',
                        foreground='aquamarine', activeforeground='black',
                        command=boss.showtrx3)
        me1.add_command(label='Seropram', background='black', activebackground='aquamarine',
                        foreground='aquamarine', activeforeground='black',
                        command=boss.showatd5)
        me1.add_command(label='Seroquel', background='black', activebackground='aquamarine',
                        foreground='aquamarine', activeforeground='black',
                        command=boss.showap6)
        me1.add_command(label='Solian', background='black', activebackground='aquamarine',
                        foreground='aquamarine', activeforeground='black',
                        command=boss.showap6)
        me1.add_command(label='Sonata', background='black', activebackground='aquamarine',
                        foreground='aquamarine', activeforeground='black',
                        command=boss.showhypno7)
        me1.add_command(label='Stilnox', background='black', activebackground='aquamarine',
                        foreground='aquamarine', activeforeground='black',
                        command=boss.showtrx5)
        me1.add_command(label='Stilnox CR', background='black', activebackground='aquamarine',
                        foreground='aquamarine', activeforeground='black',
                        command=boss.showhypno7)
        me1.add_command(label='Surmontil', background='black', activebackground='aquamarine',
                        foreground='aquamarine', activeforeground='black',
                        command=boss.showatd4)
        # Intégration du menu 2
        self.cmd3.configure(activeforeground='black', activebackground='cyan', menu=me1)

        # Liste des médicaments 3
        self.cmd4=Menubutton(self, text='T-Z', fg='cyan', bg='snow4', relief=GROOVE)
        self.cmd4.pack(side=LEFT, padx=3)
        # Partie déroulante du menu 3
        me1=Menu(self.cmd4)
        me1.add_command(label='Taloxa', background='black', activebackground='aquamarine',
                        foreground='aquamarine', activeforeground='black',
                        command=boss.showmae6)
        me1.add_command(label='Temesta', background='black', activebackground='aquamarine',
                        foreground='aquamarine', activeforeground='black',
                        command=boss.showtrx3)
        me1.add_command(label='Tiapridal', background='black', activebackground='aquamarine',
                        foreground='aquamarine', activeforeground='black',
                        command=boss.showap5)
        me1.add_command(label='Tofranyl', background='black', activebackground='aquamarine',
                        foreground='aquamarine', activeforeground='black',
                        command=boss.showatd4)
        me1.add_command(label='Topamax', background='black', activebackground='aquamarine',     
                        foreground='aquamarine', activeforeground='black',
                        command=boss.showmae6)
        me1.add_command(label='Tranxiulum', background='black', activebackground='aquamarine',
                        foreground='aquamarine', activeforeground='black',
                        command=boss.showtrx3)
        me1.add_command(label='(Trazodone)', background='black', activebackground='aquamarine',
                        foreground='orange', activeforeground='black',
                        command=boss.showatd4)
        me1.add_command(label='Trileptal', background='black', activebackground='aquamarine',
                        foreground='aquamarine', activeforeground='black',
                        command=boss.showmae6)
        me1.add_command(label='Trittico', background='black', activebackground='aquamarine',
                        foreground='aquamarine', activeforeground='black',
                        command=boss.showatd4)
        me1.add_command(label='Trobalt', background='black', activebackground='aquamarine',
                        foreground='aquamarine', activeforeground='black',
                        command=boss.showmae6)
        me1.add_command(label='Truxal', background='black', activebackground='aquamarine',
                        foreground='aquamarine', activeforeground='black',
                        command=boss.showhypno3)
        me1.add_command(label='Urbanyl', background='black', activebackground='aquamarine',
                        foreground='aquamarine', activeforeground='black',
                        command=boss.showtrx3)
        me1.add_command(label='(Valium)', background='black', activebackground='aquamarine',
                        foreground='orange', activeforeground='black',
                        command=boss.showtrx3)
        me1.add_command(label='(Valproate)', background='black', activebackground='aquamarine',
                        foreground='orange', activeforeground='black',
                        command=boss.showmae5)
        me1.add_command(label='(Venlafaxine)', background='black', activebackground='aquamarine',
                        foreground='orange', activeforeground='black',
                        command=boss.showatd7)
        me1.add_command(label='Vimpat', background='black', activebackground='aquamarine',
                        foreground='aquamarine', activeforeground='black',
                        command=boss.showmae6)
        me1.add_command(label='Xanax', background='black', activebackground='aquamarine',
                        foreground='aquamarine', activeforeground='black',
                        command=boss.showtrx3)
        me1.add_command(label='Zoloft', background='black', activebackground='aquamarine',
                        foreground='aquamarine', activeforeground='black',
                        command=boss.showatd5)
        me1.add_command(label='Zonegran', background='black', activebackground='aquamarine',
                        foreground='aquamarine', activeforeground='black',
                        command=boss.showmae6)
        me1.add_command(label='Zyprexa', background='black', activebackground='aquamarine',
                        foreground='aquamarine', activeforeground='black',
                        command=boss.showap6)
        # Intégration du menu 3
        self.cmd4.configure(activeforeground='black', activebackground='cyan', menu=me1)

        # Bouton des Abréviations
        FunnyButton2=Button(self, text ="Abréviations", relief=GROOVE, fg='white', bg='snow4', 
                            activebackground='cyan', command=boss.showabr1).pack(side =LEFT, padx=3)

        # Menu MAE
        self.mae=Menubutton(self, text='Anti-épileptiques', fg='white', bg='snow4', relief=GROOVE)
        self.mae.pack(side=LEFT, padx=3)
        # Partie déroulante du menu Antiépileptiques
        me1=Menu(self.mae)
        me1.add_command(label="Propriétés des MAE", underline=0, background='black', activebackground='aquamarine',
                        foreground='aquamarine', activeforeground='black',
                        command=boss.showmae2)
        me1.add_command(label="Effets secondaires des MAE", underline=0, background='black', activebackground='aquamarine',
                        foreground='aquamarine', activeforeground='black',
                        command=boss.showmae3)
        me1.add_command(label='Interactions', underline=0, background='black', activebackground='aquamarine',
                        foreground='red', activeforeground='red',
                        command=boss.showmae4) 
        # Sous-menu pour les MAE
        me2=Menu(me1)
        me2.add_command(label='1ère génération MAE', underline=0, background='black', activebackground='aquamarine',
                        foreground='aquamarine', activeforeground='black',
                        command=boss.showmae5)
        me2.add_command(label='2ème génération MAE', underline=0, background='black', activebackground='aquamarine',
                        foreground='aquamarine', activeforeground='black',
                        command=boss.showmae6)
        # Intégration du sous-menu
        me1.add_cascade(label='Médicaments anti-épileptiques', underline=0, background='black', foreground='aquamarine', 
                        activeforeground='black', activebackground='aquamarine', menu=me2)
        # Intégration du menu Antiépileptiques
        self.mae.configure(activeforeground='black', activebackground='cyan', menu=me1)

        # Menu Antipsychotiques
        self.ap=Menubutton(self, text='Neuroleptiques', fg='white', bg='snow4', relief=GROOVE)
        self.ap.pack(side=LEFT, padx=3)
        # Partie déroulante du menu Antipsychotique
        me1=Menu(self.ap)
        me1.add_command(label='Propriétés des AP', underline=0, background='black', activebackground='aquamarine',
                        foreground='aquamarine', activeforeground='black',
                        command=boss.showap0)    
        me1.add_command(label='Effets secondaires des AP', underline=0, background='black', activebackground='aquamarine',
                        foreground='aquamarine', activeforeground='black',
                        command=boss.showap1)                  
        me1.add_command(label='Syndrome extrapyramidal', underline=0, background='black', activebackground='aquamarine',
                        foreground='aquamarine', activeforeground='black',
                        command=boss.showap2)                 
        me1.add_command(label='Syndrome Neuroleptique Malin', underline=0, background='black', activebackground='aquamarine',
                        foreground='aquamarine', activeforeground='black',
                        command=boss.showap3)
        me1.add_command(label='Interactions', underline=0, background='black', activebackground='aquamarine',
                        foreground='red', activeforeground='red',
                        command=boss.showap4)
        # Sous-menu pour les AP
        me2=Menu(self.ap)
        me2.add_command(label='1ère génération antipsychotiques', underline=0, background='black', activebackground='aquamarine',
                        foreground='aquamarine', activeforeground='black',
                        command=boss.showap5)
        me2.add_command(label='Antipsychotiques atypiques', underline=0, background='black', activebackground='aquamarine',
                        foreground='aquamarine', activeforeground='black',
                        command=boss.showap6)
        # Intégration du sous-menu
        me1.add_cascade(label='Antipsychotiques', underline=0, background='black', foreground='aquamarine', 
                        activeforeground='black', activebackground='aquamarine', menu=me2)
        # Intégration du menu Antipsychotique
        self.ap.configure(activeforeground='black', activebackground='cyan', menu=me1)

        # Menu Antidépresseurs
        self.atd=Menubutton(self, text='Antidépresseurs', fg='white', bg='snow4', relief=GROOVE)
        self.atd.pack(side=LEFT, padx=3)
        # Partie déroulante du menu Antidépresseurs
        me1=Menu(self.atd)
        me1.add_command(label='Propriétés des AD', underline=0, background='black', activebackground='aquamarine',
                        foreground='aquamarine', activeforeground='black',
                        command=boss.showatd0)  
        me1.add_command(label='Syndrome sérotoninergique', underline=0, background='black', activebackground='aquamarine',
                        foreground='aquamarine', activeforeground='black',
                        command=boss.showatd1)   
        me1.add_command(label='Effets secondaires AD', underline=0, background='black', activebackground='aquamarine',
                        foreground='aquamarine', activeforeground='black',
                        command=boss.showatd2)                      
        me1.add_command(label='Interactions', underline=0, background='black', activebackground='aquamarine',
                        foreground='red', activeforeground='red',
                        command=boss.showatd3)
        # Sous-menu pour les ATD
        me2=Menu(self.atd)
        me2.add_command(label='Antidépresseurs TCC', underline=0, background='black', activebackground='aquamarine',
                        foreground='aquamarine', activeforeground='black',
                        command=boss.showatd4)
        me2.add_command(label='Antidépresseurs ISRS', underline=0, background='black', activebackground='aquamarine',
                        foreground='aquamarine', activeforeground='black',
                        command=boss.showatd5)
        me2.add_command(label='Antidépresseurs IMAO', underline=0, background='black', activebackground='aquamarine',
                        foreground='aquamarine', activeforeground='black',
                        command=boss.showatd6)
        me2.add_command(label='Antidépresseurs Sélectifs', underline=0, background='black', activebackground='aquamarine',
                        foreground='aquamarine', activeforeground='black',
                        command=boss.showatd7)             
        # Intégration du sous-menu
        me1.add_cascade(label='Antidépresseurs', underline=0, background='black', foreground='aquamarine', 
                        activeforeground='black', activebackground='aquamarine', menu=me2)
        # Intégration du menu Antidépresseurs
        self.atd.configure(activeforeground='black', activebackground='cyan', menu=me1)

        # Menu des stabilisateurs d'humeur
        self.sh=Menubutton(self, text='Thymorégulateurs', fg='white', bg='snow4', relief=GROOVE)
        self.sh.pack(side=LEFT, padx=3)
        # Partie déroulante du menu SH
        me1=Menu(self.sh)
        me1.add_command(label='Propriétés des SH', underline=0, background='black', activeforeground='black',
                        foreground='aquamarine', activebackground='aquamarine',   
                        command=boss.showsh0)
        me1.add_command(label='Effets secondaires SH', underline=0, background='black', activeforeground='black', 
                        foreground='aquamarine', activebackground='aquamarine',   
                        command=boss.showsh1)
        me1.add_command(label='Interactions', underline=0, background='black', activebackground='aquamarine',
                        foreground='red', activeforeground='red',
                        command=boss.showsh2)
        # Sous-menu pour les SH
        me2=Menu(self.sh)
        me2.add_command(label='Généralités', underline=0, background='black', activebackground='aquamarine',
                        foreground='aquamarine', activeforeground='black',
                        command=boss.showsh3)
        me2.add_command(label='Lithium', underline=0, background='black', activebackground='aquamarine',
                        foreground='aquamarine', activeforeground='black',
                        command=boss.showsh4)
        me2.add_command(label='Carbamazépine', underline=0, background='black', activebackground='aquamarine',
                        foreground='aquamarine', activeforeground='black',
                        command=boss.showmae5)
        # Intégration du sous-menu
        me1.add_cascade(label='Thymorégulateurs', underline=0, background='black', foreground='aquamarine', 
                        activeforeground='black', activebackground='aquamarine', menu=me2)
        # Intégration du menu Stabilisateur d'humeur
        self.sh.configure(activeforeground='black', activebackground='cyan', menu=me1)     

        # Menu des tranquilisants
        self.trx=Menubutton(self, text='Anxiolytiques', fg='white', bg='snow4', relief=GROOVE)
        self.trx.pack(side=LEFT, padx=3)
        # Partie déroulante du menu tranx      
        me1=Menu(self.trx)
        me1.add_command(label='Propriétés des TR', underline=0, background='black', activeforeground='black',
                        foreground='aquamarine', activebackground='aquamarine',
                        command=boss.showtrx0)
        me1.add_command(label='Effets secondaires des anxiolytiques', underline=0, background='black', 
                        activeforeground='black', activebackground='aquamarine',
                        foreground='aquamarine', 
                        command=boss.showtrx1)
        me1.add_command(label='Interactions', underline=0, background='black', activebackground='aquamarine',
                        foreground='red', activeforeground='red',
                        command=boss.showtrx2)       
       # Sous-menu pour les 3 classes de tranquilisants
        me2=Menu(self.trx)
        me2.add_command(label='BZD anxiolytiques', underline=0, background='black', activebackground='aquamarine',
                        foreground='aquamarine', activeforeground='black',
                        command=boss.showtrx3)
        me2.add_command(label='BZD hypno-inductrices', underline=0, background='black', 
                        activebackground='aquamarine', activeforeground='black',
                        foreground='aquamarine', 
                        command=boss.showtrx4)
        me2.add_command(label='Sédatifs et anxiolytiques non BZD', underline=0, background='black', 
                        activebackground='aquamarine', activeforeground='black',
                        foreground='aquamarine', 
                        command=boss.showtrx5)
        # Intégration du sous-menu tranx
        me1.add_cascade(label='3 classes tranquilisants', underline=0, background='black', foreground='aquamarine', 
                        activeforeground='black', activebackground='aquamarine', menu=me2)
        # Intégration du menu tranx
        self.trx.configure(activeforeground='black', activebackground='cyan', menu=me1)

        # Menu des hypnotiques
        self.hypno=Menubutton(self, text='Hypnotiques', fg='white', bg='snow4', relief=GROOVE)
        self.hypno.pack(side=LEFT, padx=3)
        # Partie déroulante du menu hypno
        me1=Menu(self.hypno)
        me1.add_command(label='Propriétés des Hypno', underline=0, background='black', 
                        activebackground='aquamarine', activeforeground='black',
                        foreground='aquamarine', 
                        command=boss.showhypno0)
        me1.add_command(label='Effets secondaires des hypnotiques', underline=0, background='black', 
                        activebackground='aquamarine', activeforeground='black',
                        foreground='aquamarine', 
                        command=boss.showhypno1)
        me1.add_command(label='Interactions', underline=0, background='black', 
                        activebackground='aquamarine', activeforeground='red',
                        foreground='red', 
                        command=boss.showhypno2)
        me2=Menu(self.hypno)
        me2.add_command(label='NL et antihistaminique', underline=0, background='black', 
                        activebackground='aquamarine', activeforeground='black',
                        foreground='aquamarine', 
                        command=boss.showhypno3)
        me2.add_command(label='Benzodiazépines', underline=0, background='black', 
                        activebackground='aquamarine', activeforeground='black', 
                        foreground='aquamarine', 
                        command=boss.showhypno4)
        me2.add_command(label='Barbituriques', underline=0, background='black', 
                        activebackground='aquamarine', activeforeground='black', 
                        foreground='aquamarine', 
                        command=boss.showhypno5) 
        me2.add_command(label='Non barbituriques', underline=0, background='black', 
                        activebackground='aquamarine', activeforeground='black', 
                        foreground='aquamarine', 
                        command=boss.showhypno6)
        me2.add_command(label='Autres hypnotiques', underline=0, background='black',
                        activebackground='aquamarine', activeforeground='black',
                        foreground='aquamarine', 
                        command=boss.showhypno7)   
        # Intégration du sous-menu dans le menu hypnotique
        me1.add_cascade(label='Divers hypnotiques', underline=0, background='black', 
                        foreground='aquamarine', 
                        activeforeground='black', activebackground='aquamarine', menu=me2) 
        # Intégration du menu hypno
        self.hypno.configure(activeforeground='black', activebackground='cyan', menu=me1) 

# Application principale
class Application(Frame):
    def __init__(self, boss=None):
        Frame.__init__(self, borderwidth=5, bg='grey22', padx=20, pady=20, relief=GROOVE)
        self.master.title('PSYCHOTABS - Developed by CK - Nov. 2017')
        mBar = MenuBar(self)
        mBar.pack(side=TOP, fill=X, expand=YES)
        # ScrollCanvas limite de la zone à parcourir avec la barre
        self.can = Canvas(self, width=1250, height=800, bg='snow3')
        self.frame = Frame(self.can)
        self.vsb = Scrollbar(self, orient=VERTICAL, command=self.can.yview)
        self.can.configure(yscrollcommand=self.vsb.set)
        self.can.bind_all("<MouseWheel>", self._on_mousewheel)
        self.vsb.pack(side=RIGHT, fill=Y)
        self.can.pack(side=LEFT, fill=BOTH, expand=YES)
        self.can.create_window((4,4), window=self.frame, anchor=NW,
                                  tags="self.frame")
        # Insertion du texte
        self.can.create_text(625, 500, anchor=CENTER,
            text="Python 3.5 - Tkinter 8.6 - GIMP 2.8",
            font=('Times New Roman', 18), fill='aquamarine')
        self.can.create_text(170, 770, anchor=NE, text="Copyright (C) 2017 Inc.",
            font=('Times', 12), fill='white')
        self.can.pack(side=LEFT, fill=BOTH, expand=YES)
        # Configuration de la Scrollbar sur le Frame
        self.frame.bind("<Configure>", self.onFrameConfigure)
        # Création de 4 boutons
        button1 = Button(self, text="CLICK ON IT!", font=70, bg='navy', fg='turquoise',
            anchor = CENTER, command = self.showonit)
        button1.configure(width=15, activebackground='SteelBlue', activeforeground='white',
            relief=GROOVE)
        button1_window = self.can.create_window(425, 600, anchor=CENTER, window=button1)
        button2 = Button(self, text="TUTORIAL", font=74, bg='navy', fg='turquoise',
            anchor = CENTER, command = self.showtuto)
        button2.configure(width=15, activebackground='SteelBlue', activeforeground='white',
            relief=GROOVE)
        button2_window = self.can.create_window(625, 600, anchor=CENTER, window=button2)
        button4 = Button(self, text="EQUIVALENCES", font=70, bg='navy', fg='turquoise',
                         anchor = CENTER, command = self.showdico)
        button4.configure(width=15, activebackground='SteelBlue', activeforeground='white',
            relief=GROOVE)
        button4_window = self.can.create_window(825, 600, anchor=CENTER, window=button4)
        self.pack()

    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(-1*(event.delta/120), "units")

    # Méthode pour reconfigurer la scrollbar à chaque fois
    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.can.configure(scrollregion=self.can.bbox(ALL))

    def effacer(self):
        '''Réinitialise le canevas quand on passe d'un à l'autre'''
        self.can.delete(ALL)