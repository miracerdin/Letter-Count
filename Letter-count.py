Task:

Count the number of each letter in a sentence.

 The department you work for undertook a project construction that makes word / text analysis. You are asked to calculate the number of letters or any chars in the sentences entered under this project.
 Write a Python program that;

1-takes a sentence from the user,
2-counts the number of each letter/chars of the sentence,
3-collects the letters/chars as a key and the counted numbers as a value in a dictionary.

answer-1:
sentence = input()
dict1 = {}
for i in sentence:
    x = sentence.count(i)
    dict1[i] = x
print(dict1)

answer-2:

sentence = input()
dict1 = {}
for i in sentence:
    if i not in dict1:
        dict1[i] = 1
    else:
        dict1[i] += 1
print(dict1
