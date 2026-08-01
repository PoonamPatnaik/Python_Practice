word = input("Enter the word")
char = input("Enter the char")

def check_char_occurance(word,char):
    count = 0
    for i in range(len(word)):
        if word[i] == char:
            count = count +1
    return (char,count)
def each_char_occurance(word,char):
    my_tuple =()
    count = 0
    for i in range(len(word)):
        if word[i] not in my_tuple:
            my_tuple = (word[i],1)
        else:
            my_tuple = (word[i],my_tuple[1]+1)
    return my_tuple
print(each_char_occurance(word,char))


