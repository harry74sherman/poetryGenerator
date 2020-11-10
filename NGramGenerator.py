import requests
import random
import nltk
from Poem import Poem
from nltk.tokenize import RegexpTokenizer
tokenizer = RegexpTokenizer('\s+', gaps=True)
import os
DEGREE = 3


def generate_urls():
    '''This utlizes a New York Times API to accumulate the urls of the 30 most popular articles at the moment'''

    nyt_articles = requests.get('https://api.nytimes.com/svc/mostpopular/v2/viewed/30.json?api-key=LhFDfxEoNl7kGDVWHN7SvubcXXaCx0e7')

    titles = []
    urls = []
    for i in range(len(nyt_articles.json()["results"])):
        title = nyt_articles.json()["results"][i]["title"]
        url = nyt_articles.json()["results"][i]["url"]
        titles.append(title)
        urls.append(url)

    return urls


def generate_tokens_list(urls):
    '''Generates a list of the comments, and then turns them into a list of tokens'''

    comments = []
    all_comments = []

    for url in urls:
        try:
            article_comments = requests.get("https://api.nytimes.com/svc/community/v3/user-content/url.json?url={}&sort=newest&api-key=LhFDfxEoNl7kGDVWHN7SvubcXXaCx0e7".format(url))
            if len(article_comments.json()["results"]["comments"]) > 0:
                for i in range(len(article_comments.json()["results"]["comments"])):
                    comments.append(article_comments.json()["results"]["comments"][i]["commentBody"])
        except:
            pass
    #tokenize comments and make one massive list
    for comment in comments:
        comment = tokenizer.tokenize(comment)
        all_comments.extend(comment)

    return all_comments


def generate_ngrams(all_comments, degree):
    '''Generates the ngram dictionary, which will be used to generate random text'''
    
    ngrams = {}
    for i in range(len(all_comments)-degree):
        gram = ' '.join(all_comments[i:i+degree])
        if gram not in ngrams.keys():
            ngrams[gram] = []
        ngrams[gram].append(all_comments[i+degree])

    return ngrams


def generate_line(ngrams, all_comments, degree):
    '''Generates a line of the poem'''

    word = random.choice(all_comments)
    while not (ord(word[0]) >= 65 and ord(word[0]) <= 90):
        word = random.choice(all_comments)
    cur_line = ' '.join(all_comments[all_comments.index(word):all_comments.index(word)+degree])
    output = cur_line
    while cur_line[-1] not in ['.', '?', '!']:
        if cur_line not in ngrams.keys():
            break
        possible_words = ngrams[cur_line]
        next_word = possible_words[random.randrange(len(possible_words))]
        output += ' ' + next_word
        output_tokens = tokenizer.tokenize(output)
        cur_line = ' '.join(output_tokens[len(output_tokens)-degree:len(output_tokens)])

    output = cleanup_line(output)

    return output

def cleanup_line(line):
    '''removes text after any punctuation'''

    for i in range(len(line)-1):
        if line[i] in [',', '.', '?', '!']:
            line = line[0:i+1]
            if line[-1] == ',':
                line = line[0:-1]
            break

    return line

def generate_poem(ngrams, all_comments, degree):
    '''Creates a poem object with 5 lines of content'''
    
    poem_content = []
    for i in range(5):
        line = generate_line(ngrams, all_comments, DEGREE)
        poem_content.append(line)
    
    poem = Poem(poem_content)
    return poem


if __name__ == "__main__":
    urls = generate_urls()
    all_comments = generate_tokens_list(urls)
    ngrams = generate_ngrams(all_comments, DEGREE)
    poem = generate_poem(ngrams, all_comments, DEGREE)
    changes = poem.tighten_up()
    print("Changes Made: " + str(changes))
    poem.speak()

