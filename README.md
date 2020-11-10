# poetryGenerator

This is a poem generator that generates poems using n-grams of comments from the New York Times 30 most popular articles at a given moment. 

This generator utlizes three APIs: The New York Times 'Most Popular' API, the New York Times 'Community' API and the Dictionary.com 'Thesaurus' API. 
  - The 'Most Popular' API is used to get the 30 most popular articles at a given moment
  - The 'Community' API is used to collect the comments from each of the aforementioned articles
  - The 'Thesaurus' API is used to replace mean words with nice words, as well as add alliteration to the poems by finding synonyms for words that begin with the first letter of each line, and replace them
  

Scholarly sources that acted as inspiration

https://www.aclweb.org/anthology/W17-3904.pdf
  - This paper acted as inspiration for how I collected my "inspiring set"/corpus. While they used thousands of novels to comprise their corpus, I used hundreds of article comments. 

http://reidswanson.com/?page_id=761
  - This paper discusses co-creation, which is the process of humans and computers collaboratively writing something. While the computer uses ngrams to construct the actual poem itself, humans play a role in the content from the beginning, since we are using user written comments. While this isn't necessary considered co-creation in the way Swanson describes it, it still inspired the usage of comments as my corpus. 
  
https://science.sciencemag.org/content/267/5199/843/tab-article-info
- This paper helped give me context for n-grams and how to implement

# How to run

type the following commands:

1. pipenv install

2. python NGramGenerator.py

# How this challenged me
To challenge myself on this project, I chose to incorporate three different API's, which allowed me to greatly expand on this skill which I first was exposed to by implementing an API on PQ3. I also chose to implement n-grams, which was a unique challenge and gave me good exposure to text analysis. I also was forced to closely consider how I was parsing and producing text in a way that I never have before, resulting in a fun and challenging project. 


