class Super:
    def method(self):
        print("I am Super.method") # Стандартное поведение
    def delegate(self):
        self.action() # Ожидается опредение метода
class Inheritor(Super): # Буквльное наследование метода
    pass
class Replacer(Super):
    def method(self):
        print("I am Replacer.method") # Полное замещение метода
class Extender(Super): # Расширение поведения метода
    def method(self):
        print("Starting Extender.method")
        Super.method(self)
        print("Ending Extender.method")
class Provider(Super): # Заполнение обязательного метода
    def action(self):
        print("I am Provider.action")


if __name__ == "__main__":
    for klass in (Inheritor, Replacer, Extender):
        print("\n" + klass.__name__ + "...")
        klass().method()
    print("\nProvider...")
    x = Provider()
    x.delegate()