#BA1A
#Compute the Number of Times a Pattern Appears in a Text

def Count(text, pattern):
    count = 0
    for i in range(len(text)-len(pattern)+1):
        if (text[i:i+len(pattern)] == pattern):
            count+=1
    return count


if __name__ == '__main__':
    with open("C:/Users/Doris/Downloads/rosalind_ba1a.txt", "r") as f:
        text = f.readline().strip()
        pattern = f.readline().strip()
    print(Count(text, pattern))
    