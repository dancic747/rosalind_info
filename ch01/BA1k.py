#BA1K
#Generate the Frequency Array of a String

import itertools

def make_dict(k):
    d={}
    kmers=list(itertools.product(['A','T','G','C'], repeat=k))
    for i in range(len(kmers)):
        kmers[i]=''.join(kmers[i])
        d[kmers[i]]=0
    return d


def frequency_array(text,k):
    dict=make_dict(k)
    for key in dict:
        for i in range(len(text)-k+1):
            if text[i:i+k]==key: dict[key]+=1
    return dict


if __name__=="__main__":
    with open("C:/Users/Doris/Downloads/rosalind_ba1k.txt", "r") as f:
        text = f.readline().strip()
        k=int(f.readline().strip())

    dict=frequency_array(text,k)
    sorted_values=[]
    for key in sorted(list(dict.keys())):
        sorted_values.append(dict[key])
    print(*sorted_values,' ', file=open('output.txt','w'))