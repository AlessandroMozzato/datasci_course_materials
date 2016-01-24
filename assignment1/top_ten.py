import sys
import json

def main():                                              
    hashtags = {}
    tot_hash = 0
    for line in open(sys.argv[1]):
        twit = json.loads(line)
                
        if twit.has_key('entities'):
            for hasht in twit['entities']:
                if hasht == 'hashtags' and twit['entities'][hasht]:
                    if twit['entities'][hasht]:
                        for el in twit['entities'][hasht]:
                            word = el['text']
                            if hashtags.has_key(word):
                                hashtags[word] += 1
                            else:
                                hashtags[word] = 1
                            tot_hash = tot_hash + 1    
#    for hasht in hashtags:
#        hashtags[hasht] = hashtags[hasht]/float(tot_hash)
        
    nprint = 0
    hashtags_temp = dict(hashtags)
    while nprint < 10:
        for hasht in hashtags:
            if hashtags_temp.has_key(hasht) and hashtags[hasht] == max(hashtags_temp.values()) and nprint < 10:
                print hasht.encode('utf-8'), hashtags[hasht]
                nprint = nprint + 1
                hashtags_temp.pop(hasht)
            
            
if __name__ == '__main__':
    main()

