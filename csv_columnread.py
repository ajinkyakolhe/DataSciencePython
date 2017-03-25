from csv import DictReader
import matplotlib.pyplot as mpl
import codecs


with codecs.open("movie_metadata.csv", encoding='utf-8', errors='ignore') as f:
    a2 = [row["title_year"] for row in DictReader(f)]
[int(i) for i in a2]

with codecs.open("movie_metadata.csv", encoding='utf-8', errors='ignore') as f:
    a1 = [row["imdb_score"] for row in DictReader(f)]
[int(i) for i in a1]
print(a1)
print(a2)

mpl.scatter(a1,a2)
mpl.show()