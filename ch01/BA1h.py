#BA1H
#Find All Approximate Occurrences of a Pattern in a String

import BA1g

def pattern_matching(text,pattern,max_num_of_mismatches):
    positions=[]
    for i in range(len(text)-len(pattern)+1):
        k=BA1g.compute_hamming_distance(text[i:i+len(pattern)],pattern)
        if(k<=max_num_of_mismatches): positions.append(i)
    return positions


if  __name__=='__main__':
    with open('C:/Users/Doris/Downloads/rosalind_ba1h.txt','r') as f:
        pattern=f.readline().strip()
        text=f.readline().strip()
        max_num_of_mismatches=int(f.readline().strip())
    positions=pattern_matching(text,pattern,max_num_of_mismatches)
    print(*positions,' ')

