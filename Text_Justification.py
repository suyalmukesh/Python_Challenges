def fullJustify(words, maxWidth):

    lst = [] 
    temp = ''

    for word in words:
        n = len(word)
        temp = temp.lstrip()
        if n + len(temp) + 1 <= maxWidth:
            temp += ' '
            temp += word 
        else:
            temp = temp.rstrip()
            lst.append(temp)
            temp = '' 
            temp += word
    lst.append(temp)
             
            


    return lst                 

def count_words(strr):
    count = 0 
    for word in strr:
        count += 1
    return count    








if __name__ == "__main__":
    words = ["This", "is", "an", "example", "of", "text", "justification."]
    maxWidth = 16
    print("CASE 1 : ")
    print(fullJustify(words, maxWidth))

    words = ["What","must","be","acknowledgment","shall","be"]
    maxWidth = 16
    print("CASE 2 : ")
    print(fullJustify(words, maxWidth))


    words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]
    maxWidth = 20
    print("CASE 3 : ")
    print(fullJustify(words, maxWidth))

