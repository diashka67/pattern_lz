import copy

class Face:
    def __init__(self, kolichectvoeyes, kolichestvovolosbrows, colorcheeks):
        self.kolichectvoeyes = kolichectvoeyes
        self.kolichestvovolosbrows = kolichestvovolosbrows
        self.colorcheeks = colorcheeks

    def clone(self):
        return copy.deepcopy(self)

face1 = Face(15,7,'зеленый')
copyface = face1.clone()

print(copyface.colorcheeks)
