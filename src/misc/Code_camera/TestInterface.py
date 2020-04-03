from tkinter import *
import camera

class Interface (Frame) :
    def __init__(self, fenetre, **kwargs) :
        Frame.__init__(self, fenetre, width=320, height=240, **kwargs)
        self.pack(fill=BOTH)

        #creation widgets
        self.message = Label(self, text="Interface de Test")
        self.message.pack()
        
        #Bouton quitter
        self.bouton_quitter = Button(self, text="Quitter", command=self.quit)
        self.bouton_quitter.pack(side="left")

        self.bouton_cliquer = Button(self, text="Prendre une photo", fg="blue", command=self.cliquer)
        self.bouton_cliquer.pack(side="right")

    def cliquer(self):
        camera.captureImageAnalyse()