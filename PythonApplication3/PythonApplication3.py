import pprint
print 'Importing resources....'
import nltk
print 'Done!'
#W = nltk.corpus.reader.wordnet
#wn = W.WordNetCorpusReader(nltk.data.find('corpora/wordnet'))
from nltk.corpus import wordnet as wn
poses = [wn.NOUN, wn.VERB, wn.ADJ, wn.ADV]
def main():
    get_word()

def get_word():
    while True:
        lookup_word = raw_input('Enter a word or Q: ').lower()
        if lookup_word in("", "q"):
            break
        elif type(lookup_word) != type(str()):
            print "Input must be a string!"
        else:
            print lookup_word
            process_word(lookup_word)


def process_word(lookup_word):
    synlist = wn.synsets(lookup_word)
    print "synlist = " + str(synlist)
    print "Number of synonyms = " + str(len(synlist))
    cnt = 0
    print 
    for syn in synlist:
        synonym = wn.synsets(lookup_word)[cnt]
        print "Synonym #" + str(cnt) + ": " + str(synonym)
        cnt +=1

def get_lemmas(lookup_word):
    syn = wn.synsets(lookup_word)[0]
    lemmas = syn.lemmas
    lemmas_cnt = len(lemmas)
    print "There are " + str(lemmas_cnt) + " lemmas for the word " + lookup_word 
    return lemmas

def print_lemmas(lemmas):
    lemmas_cnt = len(lemmas)
    for lemma in lemmas:
        print str(lemma)


if __name__ == "__main__":
    main()

