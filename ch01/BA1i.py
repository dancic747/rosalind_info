#BA1i
#Find the Most Frequent Words with Mismatches in a String

import BA1g
import itertools

def make_dict(k):
    d={}
    kmers=list(itertools.product(['A','T','G','C'], repeat=k))
    for i in range(len(kmers)):
        kmers[i]=''.join(kmers[i])
        d[kmers[i]]=0
    return d


def most_frequent(text,k,d): #d = max num of mismatches // k = kmer
    dict=make_dict(k)
    for key in dict:
        for i in range(len(text)-k+1):
            if BA1g.compute_hamming_distance(key,text[i:i+k])<=d:
                dict[key]+=1
    return dict


if __name__=="__main__":
    with open("C:/Users/Doris/Downloads/rosalind_ba1i.txt", "r") as f:
        text = f.readline().strip()
        kd=f.readline().strip()
    k = int(kd.split(' ')[0])
    d=int(kd.strip().split(' ')[1])
        
    dict=most_frequent(text, k, d)
    max_value_key_list=[]
    max_value=max(dict.values())
    for key in dict:
        if dict[key]==max_value: max_value_key_list.append(key)
    print(*max_value_key_list, ' ')

