#BA1M
#

def number_to_symbol(num):
  if num==0: symbol='A'
  elif num==1: symbol='C'
  elif num==2: symbol='G'
  else: symbol='T'
  return symbol


def number_to_pattern(ind,k):
  if k==1:
    symbol=number_to_symbol(ind)
    return symbol
  prefix_index=ind//4
  r=ind%4
  symbol=number_to_symbol(r)
  prefix_pattern=number_to_pattern(prefix_index,k-1)
  word=prefix_pattern+symbol
  return word


if __name__=="__main__":
    with open("C:/Users/Doris/Downloads/rosalind_ba1m.txt", "r") as f:
        index = int(f.readline().strip())
        k=int(f.readline().strip())

    word=number_to_pattern(index,k)
    print(word)