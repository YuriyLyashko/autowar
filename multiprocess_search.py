import datetime, os
from multiprocessing import Pool

from browser import find_image

cpu_cout = os.cpu_count()
print('cpu_cout', cpu_cout)




def go_1(img):
    print('{}'.format(datetime.datetime.now().strftime('%d/%m/%Y__%H:%M:%S')))
    # s = datetime.datetime.now()
    result = find_image(img)
    # print(result)
    # f = datetime.datetime.now()
    # print('go_1', f - s, '\n')
    return result

    # print('{}'.format(datetime.datetime.now().strftime('%d/%m/%Y__%H:%M:%S')))




imgs = ['accept_flash_running.png',
        'accept_flash_running.png',
        'accept_flash_running.png',
        'accept_flash_running.png',
        'a.png']


if __name__ == '__main__':
    s = datetime.datetime.now()

    with Pool(len(imgs)) as p:
        for i in p.imap_unordered(go_1, imgs):
            print(i)
            if i:
                p.terminate()
                break




    # for img in imgs:
    #     go_1(img)

    f = datetime.datetime.now()
    print('!!!', f - s, '\n')
