letters = input("Please enter a sentence.")

result_string1 = ""

for i in range(len(letters)):

    if i % 2 == 1:

        result_string1 += letters[i].upper()
        
    else:

        result_string1 += letters[i].lower()

print(result_string1)

words = letters.split()
weird_words = []


for i in range(len(words)):

    if i % 2 == 0:

        weird_words.append(words[i].upper())
    
    else:

        weird_words.append(words[i].lower())
       
    
result_string2 = " ".join(weird_words)

print(result_string2)


