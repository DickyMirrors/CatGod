# https://stackoverflow.com/questions/44367238/text-to-morse-code

import winsound
import time

# define the values for the alphabet (using easy to verify strings)
alphabet = dict(
    a='.-',
    b='-...',
    c='-.-.',
    d='-..',
    e='.',
    h='....',
    l='.-..',
    o='---',
    w='.--',
    r='.-.',
    # etc.
)

def play_dot():
    winsound.Beep(600, 100)

def play_dash():
    winsound.Beep(500, 200)  # a bit lower frequency, double length

def play_char(ch):
    if ch == ' ':             # space is a special case
        time.sleep(0.9)       # wait for 0.9 seconds before returning
        return '<space>'

    morseval = alphabet[ch]   # morseval is now a series of dots/dashes
    for d in morseval:        # loop over them
        if d == '.':          # if it's a dot, play a dot
            play_dot()
        else:
            play_dash()
        time.sleep(0.1)       # a small break (0.1 secs) makes it easier on the ears

    return morseval           # return the morse value so we can see what was played.. 

def txt2morse(txt):
    for ch in txt.lower():    # convert the text to lower case, just in case..
        print play_char(ch),  # Python 2.7'ism to keep printing on the same line
    print
