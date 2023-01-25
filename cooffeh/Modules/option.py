from Models.Option import Option

class Options:
    lista = []

    def find(self, index):
        return self.lista[index]

    def add(self, obj):
        self.lista.append(obj)

    def quantity(self):
        return len(self.lista) - 1

options = Options()
def get(index):
    return options.find(index)

def set(msg):
    option = Option()
    option.chat = msg.from_user.id
    option.text = msg.text
    options.add(option)
    return options.quantity()
