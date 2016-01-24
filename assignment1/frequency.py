import sys
import json

def main():
    tweet_file = open(sys.argv[1])                     
    twit_dic = {}
    n_twit = 0
    for line in open(sys.argv[1]):
        n_twit = n_twit + 1
        twit = json.loads(line)
        if twit.has_key('text'):
            words = twit['text'].split(' ')
            for word in words:
                
                word = word.lower()
                if word.isalpha() and twit_dic.has_key(word):
                    twit_dic[word] = twit_dic[word] + 1
                elif word.isalpha() and not(twit_dic.has_key(word)):
                    twit_dic[word] = 1

    total = 0                

    for word in twit_dic:
        total = total + twit_dic[word]
                    
    for word in twit_dic:
        print word.encode('utf-8'),twit_dic[word]/float(total)

if __name__ == '__main__':
    main()
