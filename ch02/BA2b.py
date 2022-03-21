#BA2B
#Find a Median String

import BA2a
import itertools

def make_dict(k):
    d={}
    kmers=list(itertools.product(['A','T','G','C'], repeat=k))
    for i in range(len(kmers)):
        kmers[i]=''.join(kmers[i])
        d[kmers[i]]=0
    return d


def medianString(k,dna_list):
    dict=make_dict(k)
    #dict2=make_dict(k)
    for dna in dna_list:
        for key in dict:
            hamming=[]
            for i in range(len(dna)-k+1):
                hamming.append(BA2a.compute_hamming_distance(key,dna[i:i+k]))
            dict[key]+=min(hamming)
    min_value=min(dict.values())
    keys_with_min_value=[]
    for key in dict:
        if dict[key]==min_value: keys_with_min_value.append(key)
    return keys_with_min_value


if __name__=="__main__":
    with open("C:/Users/Doris/Downloads/rosalind_ba2b.txt", "r") as f:
        k=int(f.readline().strip('\n'))
        dna_list = f.read().split()
    
    median_string_list=medianString(k,dna_list)
    print(median_string_list[0]) #if the list contains more than one element, we can choose any of them as our "final soultion"
    