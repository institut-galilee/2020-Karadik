from Tkinter import *
import camera
import sonar as s

class Interface (Frame) :
    def __init__(self, fenetre, **kwargs) :
        Frame.__init__(self, fenetre, width=320, height=240, **kwargs)
        self.pack(fill=BOTH)

        #creation widgets
        self.message = Label(self, text="Prototype poubelle ECO3, par Karadik")
        self.message.pack()
        
        #Bouton quitter
        self.bouton_quitter = Button(self, text="Quitter", command=self.quit)
        self.bouton_quitter.pack(side="left")

        self.bouton_analyse = Button(self, text="Analyser la poubelle", command=self.analyse_contenu)
        self.bouton_analyse.pack(side="top")

        self.bouton_cliquer = Button(self, text="Prendre une photo", fg="blue", command=self.cliquer)
        self.bouton_cliquer.pack(side="right")

    def cliquer(self):
        value = camera.captureImageAnalyse()
        self.message = Label(self, text=value)
        self.message.pack()

    def analyse_contenu(self):
        value = s.compute_occupancy_rate(1, 10)
        self.message = Label(self, texte=value)
        self.message.pack()