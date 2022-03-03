#BA1A
#Compute the Number of Times a Pattern Appears in a Text


def Count(text, pattern):
    count = 0
    for i in range(0, len(text)-len(pattern)+1):
        if (text[i:i+len(pattern)] == pattern):
            count+=1
    return count


if __name__ == '__main__':
    
    text=input('text: ')
    pattern=input('pattern:  ')
    c=Count(text,pattern)
    print(c)