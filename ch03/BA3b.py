#BA3B
#Reconstruct a String from its Genome Path

def reconstruct_genome(patterns):
  genome=''
  for i in range(len(patterns)):
    if i==0: genome+=patterns[i]
    else:
      genome+=patterns[i][-1]
  return genome

if __name__=='__main__':
    patterns=[]
    with open("C:/Users/Doris/Downloads/rosalind_ba3b.txt", "r") as f:
        for line in f.readlines():
            patterns.append(line.strip())
    
    genome=reconstruct_genome(patterns)
    print(genome)