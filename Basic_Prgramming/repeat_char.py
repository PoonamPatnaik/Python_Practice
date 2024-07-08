word = input("Enter the word")
char = input("Enter the char")
wl = len(word)
count = 0
'''for i in range(wl):
    if word[i] == char:
        count = count +1
print(char,count)'''



for item in word:
    if item == char:
        count = count + 1
print(char,count)



