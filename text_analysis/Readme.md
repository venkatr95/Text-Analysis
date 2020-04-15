#Text Analytics (TA) / Data Mining

NLTK - Natural language toolkit

ext mining is a process of exploring sizeable textual data and find patterns. Text Mining process the text itself, while NLP process with the underlying metadata. Finding frequency counts of words, length of the sentence, presence/absence of specific words is known as text mining. Natural language processing is one of the components of text mining.


Tokenization
------------
First step in TA. Process of breaking down text paragraph into smalleer chunks. Token is an entity that forms a sentence or a paragraph

Word Tokenization
------------------
Word tokenizer breaks text paragraph into words.

Stopwords
---------
Stopwords are considered as noise in the text. To remove stopwords, create a list and filter your tokens from words

Lexicon Normalization
---------------------
Lexicon normalization considers another type of noise in the text. For example, connection, connected, connecting word reduce to a common word "connect". It reduces derivationally related forms of a word to a common root word.

Stemming
--------
Stemming is a process of linguistic normalization, which reduces words to their word root word or chops off the derivational affixes. For example, connection, connected, connecting word reduce to a common word "connect".

Lemmatization
-------------
Lemmatization reduces words to their base word, which is linguistically correct lemmas. It transforms root word with the use of vocabulary and morphological analysis. Lemmatization is usually more sophisticated than stemming. Stemmer works on an individual word without knowledge of the context. For example, The word "better" has "good" as its lemma. This thing will miss by stemming because it requires a dictionary look-up.