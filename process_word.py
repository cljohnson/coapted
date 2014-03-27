#!/usr/bin/python
print 'Importing resources....'
import pprint
import re
import nltk
from nltk.corpus import wordnet as wn
print 'Done!'
#poses = [wn.NOUN, wn.VERB, wn.ADJ, wn.ADV]

def main():
    lookup_word = ""
    while lookup_word == "":
        lookup_word = get_word(lookup_word)
        if lookup_word != '':
            if lookup_word == 'q':
                break
            else:
                print '\nProcessing the word "' + lookup_word + '"\n'
                synlist = process_word(lookup_word)
                if len(synlist) > 0:
                    process_lemmas(lookup_word, synlist)
                    get_examples(lookup_word, synlist)
                    get_definitions(lookup_word, synlist)
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

def process_word(lookup_word):
    synlist = wn.synsets(lookup_word)
    print "\nNumber of synsets = " + str(len(synlist)) + "\n"
    cnt = 0
    for synset in synlist:
        print "#" + str(cnt) + ": " + str(synset)
        cnt +=1
    return synlist

def process_lemmas(lookup_word, synlist):
    print "\nLemmas for " + lookup_word
    for synset in synlist:
        lemmas = synset.lemmas
        print "\nFor " + str(synset) + " there are " + str(len(lemmas)) + " lemmas:\n"
        cnt = 0
        for lemma in lemmas:
            print "     #" + str(cnt) + ": " + str(lemma)
            cnt +=1

def get_examples(lookup_word, synlist):
    syn_cnt = 0
    for synset in synlist:
        print "\nExamples for " + synset.name + "\n"
        examples = synset.examples
        ex_cnt = 0
        for example in examples:
            print "     Example #" + str(ex_cnt) + ": " + example
            ex_cnt +=1
        syn_cnt +=1


def get_definitions(lookup_word, synlist):
    print "\nDefinitions for " + lookup_word + "\n"
    cnt = 0
    for synset in synlist:
        syn_def = synset.definition
        print "    #" + str(cnt) + ": " + syn_def
        cnt +=1

if __name__ == "__main__":
    main()

