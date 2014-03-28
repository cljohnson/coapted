#!/usr/bin/python
print 'Importing resources....'
import pprint
import re
import nltk
from nltk.corpus import wordnet as wn
print 'Done!'
#poses = [wn.NOUN, wn.VERB, wn.ADJ, wn.ADV]
lookup_word = ""
dashes = "-----------------------------------------------------------------------------------------"

def main():
    global lookup_word
    while lookup_word == "":
        lookup_word = get_word(lookup_word)
        if lookup_word != '':
            if lookup_word == 'q':
                break
            else:
                OutType = get_OutType()
                if OutType == 'q':
                    break
                else:
                    print '\nProcessing the word "' + lookup_word + '"\n'
                    synlist = process_word(lookup_word)
                    if len(synlist) > 0:
                        if OutType == 's':
                            print dashes
                            get_lemmas(lookup_word, synlist)
                            print dashes
                            get_examples(lookup_word, synlist)
                            print dashes
                            get_definitions(lookup_word, synlist)
                            lookup_word = ""
                        else:
                            syn_cnt = 0
                            for synset in synlist:
                                print dashes
                                print_lemmas(synset, lookup_word, syn_cnt)
                                print_examples(synset, lookup_word, syn_cnt)
                                print_definitions(synset, lookup_word, syn_cnt)
                                syn_cnt +=1
                    else:
                        print "come back to handle word without synonynms"
                    print "\n\n"

def get_word(lookup_word):
    raw_check = re.compile(r"^([^'']|[^--][a-z]+[a-z]+[\s][a-z]+|[a-z]+[-][a-z]+|[a-z]+[-][a-z]+[-][a-z]+|[a-z]+[']?[a-z]+)$")
    prompt = "Please enter a one or more words separated by a space or hyphen: "
    input_err = "  contains invalid characters. "
    while True:
        lookup_word = raw_input(prompt).lower()
        if lookup_word in ['', 'q']:
            break
        else:        
            test = raw_check.search(lookup_word)
            if test == None:
                print lookup_word + input_err
            else:
                break    
    return lookup_word

def get_OutType():
    prompt = "Output data as (S)ets of Lemmas, Examples and Definitions,\nor in (T)ree form for each synset associated with the word provided?"
    OutType = "Please enter the first letter of the chosen output type as shown in parenthesis (S)et or (T)ree, or (Q)uit:"
    while True:
        OutType = raw_input(prompt).lower()
        if OutType in ['q', 's', 't']:
            break
    return OutType

def process_word(lookup_word):
    synlist = wn.synsets(lookup_word)
    print "\nNumber of synsets = " + str(len(synlist)) + "\n"
    cnt = 0
    for synset in synlist:
        print "#" + str(cnt) + ": " + str(synset)
        cnt +=1
    return synlist

def get_lemmas(lookup_word, synlist):
    syn_cnt = 0
    for synset in synlist:
        print_lemmas(synset, lookup_word, syn_cnt)
        syn_cnt +=1

def get_examples(lookup_word, synlist):
    syn_cnt = 0
    for synset in synlist:
        print_examples(synset, lookup_word, syn_cnt)
        syn_cnt +=1

def get_definitions(lookup_word, synlist):
    syn_cnt = 0
    for synset in synlist:
        print_definitions(synset, lookup_word, syn_cnt)
        syn_cnt +=1

def print_lemmas(synset, lookup_word, syn_cnt):
    print "\nLemmas for " + lookup_word + ", " + "synset #" + str(syn_cnt) + ": " + str(synset)
    lemmas = synset.lemmas
    print "\nFor " + str(synset) + " there are " + str(len(lemmas)) + " lemmas:"
    lem_cnt = 0
    for lemma in lemmas:
        print "     #" + str(lem_cnt) + ": " + str(lemma)
        lem_cnt +=1

def print_examples(synset, lookup_word, syn_cnt):
    print "\nExamples for synset #" + str(syn_cnt) + ": " + synset.name
    examples = synset.examples
    ex_cnt = 0
    for example in examples:
        print "     Example #" + str(ex_cnt) + ": " + example
        ex_cnt +=1

def print_definitions(synset, lookup_word, syn_cnt):
    syn_def = synset.definition
    print "\nDefinition for synset #" + str(syn_cnt) + ": " + synset.name + ":"
    print "     " + syn_def

if __name__ == "__main__":
    main()

