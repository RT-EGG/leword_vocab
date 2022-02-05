import re
import sqlite3
import string

class WordDictionary():
    def __init__(self, in_dict_path) -> None:
        self.dictionary_path = in_dict_path
        self.valid_characters = string.ascii_lowercase

    def lookup(self, in_option):
        connection = sqlite3.connect(self.dictionary_path)
        connection.cursor()
        query = '''SELECT * FROM items'''

        regex = re.compile(in_option.search_pattern)

        result = []
        rows = connection.execute(query)
        for word in [row[1] for row in rows]:
            if len(word) != 5:
                continue
            if not self.is_valid_word(word):
                continue
            if in_option.remove_duplicate and self.has_duplicate_character(word):
                continue

            match = regex.match(word)
            if not match:
                continue

            if not self.contains_character(word, in_option.contain_characters):
                continue
            if not self.not_contains_character(word, in_option.remove_characters):
                continue

            result.append(word)

        connection.close()
        return result
    
    def is_valid_word(self, in_str):
        for char in in_str:
            if not (char in self.valid_characters):
                return False
        return True

    def has_duplicate_character(self, in_str):
        for i in range(len(in_str)):
            for j in range(i + 1, len(in_str)):
                if in_str[i] == in_str[j]:
                    return True
        return False

    def contains_character(self, in_word, in_check_characters):
        for char1 in in_check_characters:
            found = False
            for char2 in in_word:
                if char1 == char2:
                    found = True
                    break
            if not found:
                return False
        return True

    def not_contains_character(self, in_word, in_check_characters):
        for char1 in in_check_characters:
            found = False
            for char2 in in_word:
                if char1 == char2:
                    found = True
                    break
            if found:
                return False
        return True
        