#BA3D
#Construct the De Bruijn Graph of a String

def deBruijn(k, text):
    dictionary={}
    for i in range(len(text)-k+1):
        pattern_prefix=text[i:i+k-1]
        pattern_sufix=text[i+1:i+k]

        if pattern_prefix not in dictionary: dictionary[pattern_prefix]=[pattern_sufix]
        else: dictionary[pattern_prefix].append(pattern_sufix)
    
    return dictionary


if __name__=='__main__':
    with open("C:/Users/Doris/Downloads/rosalind_ba3d (1).txt", "r") as f:
        k = int(f.readline().strip())
        text = f.readline().strip()
    
    dictionary=deBruijn(k,text)
    for key in sorted(dictionary.keys()):
        print(key + ' -> ' +  ','.join(dictionary[key]),file=open('output.txt','a'))
