#!/usr/bin/python3
text_indentation = __import__('5-text_indentation').text_indentation

text_indentation("""Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
Quonam modo? Utrum igitur tibi litteram videor an totas paginas commovere? \
Non autem hoc: igitur ne illud quidem. Fortasse id optimum, sed ubi illud: \
Plus semper voluptatis? Teneo, inquit, finem illi videri nihil dolere. \
Transfer idem ad modestiam vel temperantiam, quae est moderatio cupiditatum \
rationi oboediens. Si id dicis, vicimus. Inde sermone vario sex illa a Dipylo \
stadia confecimus. Sin aliud quid voles, postea. Quae animi affectio suum \
cuique tribuens atque hanc, quam dico. Utinam quidem dicerent alium alio \
beatiorem! Iam ruinas videres""")

try:
    text_indentation(683463664236236234)
except Exception as e:
    print(e)

try:
    text_indentation('H')
except Exception as e:
    print(e)

try:
    text_indentation(7.7)
except Exception as e:
    print(e)

try:
    text_indentation([7.7, 34564, 74247])
except Exception as e:
    print(e)

try:
    text_indentation((5, 6))
except Exception as e:
    print(e)

try:
    text_indentation("Holberton.")
except Exception as e:
    print(e)

try:
    text_indentation("Holberton.\\,,.:??:.")
except Exception as e:
    print(e)

try:
    print("**********************")
    text_indentation("  \n    .\n        ")
except Exception as e:
    print(e)
