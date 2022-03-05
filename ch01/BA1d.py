#BA1D
#Find All Occurrences of a Pattern in a String


def position(text, pattern):
    positions=[]
    l=len(pattern)
    for i in range(len(text)-l+1):
        if text[i:i+l]==pattern: positions.append(i)
    return positions


if __name__=='__main__':
    with open("C:/Users/Doris/Downloads/rosalind_ba1d.txt", "r") as f:
        pattern=f.readline().strip()
        text=f.readline().strip()
    positions=position(text, pattern)
    print(*positions, ' ')