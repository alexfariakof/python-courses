class ArquivoAudio:
    arquivo = ""
    def __init__(self, arquivo):
        if not arquivo.endswith(self.ext):
            raise Exception("Formatop inválido")

class ArquivoMP3(ArquivoAudio):
    ext = "mp3"
    
    def tocar(self):
        print("Tocando %s como MP3" % self.arquivo)


class ArquivoWAV(ArquivoAudio):
    ext = "wav"
    
    def tocar(self):
        print("Tocando %s como WAV" % self.arquivo)


class ArquivoOGG(ArquivoAudio):
    ext = "ogg"
    
    def tocar(self):
        print("Tocando {} como OGG".format(self.arquivo))

class ArquivoACC(ArquivoAudio):
    ext = "acc"
    
    def __init__(self, arquivo):
        super().__init__(arquivo)
        if not arquivo.endswith(".acc"):
            raise Exception("Formato inválido")
        self.arquivo = arquivo
    
    def tocar(self):
        print("Tocando {} como ACC".format(self.arquivo))
        
        
    
ogg = ArquivoOGG("musica.ogg")
mp3 = ArquivoMP3("musica.mp3")
wav = ArquivoWAV("musica.wav")
ogg.tocar()
mp3.tocar()
wav.tocar()

acc = ArquivoACC("musica.acc")

acc.tocar()