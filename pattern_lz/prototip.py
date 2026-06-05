class Babushka:
    def polite_speech(self, text:str):
        print('Люблю тебя мой внучек,очень рада тебя видеть')


class Child:
    def unpolite_speech(self):
        return 'Йоу, здарова, бабка, у меня все ништяк 67'



class PoliteAdapter:
    def __init__(self, gangster: Child ):
        self.gangster = gangster

    def translate_to_babka(self, babulik: Babushka):
        slang = self.gangster.unpolite_speech()
        polite_text = 'Привет, дорогая бабушка, у меня все очень хорошо'
        babulik.polite_speech(polite_text)

babulik = Babushka()
gangster = Child()

perevod = PoliteAdapter(gangster)
perevod.translate_to_babka(babulik)
