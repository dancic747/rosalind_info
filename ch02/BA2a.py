#BA2A
#Implement MotifEnumeration

import itertools

def make_dict(k):
    d={}
    kmers=list(itertools.product(['A','T','G','C'], repeat=k))
    for i in range(len(kmers)):
        kmers[i]=''.join(kmers[i])
        d[kmers[i]]=0
    return d


#from ch01:
def compute_hamming_distance(text1,text2):
    mismatches=0
    for i in range(len(text1)):
        if(text1[i]!=text2[i]): mismatches+=1
    return mismatches


def generate_d_neighbourhood(text,d):
  dict=make_dict(len(text))
  d_neighbourhood=[]
  for key in dict:
    if compute_hamming_distance(text,key)<=d and key not in d_neighbourhood:
      d_neighbourhood.append(key)
  return d_neighbourhood


#BA1n
def motifEnumeration(dna_list,k,d):
    patterns=[]
    patterns2=[]
    for dna in dna_list:
        for i in range(len(dna)-k+1):
            l=generate_d_neighbourhood(dna[i:i+k],d)
        for j in range(len(l)):
            if l[j] not in patterns2: 
                patterns2.append(l[j])
    
    for pat in patterns2:
        count=0
        for i in range(len(dna_list)):
            for p in range(len(dna_list[i])-k+1):
                if compute_hamming_distance(dna_list[i][p:p+k],pat)<=d:
                    count+=1
                    break
        if count==len(dna_list):
            patterns.append(pat)
    patterns=list(dict.fromkeys(patterns)) #removes duplicates
    return patterns


if __name__=="__main__":
    with open("C:/Users/Doris/Downloads/rosalind_ba2a.txt", "r") as f:
        kd=f.readline().strip('\n')
        dna_list = f.read().split()
    k = int(kd.split(' ')[0])
    d=int(kd.split(' ')[1])

    motif_list=motifEnumeration(dna_list,k,d)
    print(*motif_list, ' ', file=open('output.txt','w'))

