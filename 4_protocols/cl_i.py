# goal is for it to call the capital letter. e.g. "Hello World" = "H", "W"


class CapitalLettersIterator:
    def __init__(self, text) -> None:
        # private attribute, if you use the method text somewhere else raises error.
        self.__text = text[:]
        # set the index to 0 before starting

    def __iter__(self):
        # set the index to 0 before starting
        self.__index = 0
        return self

    def __next__(self):
        if self.__index >= len(self.__text):
            raise StopIteration
        if self.__text[self.__index].isupper():
            upper_char = self.__text[self.__index]
            self.__index += 1
            return upper_char
        else:
            self.__index += 1
            return self.__next__()


# for next, because we only use it once, we need to use a for loop here, not within functions
for cl in CapitalLettersIterator("Hello WorlD"):
    print(cl)
