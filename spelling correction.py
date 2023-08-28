from textblob import text
word=list(input("Enter the word : ").split(" "))
# Enter the word in the format of use "_" for combined words use the space for different words
correct_words=[]
wrong_words=[]
for i in word:
    if text(i)==i:
        correct_words.append(i)
    else:
        wrong_words.append(i)
        correct_words.append(text(i))
print("Wrong word are : "+wrong_words)
print("Correct_words are : ")
for i in correct_words:
    print(i.correct(),end=' ')