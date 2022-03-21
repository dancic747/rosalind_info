#BA1J
#Find Frequent Words with Mismatches and Reverse Complements

import BA1c
import BA1g
import itertools

def make_dict(k):
    d={}
    kmers=list(itertools.product(['A','T','G','C'], repeat=k))
    for i in range(len(kmers)):
        kmers[i]=''.join(kmers[i])
        d[kmers[i]]=0
    return d


def mismatches(text,k,d):
    dict=make_dict(k)
    for key in dict:
        for i in range(len(text)-k+1):
            if BA1g.compute_hamming_distance(key,text[i:i+k])<=d:
                dict[key]+=1
            if BA1g.compute_hamming_distance(BA1c.complement(key),text[i:i+k])<=d:
                dict[key]+=1
    return dict


if __name__=="__main__" :
    with open("C:/Users/Doris/Downloads/rosalind_ba1j.txt", "r") as f:
        text = f.readline().strip()
        kd=f.readline().strip()
    k = int(kd.split(' ')[0])
    d=int(kd.strip().split(' ')[1])

    dict=mismatches(text,k,d)
    max_value=max(dict.values())
    max_value_key_list=[]
    for key in dict:
        if dict[key]==max_value: max_value_key_list.append(key)
    print(*max_value_key_list, ' ')

