import spacy

nlp = spacy.load('en_core_web_md')


# I found the difference in similarity between monkey + banana and cat + banana quite interesting.
# Spacy determined that a cat and monkey were quite similar (they are both animals) and yet the similarity
# between monkey and banana was also quite high (as monkeys are associated with eating bananas).
# The similarity between cat and banana however was low, but not as low as one might expect.
# It would be hard to draw absolute similarities between a cat and a banana.
# Yet spacy has determined that there must be some.
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

tokens = nlp('cat apple monkey banana ')

for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

sentence_to_compare = "Why is my cat on the car"

sentences = ["where did my dog go",
                "Hello, there is my car",
                "I\'ve lost my car in my car",
                "I\'d like my boat back",
                "I will name my dog Diana"]

model_sentence = nlp(sentence_to_compare)

for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)