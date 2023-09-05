#Создайте класс Person, который имеет атрибуты name, age и метод introduce(), выводящий информацию о человеке. 
#Создайте несколько объектов этого класса и вызовите метод introduce() для каждого из них.
#Понятие Императивная vs Декларативная парадигма опишу в Readme.md

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Привет, меня зовут {self.name} и мне {self.age} лет.")

Person1 = Person("Игорь", 26)
Person1.introduce()