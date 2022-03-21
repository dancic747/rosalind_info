#BA1L
#Implement PatternToNumber

def last_symbol(text):
  return text[-1]


def text_prefix(text):
  text=text[:len(text)-1]
  return text


def symbol_to_number(symbol):
  if symbol=='A': number=0
  elif symbol=='C': number=1
  elif symbol=='G': number=2
  else: number=3
  return number


def pattern_to_number(pattern):
  if len(pattern)==0: return 0
  symbol=last_symbol(pattern)
  prefix=text_prefix(pattern)
  x=4*pattern_to_number(prefix)+symbol_to_number(symbol)
  return x


if __name__=="__main__":
    with open("C:/Users/Doris/Downloads/rosalind_ba1l.txt", "r") as f:
        pattern = f.readline().strip()

    x=pattern_to_number(pattern)
    print(x)