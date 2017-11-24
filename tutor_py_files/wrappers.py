import datetime

import browser



def print_time(func):
    def wrapper(*args, **kwargs):
        print('{} started at {}'.format(func.__name__, datetime.datetime.now().strftime('%d/%m/%Y__%H:%M:%S')))
        func(*args)
        print('{} finished at {}\n'.format(func.__name__, datetime.datetime.now().strftime('%d/%m/%Y__%H:%M:%S')))
    return wrapper

def else_click_to_help_arrow(func):
    def wrapper(*args, **kwargs):
        print('else_click_to_help_arrow {}'.format(datetime.datetime.now().strftime('%d/%m/%Y__%H:%M:%S')))
        if not func(*args, **kwargs):
            print('!!!!!!!!!!!!!!!', *args)
            browser.find_flashing_image_and_click(*args, **kwargs)
            # print('{} finished at {}\n'.format(func.__name__, datetime.datetime.now().strftime('%d/%m/%Y__%H:%M:%S')))
    return wrapper

