
import random

def madlib(s):
    lnouns = ['dog', 'hole','park']
    lverbs = ['walked','ran','jumped']
    ladj = ['gray','big','cute','tiny','brown']
    story = s
    numnouns = story.count('NOUN')
    numverbs = story.count('VERB')
    numadj = story.count('ADJ')

    story = nouns(story,lnouns)
    story = verbs(story,lverbs)
    story = adj(story,ladj)

    return story

def nouns(story,nouns):
    parts = story.split('NOUN')
    ans = ''
    for i in range(len(parts)-1):
        ans += parts[i] + random.choice(nouns)
    return ans + parts[-1]

def verbs(story,verbs):
    parts = story.split('VERB')
    ans = ''
    for i in range(len(parts)-1):
        ans += parts[i] + random.choice(verbs)
    return ans + parts[-1]

def adj(story,adj):
    parts = story.split('ADJ')
    ans = ''
    for i in range(len(parts)-1):
        ans += parts[i] + random.choice(adj)
    return ans + parts[-1]

s = "You VERB out to the NOUN. You VERB a NOUN. Then you VERB into a ADJ NOUN."

print (madlib(s))
