#BA1C
#Find the Reverse Complement of a String

def complement(text):
    c=''
    for i in range(len(text)):
        if (text[i]=='A'): c+='T'
        elif (text[i]=='T'): c+='A'
        elif (text[i]=='C'): c+='G'
        else: c+='C'
    c=c[::-1]
    return c


if __name__=='__main__':
    with open("C:/Users/Doris/Downloads/rosalind_ba1c.txt", "r") as f:
       text = f.readline().strip()
    print(complement(text))

