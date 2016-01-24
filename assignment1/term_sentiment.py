import sys
import json

def hw():
#    print 'Hello, world!'
    pass

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw()
#    lines(sent_file)
#    lines(tweet_file)

    scores = {} # initialize an empty dictionary                                                    
    for line in open(sys.argv[1]):
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"    
        scores[term] = int(score)  # Convert the score to an integer.                               

    #print scores.items() # Print every (term, score) pair in the dictionary     
    twit_dic = {}
    for line in open(sys.argv[2]):
        twit = json.loads(line)
        score = 0
        if twit.has_key('text'):
            words = twit['text'].split(' ')
            for word in words:
                
                word = word.lower()
                if scores.has_key(word):
                    score += scores[word]
            for word in words:        
                word = word.lower()
                if twit_dic.has_key(word) and not(scores.has_key(word)) and word.isalpha():
                    twit_dic[word][0] = twit_dic[word][0] + score
                    twit_dic[word][1] = twit_dic[word][1] + 1
                elif not(twit_dic.has_key(word)) and not(scores.has_key(word)) and word.isalpha():
                    twit_dic[word] = [0,0]
                    twit_dic[word][0] = score
                    twit_dic[word][1] = 1
                    
    for word in twit_dic:
#        word.encode('utf-8')
        print word.encode('utf-8'),twit_dic[word][0]/twit_dic[word][1]

if __name__ == '__main__':
    main()
