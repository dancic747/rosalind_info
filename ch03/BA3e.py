#BA3E
#

def deBruijn(patterns):
    dictionary={}
    for p1 in patterns:
        prefix=p1[:-1]
        if prefix not in dictionary: dictionary[prefix]=[]
 
    for pattern in patterns:
        for key in dictionary:
            if key==pattern[:-1]: dictionary[key].append(pattern[1:])

    return dictionary
  

if __name__=='__main__':
    patterns=[]
    with open("C:/Users/Doris/Downloads/rosalind_ba3e.txt", "r") as f:
        for line in f.readlines():
            patterns.append(line.strip())
    
    dictionary=deBruijn(patterns)

    for key in sorted(dictionary.keys()):
        if len(dictionary[key])>0:
            print(key+' -> '+ ','.join(sorted(dictionary[key])),file=open('output.txt','a'))
