#BA1N
#Generate the d-Neighborhood of a String

import BA1g
import itertools

def make_dict(k):
    d={}
    kmers=list(itertools.product(['A','T','G','C'], repeat=k))
    for i in range(len(kmers)):
        kmers[i]=''.join(kmers[i])
        d[kmers[i]]=0
    return d


def generate_d_neighbourhood(text,d):
  dict=make_dict(len(text))
  d_neighbourhood=[]
  for key in dict:
    if BA1g.compute_hamming_distance(text,key)<=d and key not in d_neighbourhood:
      d_neighbourhood.append(key)
  return d_neighbourhood


if __name__=="__main__":
    with open("C:/Users/Doris/Downloads/rosalind_ba1n.txt", "r") as f:
        pattern=f.readline().strip()
        d=int(f.readline().strip())

    d_neighbourhood=generate_d_neighbourhood(pattern,d)
    for neighbour in d_neighbourhood:
        print(neighbour, file=open('output.txt','a'))