import locale
import pyfiglet
import sys
import time

def date(format_string = '%Y %d %b, %A', font = 'graceful'):
    locale.setlocale(locale.LC_ALL, ('RU', 'UTF8'))
    current_date = time.strftime(format_string)
    beautiful_date = pyfiglet.figlet_format(current_date, font=font)
    print(beautiful_date)

if __name__ == '__main__':
    if len(sys.argv) == 1:
        date()
    elif len(sys.argv) == 2:
        date(sys.argv[1])
    elif len(sys.argv) == 3:
        date(sys.argv[1], sys.argv[2])
    else:
        print('Usage: python3 -m figdate [format] [font]')

