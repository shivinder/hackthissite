#!/usr/bin/env python3
# unscrambling words
# HTS - Programming Challenge - 1
# Date: 6th October 2018

# define the list filenames
wordlist_file = 'wordlist.txt'
jumbledlist_file = 'jumbledlist.txt'

# define the lists with all the words
# we are going to read everything to memory
matched_words = []

# read the jumbled list file to the list var
with open(jumbledlist_file,'r') as fh_jumbledlist:
    jumbled_words_list = [line.rstrip() for line in fh_jumbledlist]

# read the dictionary file to the list var
with open(wordlist_file,'r') as fh_wordlist:
    dictionary_words_list = [line.rstrip() for line in fh_wordlist]

# the core comparision logic here
for jumbled_word in jumbled_words_list:
    jumbled_word_length = len(jumbled_word)

    for dictionary_word in dictionary_words_list:
        dictionary_word_length = len(dictionary_word)

        # define word match flag vars. gets reset in every iteration
        word_match = True

        # begin the comparision logic only if the length of the 2 words matches
        if(jumbled_word_length==dictionary_word_length):
            
            # comparing the characters of the words in the list
            for j_char in jumbled_word:
                # count the number of characters in both the words. 
                # idea is that they should match
                jumbled_word_char_count = jumbled_word.count(j_char)
                dictionary_word_char_count = dictionary_word.count(j_char)

                if(jumbled_word_char_count!=dictionary_word_char_count):
                    word_match = False
                    break
                
        else:
            word_match = False
        
        # if the word has matched. append it to the list
        if(word_match):
            matched_words.append(dictionary_word)
            break

# print the matched words on terminal in a comma separated list
print(','.join([matched_word for matched_word in matched_words]))
