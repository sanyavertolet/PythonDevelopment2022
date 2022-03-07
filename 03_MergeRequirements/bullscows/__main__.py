from bullscows.gameplay import gameplay
from bullscows.utils import ask
from bullscows.utils import inform

import sys
import urllib

sys.path.append('.')

if 2 <= len(sys.argv) <= 3:
    dictionary_path = sys.argv[1]
    length = sys.argv[2] if len(sys.argv) == 3 else 5
    dictionary = ''
    try:
        with open(dictionary) as f:
            dictionary = f.read()
    except FileNotFoundError:
        try:
            response = urllib.request.urlopen(dictionary_path)
            dictionary = response.read().decode()
        except:
            raise RuntimeError('Please set either valid path or url to dictionary.')
    words = dictionary.split()
    print(gameplay(ask, inform, words))
else:
    raise RuntimeError('Usage: python3 -m bullscows <dictionary/link> [length]')
