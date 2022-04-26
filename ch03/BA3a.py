#BA3A
#Generate the k-mer Composition of a String

def composition(text,k):
    kmers=[]
    for i in range(len(text)-k+1):
        kmers.append(text[i:i+k])
    return kmers


if __name__=='__main__':
    with open("C:/Users/Doris/Downloads/rosalind_ba3a.txt", "r") as f:
        k = int(f.readline().strip())
        text = f.readline().strip()
    
    kmers=composition(text,k)
    print(*kmers, sep='\n', file=open('output.txt','w'))