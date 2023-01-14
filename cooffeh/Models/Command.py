class Command:
    def __init__(self, com, act):
        self.command = com
        self.action = act

def add(com, act):
    return Command(com, act)