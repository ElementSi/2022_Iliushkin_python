from nltk.stem.snowball import SnowballStemmer
from nltk.corpus import stopwords
import nltk
import numpy as np


headlines = ["Британская полиция знает о местонахождении основателя WikiLeaks",
             "В суде США начинается процесс против россиянина, рассылавшего спам",
             "Церемонию вручения Нобелевской премии мира бойкотируют 19 стран",
             "В Великобритании арестован основатель сайта Wikileaks Джулиан Ассандж",
             "Украина игнорирует церемонию вручения Нобелевской премии",
             "Шведский суд отказался рассматривать апелляцию основателя Wikileaks",
             "НАТО и США разработали планы обороны стран Балтии против России",
             "Полиция Великобритании нашла основателя WikiLeaks, но, не арестовала",
             "В Стокгольме и Осло сегодня состоится вручение Нобелевских премий"]

new_headlines = []

for line in headlines:
    line = line.lower().split(' ')
    new_headlines.append(line)

headlines = new_headlines

new_headlines = []

for line in headlines:
    new_line = []
    for word in line:
        word = word.split(',')[0]
        new_line.append(word)
    new_headlines.append(new_line)

headlines = new_headlines

new_headlines = []

for line in headlines:
    new_line = []
    for word in line:
        if len(word) >= 3:
            new_line.append(word)
    new_headlines.append(new_line)

headlines = new_headlines

stemmer = SnowballStemmer("russian")
russian_stopwords = stopwords.words("russian")

new_headlines = []

for line in headlines:
    new_line = []
    for word in line:
        new_line.append(stemmer.stem(word))
    new_headlines.append(new_line)

headlines = new_headlines

word_set = set()

for line in headlines:
    for word in line:
        word_set.add(word)

word_list = list(word_set)
FREQ = []

for word in word_list:
    freq_rate = []
    for line in headlines:
        is_found = 0
        for line_word in line:
            if line_word == word:
                is_found += 1
        freq_rate.append(is_found)
    FREQ.append(freq_rate)

print(word_list)
print(FREQ)

U, S, Vh = np.linalg.svd(FREQ)

print(S)
