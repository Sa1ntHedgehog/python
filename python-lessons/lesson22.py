import collections
string="Some lenght words words"
words = string.split()
counter=collections.Counter(words)
most_common,occurences=counter.most_common()[0]

longest=max(words,key=len)
print(most_common,longest)