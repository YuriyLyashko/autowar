import datetime, re, logging, subprocess, os, sys

# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

import browser

time_to_stop = '1200'


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





def write_log_and_video(videos_dir):
    def real_decorator(func):
        def wrapper(*args, **kwargs):
            logging.info('{} started'.format(func.__name__))
            command = """ffmpeg -t {} -f gdigrab -r 30 -i desktop {}{}{}_{}.mpeg""".format(time_to_stop,
                                                                                     os.getcwd(),
                                                                                     videos_dir,
                                                                                     datetime.datetime.now().strftime('%Y_%m_%d__%H_%M_%S'),
                                                                                     func.__name__
                                                                                     )
            process = subprocess.Popen(command)

            func(*args, **kwargs)

            # subprocess.getoutput("taskkill /f /im ffmpeg.exe") #kill video writing process in taskmanager!!!
            process.kill()
            process.communicate()[0]
            logging.info('{} finished \n'.format(func.__name__))
        return wrapper
    return real_decorator

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

