#!/usr/bin/python
import re
raw_check = re.compile(r"^([^'']|[^--][a-z]+[a-z]+[\s][a-z]+|[a-z]+[-][a-z]+|[a-z]+[-][a-z]+[-][a-z]+|[a-z]+[']?[a-z]+)$")
prompt = "Please enter a one or more words separated by a space or hyphen: "
input_err = "The word(s) you entered contained invalid characters. "
lookup_word = ""
while True:
    lookup_word = raw_input(prompt).lower()
    if lookup_word == 'q':
        break
    else:        
        test = raw_check.search(lookup_word)
        if test == None:
            print input_err + "for word " + lookup_word
        else:
            print "this word: " + lookup_word + " is okay!"
