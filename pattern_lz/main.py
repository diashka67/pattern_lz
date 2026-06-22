
from posrednik import Posrednik, Prepod, Kursant
from adapter import Babushka, Child, PoliteAdapter
from prototip import Face


if __name__ == "__main__":
    print("\n Посредник")
    med = Posrednik()
    prepod = Prepod('Абстрактный препод', med)
    kursant = Kursant("Питонист", med)
    med.prepod = prepod
    med.kursant = kursant

    prepod.send("Питонист, запомни: в CPython под капотом всё есть PyObject, а GIL (Global Interpreter Lock) "
            "предотвращает одновременный кейс гонки при управлении памятью через подсчет ссылок! " 
            "Твой код падает, потому что ты переопределил магический метод __get__ в дескрипторе данных "
            "без учета цепочки поиска в __getattribute__ класса, нарушив MRO (Method Resolution Order) " 
            "и вызвав бесконечную рекурсию при обращении к словарю" "__dict__ ")
    kursant.send("Сложна-а-а... Короче, я просто скопипастил декоратор с Гитхаба, бахнул туда мультипроцессинг, "
            "и у меня всё зависло намертво, а комп начал шуметь как самолет.")

    print("\n Адаптер")
    babulik = Babushka()
    gangster = Child()
    perevod = PoliteAdapter(gangster)
    perevod.translate_to_babka(babulik)


    print("\n Прототип")
    face1 = Face(15, 7, 'зеленый')
    copyface = face1.clone()
    print(f"Оригинал: {face1.colorcheeks}")
    print(f"Клон: {copyface.colorcheeks}")
