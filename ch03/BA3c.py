#BA3C
#Construct the Overlap Graph of a Collection of k-mers

def overlap_graph(patterns):
    patterns=sorted(patterns)
    dictionary={}

    for p1 in patterns:
        dictionary[p1]=[]

    for pattern in patterns:
        for pat in patterns:
            if pattern!=pat and pattern[1:]==pat[:-1]: dictionary[pattern].append(pat)
    
    return dictionary


if __name__=='__main__':
    patterns=[]
    with open("C:/Users/Doris/Downloads/rosalind_ba3c.txt", "r") as f:
        for line in f.readlines():
            patterns.append(line.strip())
            
    dictionary=overlap_graph(patterns)

    for key in dictionary:
        for j in range(len(dictionary[key])):
            print(key+' -> '+dictionary[key][j])