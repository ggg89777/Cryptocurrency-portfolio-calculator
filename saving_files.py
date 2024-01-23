import dill as dill

'''file loading and saving module'''

def dill_dump(path, object_to_save):
    with open(path, 'wb') as file:
        dill.dump(object_to_save, file)
def dill_load(path):
    with open(path, 'rb') as file:
        return dill.load(file)

def read_key():
    with open('API-KEY.txt') as file:
        return file.read()

def save_key(key):
    with open('API-KEY.txt', 'w') as file:
        file.write(key)
