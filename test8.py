#Given two sentences, return an array that has the words that appear in one sentence and not
#the other and an array with the words in common. 

sentence1 = 'We are really pleased to meet you in our city'
sentence2 = 'The city was hit by a really heavy storm'

nuevo1 = sentence1.split()
print(nuevo1)
set1 = set(nuevo1)
print(nuevo1)

nuevo2 = sentence2.split()
set2= set(nuevo2)
print(nuevo2)

resultigual = set1.intersection(set2)
resultdif = set1.symmetric_difference(set2)

print(resultigual)
print(resultdif)
