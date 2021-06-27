# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import math

def num_BTC(b):
    t = int (b/210000)
    r = b % 210000
    s = 0
    c = 50
    for i in range(0, t):
        s += 210000 * c
        c /= 2
    s += r * c
    return s



