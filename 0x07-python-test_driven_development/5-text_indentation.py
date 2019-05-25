#!/usr/bin/python3
""" text_indentation - Function that replace special characters with \n\n """


def text_indentation(text):
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
        new_text = text.replace('. ', ".\n\n")
        new_text = new_text.replace(': ', ":\n\n")
        new_text = new_text.replace('? ', "?\n\n")
        print(new_text)
