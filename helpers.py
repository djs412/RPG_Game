##Strings
import sys
import time
import textwrap


def slow_print(plist, sleeptime):
    for strng in plist:
        for letter in textwrap.fill(strng, 50, replace_whitespace = False):
            sys.stdout.write(letter)
            #print(letter, end = "")
            time.sleep(sleeptime)
        print()
    if len(plist) >1:
        print()
    return

def helper(st):
    if st == "":
        st = " "
        return st
    
    if len(st) > 0:
        st = st.lstrip()
        return str.lower(st[0])

def rep(x): return x.replace("\n", "")

