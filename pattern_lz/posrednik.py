#эта строка нужна для того, чтобы Python не ругался, когда я использую названия классов, которые написаны ниже по тексту.
from __future__ import annotations
from abc import ABC

class Mediator(ABC):
    def transmit(self, sender:object, text:str):
        pass
    
class Posrednik(Mediator):
    def __init__(self):
        self.prepod: Prepod
        self.kursant: Kursant
        
    def transmit(self, sender:object, text:str):
        if sender == self.prepod:
            translated = self._translate_for_kursant(text)
            self.kursant.receive(translated)
            
        if sender == self.kursant:
            translated = self._translate_for_prepod(text)
            self.prepod.receive(translated)
            
            
    def _translate_for_kursant(self, text: str):
        if "cpython" in text.lower() and "gil" in text.lower(): 
            return ( "Короче, питонист: Python внутри устроен хитро. Из-за одной защитной заглушки (GIL) " 
                    "твой код не может юзать все ядра процессора одновременно. А сломалось всё потому, " 
                    "что ты переписал скрытые настройки Питона (дескрипторы) и нарушил порядок поиска "
                    "переменных (MRO). В итоге Питон зациклился, пытаясь найти переменную внутри "
                    "самого себя, и сошел с ума." ) 
        return text
        
        
    def  _translate_for_prepod(self, text: str):
        if "мультипроцессинг" in text.lower() or "скопипастил" in text.lower():
            return ("Уважаемый профессор, я попытался применить паттерн 'Декоратор' для кастомизации "
                    "логики, а также задействовал модуль multiprocessing для обхода ограничений GIL. "
                    "Однако возникла взаимная блокировка (deadlock) и критическая нагрузка на CPU." )
        return text
        
class Prepod:
    def __init__(self, name:str, mediator: Mediator):
        self.name = name
        self.mediator = mediator
        
    def send(self, text:str):
        print(self.name,':', text )
        self.mediator.transmit(self, text)
        
    def receive(self, text: str):
        print(f"{self.name} → получает: {text}") 
        
class Kursant:
    def __init__(self, name:str, mediator: Mediator):
        self.name = name
        self.mediator = mediator
        
    def send(self, text:str):
        print(self.name,':', text )
        self.mediator.transmit(self, text)
        
    def receive(self, text: str):
        print(f"{self.name} получает: {text}") 
        
