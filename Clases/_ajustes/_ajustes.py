class Ajustes:
    def __init__(self):
        self.musica = True
        self.efectos_sonidos = True
    
    def on_off_musica(self):
        if self.musica:
            self.musica = False
        else:
            self.musica = True
    
    def on_off_effectos(self):
        if self.efectos_sonidos:
            self.efectos_sonidos = False
        else:
            self.efectos_sonidos = True


ajustes = Ajustes()