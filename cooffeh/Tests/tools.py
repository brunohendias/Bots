from os import path, system

class Msg:
    text = ''
msg = Msg()

def checkIfFileCreated(file_, method_):
    if path.exists(file_):
        system(f'rm {file_}')
        return 200
    
    return f'{method_} failed'
