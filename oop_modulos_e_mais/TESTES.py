from datetime import datetime


def data():
    hora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return print(hora)


data()