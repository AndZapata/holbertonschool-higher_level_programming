#!/usr/bin/python3
""" text_indentation - Function that replace special characters with \n\n """


def text_indentation(text):
    lst = []
    list2 = []
    limiters = ".?:"
    """
    Check the type of the text if it is a string,
    if not: raise an error message
    Take the old text and replace the characters
    '. ', ': ', '? ', with '\n\n'
    print the newest text with all the changes
    """
    if type(text) != str:
        raise TypeError('text must be a string')
    else:
        new_text = text.replace('.', ".\n\n")
        new_text = new_text.replace(':', ":\n\n")
        new_text = new_text.replace('?', "?\n\n")
        new_text = new_text.strip()
        lst = new_text.split('\n')
        for i in lst:
            list2.append(i.strip())
        parcial = '\n'.join(list2)
        print('\n'.join(list2))
        if len(parcial) > 0 and parcial[-1] in limiters:
            print("")
