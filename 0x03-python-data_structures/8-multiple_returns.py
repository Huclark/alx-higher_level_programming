#!/usr/bin/python3
def multiple_returns(sentence):
    """Returns a tuple with the length of a string and its first character"""
    if sentence == "":
        strlen = None
    else:
        strlen = len(sentence)

    character = sentence[0]

    return strlen, character
