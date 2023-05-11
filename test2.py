# For a given sentence, return the average word length. 
# Note: Remember to remove punctuation first.

sentence1 = "Hi all, my name is Tom...I am originally from Australia."
sentence2 = "I need to work very hard to learn more about algorithms in Python!"

p = ['!', '.', ','] 

def analizo (sentence): 
    for p in sentence:
            listo = sentence.replace(p,'')
            nuevo= listo.split()
            cuento = len(nuevo)
            print(len(nuevo))
            break

res1 = analizo(sentence1)
res2 = analizo(sentence2)

prom = (res1 + res2)/2
print(prom)