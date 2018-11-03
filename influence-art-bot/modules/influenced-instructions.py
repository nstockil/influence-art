"""
Class that makes the decisions on what actions to carry out
"""

from random import choice

strokeOptions = ["arc", "line", "angle", "shape"]

stroke = choice(strokeOptions)

print(stroke)