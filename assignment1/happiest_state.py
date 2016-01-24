import sys
import json

states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
                                                                                                         
    scores = {} # initialize an empty dictionary                                                                                  
    for line in open(sys.argv[1]):
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"                                  
        scores[term] = int(score)  # Convert the score to an integer.                                                             
    state_score = {}
    for line in open(sys.argv[2]):
        twit = json.loads(line)
        score = 0  
    
        if twit.has_key('text'):
            words = twit['text'].split(' ')
            for word in words:
                word.lower()
                if scores.has_key(word):
                    score += scores[word]
                
            if  twit.has_key('user'):
                if twit['user'].has_key('location'):
                    if states.has_key(twit['user']['location']):
                        
                        if state_score.has_key(twit['user'].has_key('location')) :
                            state_score[twit['user']['location']] += score
                        else:
                            state_score[twit['user']['location']] = score
    
    print max(state_score)

if __name__ == '__main__':
    main()

