import argparse
import sys

from gui import GUI
from word_dictionary import WordDictionary

def parse_args():
    parser = argparse.ArgumentParser(prog='leword_vocab')

    parser.add_argument('-d', '--dictionary', type=str, default="./assets/ejdict.sqlite3", help='path to help file.')
    
    return parser.parse_args(sys.argv[1:])

def main(in_args):
    dictionary = WordDictionary(in_args.dictionary)
    gui = GUI()

    def search():
        option = gui.get_search_option()
        gui.set_word_list(dictionary.lookup(option))

    gui.search_execute_command = lambda: search()
    gui.mainloop()

if __name__ == '__main__':
    sys.exit(main(parse_args()))
