#BA1F
#Find a Position in a Genome Minimizing the Skew

def compute_skew(text):
    countC=0
    countG=0
    for i in range(len(text)):
        if text[i]=='C': countC+=1
        if text[i]=='G': countG+=1
    skew=countG-countC
    return skew


def find_min_skew_positions(text):
    skew=[]
    min_skew_positions=[]
    for i in range(len(text)):
        skew.append(compute_skew(text[:i:1]))
    min_skew=min(skew)
    for i in range(len(skew)):
        if (skew[i]==min_skew): min_skew_positions.append(i)
    return min_skew_positions


if __name__=='__main__':
    with open('C:/Users/Doris/Downloads/rosalind_ba1f.txt','r') as f:
        text=f.readline().strip()
    min_skew_positions=find_min_skew_positions(text)
    print(*min_skew_positions,' ')