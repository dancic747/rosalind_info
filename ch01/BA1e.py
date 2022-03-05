#BA1E
#Find Patterns Forming Clumps in a String

import BA1b

def patterns_forming_clumps(k,L,t,text):
    patterns_forming_clumps_list=[]
    for j in range(len(text)-L+1):
        dict=BA1b.find_and_count_kmers(text[j:j+L],k)
        for key in dict:
            if(dict[key]>=t and key not in patterns_forming_clumps_list):patterns_forming_clumps_list.append(key)
    return patterns_forming_clumps_list





if __name__=='__main__':
    # with open('C:/Users/Doris/Downloads/rosalind_ba1e.txt','r') as f:
    #     text=f.readline().strip()
    #     num_params=f.readline().strip()
    #     k=num_params.split(' ')[0]
    #     L=num_params.split(' ')[1]
    #     t=num_params.split(' ')[2]
    text='CGGACTCGACAGATGTGAAGAAATGTGAAGACTGAGTGAAGAGAAGAGGAAACACGACACGACATTGCGACATAATGTACGAATGTAATGTGCCTATGGC'
    k=5
    L=75
    t=4
    patterns_forming_clumps_list=patterns_forming_clumps(k,L,t,text)
    print(*sorted(patterns_forming_clumps_list), ' ')