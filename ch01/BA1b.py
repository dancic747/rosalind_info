#BA1B
#Find the Most Frequent Words in a String


def find_and_count_kmers(text, k):
    kmer_dictionary={}
    for i in range(len(text)-k+1):
        if text[i:i+k] not in kmer_dictionary:
            kmer_dictionary[text[i:i+k]]=1
        else:
            kmer_dictionary[text[i:i+k]]+=1
    return kmer_dictionary


if __name__=="__main__":
    with open("C:/Users/Doris/Downloads/rosalind_ba1b.txt", "r") as f:
        text = f.readline().strip()
        k = int(f.readline().strip())
    
    dict=find_and_count_kmers(text, k)
    max_value_key_list=[]
    max_value=max(dict.values())
    for key in dict:
        if dict[key]==max_value: max_value_key_list.append(key)
    print(*sorted(max_value_key_list), ' ')

