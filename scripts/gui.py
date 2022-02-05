import string
import tkinter

from search_option import SearchOption


class GUI:
    def __init__(self) -> None:
        self.window = None
        self.entries_known_character = []
        self.entry_contain_characters = None
        self.entry_remove_characters = None
        self.check_remove_duplicate = None
        self.list_box_words = None

        self.next_character_entries = {}
        self.value_remove_duplicate = None
        self.value_list_box_word = None

        self.search_execute_command = None

    def mainloop(self):
        self.window = tkinter.Tk()
        self.window.title('leword_vocab')
        self.window.geometry("600x400")

        self.frame_options = tkinter.Frame(self.window, width=200)
        self.frame_options.propagate(False)
        self.frame_options.pack(side=tkinter.LEFT, fill=tkinter.Y)


        self.button_search = tkinter.Button(self.frame_options, text='検索',
                                        command=lambda: self.__search_button_click())
        self.button_search.propagate(True)
        self.button_search.grid(row=0, column=0, rowspan=1, columnspan=5, sticky=tkinter.E+tkinter.W, pady=2, padx=2)

        self.label_known_characters = tkinter.Label(self.frame_options, text='判明済の文字')
        self.label_known_characters.grid(row=1, column=0, rowspan=1, columnspan=1, sticky=tkinter.W, padx=2, pady=2)

        self.entries_known_character = []
        entry_font = ("", 48)
        entry_validation_command = self.window.register(self.__validate_entry_character)
        for i in range(5):
            entry = tkinter.Entry(self.frame_options, name=f'character_entry_{i}', 
                                    width=2, font=entry_font,
                                    validate='all',
                                    validatecommand=(entry_validation_command, '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W'),
                                    justify=tkinter.CENTER)
            entry.grid(row=2, column=i, rowspan=1, columnspan=1, padx=2)
            self.entries_known_character.append(entry)

            if i > 0:
                self.next_character_entries[str(self.entries_known_character[i-1])] = entry

        self.label_contains_characters = tkinter.Label(self.frame_options, text='含まれる文字')
        self.label_contains_characters.grid(row=3, column=0, rowspan=1, columnspan=1, sticky=tkinter.W, padx=2, pady=2)
        self.entry_contain_characters = tkinter.Entry(self.frame_options, justify=tkinter.LEFT)
        self.entry_contain_characters.grid(row=4, column=0, rowspan=1, columnspan=5, sticky=tkinter.E+tkinter.W, padx=2, pady=2)

        self.label_remove_characters = tkinter.Label(self.frame_options, text='除外する文字')
        self.label_remove_characters.grid(row=5, column=0, rowspan=1, columnspan=1, sticky=tkinter.W, padx=2, pady=2)
        self.entry_remove_characters = tkinter.Entry(self.frame_options, justify=tkinter.LEFT)
        self.entry_remove_characters.grid(row=6, column=0, rowspan=1, columnspan=5, sticky=tkinter.E+tkinter.W, padx=2, pady=2)

        self.value_remove_duplicate = tkinter.BooleanVar()
        self.value_remove_duplicate.set(True)
        self.check_remove_duplicate = tkinter.Checkbutton(self.frame_options, variable=self.value_remove_duplicate, text='同じ文字は1回のみ')
        self.check_remove_duplicate.grid(row=7, column=0, rowspan=1, columnspan=5, sticky=tkinter.W, padx=2, pady=2)

        self.value_list_box_word = tkinter.StringVar()
        list_box_words = tkinter.Listbox(self.window, listvariable=self.value_list_box_word, width=200)
        list_box_words.propagate(True)
        list_box_words.pack(side=tkinter.LEFT, expand=True, fill=tkinter.BOTH)

        self.window.mainloop()

    def get_search_option(self):
        result = SearchOption()
        result.search_pattern = ''
        for i in range(5):
            char = self.entries_known_character[i].get()
            if char == '':
                result.search_pattern = result.search_pattern + '.'
            else:
                result.search_pattern = result.search_pattern + char
        result.contain_characters = self.entry_contain_characters.get()
        result.remove_characters = self.entry_remove_characters.get()
        result.remove_duplicate = self.value_remove_duplicate.get()

        return result

    def set_word_list(self, in_list):
        self.value_list_box_word.set(in_list)

    def __validate_entry_character(self, in_action, in_index, in_new_str, in_old_str, in_item, in_validate_options, in_mode, in_name):
        if in_mode == 'key':
            if not (in_item in string.ascii_lowercase):
                if in_new_str != '': # delete character
                    return False

            if in_name in self.next_character_entries.keys():
                self.next_character_entries[in_name].focus_set()
            
        return True

    def __search_button_click(self):
        if self.search_execute_command is not None:
            self.search_execute_command()
