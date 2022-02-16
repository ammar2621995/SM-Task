from django.utils.html import escape, strip_tags

def cleanInput(input):
    input = escape(input)
    input = strip_tags(input)

    return input