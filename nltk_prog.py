from nltk.stem import PorterStemmer
wd_stem = PorterStemmer()
print(wd_stem.stem("eating"))
print(wd_stem.stem("going"))
print(wd_stem.stem("playing"))
print(wd_stem.stem("dancing"))