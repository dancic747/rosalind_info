#BA1G
#Compute the Hamming Distance Between Two Strings

def compute_hamming_distance(text1,text2):
    mismatches=0
    for i in range(len(text1)):
        if(text1[i]!=text2[i]): mismatches+=1
    return mismatches


if  __name__=='__main__':
    with open('C:/Users/Doris/Downloads/rosalind_ba1g.txt','r') as f:
        text1=f.readline().strip()
        text2=f.readline().strip()
    hamming_distance=compute_hamming_distance(text1,text2)
    print(hamming_distance)
