def tpl(x):
  """
  output: tpl returns thrice its input
  input x: a number (int or float)
  """
  return 3*x
print 'tpl(3) is', tpl(3)

def sq(x):

    return 4*x
print 'sq(4) is', sq(4)



def interp(low,hi,fraction):
  """
  :param low: the lower input
  :param hi: the higher the input
  :param fraction: the fraction of the way beween the high and the low
  :return the difference between hi and low multiplied by the fraction. This output is added to the low.
  """
  return (hi-low)*(fraction)+low
print interp(1.0,9.0,0.25)

def checkends(word):
    if word[0] == word[-1]:
        return True
    else:
        return False

def flipside(word):
    length = len(word)
    if length %2 == 0:
        return word[length/2:]+word[length/2]
else: 


