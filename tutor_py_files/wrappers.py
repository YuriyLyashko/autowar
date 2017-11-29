import datetime, re, logging

import browser

logging.basicConfig(filename='tutor_log.log',
                    level=logging.INFO,
                    datefmt='%d/%m/%Y %I:%M:%S %p',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
                    )

keywords_help_arrow = {'quest_menu': {'arg': 'help_arrow_left.png',
                                      'kwargs': {'higher_on': 0,
                                                 'lower_on': 0,
                                                 'righter_on': 0,
                                                 'lefter_on': 80,
                                                 }
                                      },
                       'squad_menu': (),
                       'order_menu': (),
                       'down_menu': (),
                       'location_icon': (),
                       'battle_icon': ()
}

def print_time(func):
    def wrapper(*args, **kwargs):
        print('{} started at {}'.format(func.__name__, datetime.datetime.now().strftime('%d/%m/%Y__%H:%M:%S')))
        func(*args)
        print('{} finished at {}\n'.format(func.__name__, datetime.datetime.now().strftime('%d/%m/%Y__%H:%M:%S')))
    return wrapper

def else_click_to_help_arrow(func):
    def wrapper(*args, **kwargs):
        if not func(*args, **kwargs):
            print('else_click_to_help_arrow {}'.format(datetime.datetime.now().strftime('%d/%m/%Y__%H:%M:%S')))
            area = re.findall(r'\w+__', *args)[0][:-2]
            print('re:', area)


            browser.find_flashing_image_and_click(keywords_help_arrow[area]['arg'],
                                                  higher_on=keywords_help_arrow[area]['kwargs']['higher_on'],
                                                  lower_on=keywords_help_arrow[area]['kwargs']['lower_on'],
                                                  righter_on=keywords_help_arrow[area]['kwargs']['righter_on'],
                                                  lefter_on=keywords_help_arrow[area]['kwargs']['lefter_on'],
                                                  **kwargs
                                                  )
            # print('{} finished at {}\n'.format(func.__name__, datetime.datetime.now().strftime('%d/%m/%Y__%H:%M:%S')))
    return wrapper

