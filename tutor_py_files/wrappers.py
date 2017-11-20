import datetime

def print_time(func):
    def wrapper(*args):
        print('{} started at {}'.format(func.__name__, datetime.datetime.now().strftime('%d/%m/%Y__%H:%M:%S')))
        func(*args)
        print('{} finished at {}\n'.format(func.__name__, datetime.datetime.now().strftime('%d/%m/%Y__%H:%M:%S')))
    return wrapper