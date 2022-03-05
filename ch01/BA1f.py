#BA1F
#Find a Position in a Genome Minimizing the Skew


def find_min_skew_positions(text):
    skew=0
    all_skews=[]
    all_skews.append(skew)
    for i in range(len(text)):
        if(text[i]=='C'): skew-=1
        elif (text[i]=='G'): skew+=1
        all_skews.append(skew)
    min_skew=min(all_skews)
    min_skew_positions=[]
    for j in range(len(all_skews)):
        if(all_skews[j]==min_skew): min_skew_positions.append(j)
    return min_skew_positions
    

if __name__=='__main__':
    with open('C:/Users/Doris/Downloads/rosalind_ba1f.txt','r') as f:
        text=f.readline().strip()
    min_skew_positions=find_min_skew_positions(text)
    print(*min_skew_positions,' ')

    