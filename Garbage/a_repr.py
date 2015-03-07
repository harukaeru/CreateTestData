def a_repr(a, i):
 i -= 1
 a = repr(a)
 if i > 0:
  return a_repr(a, i)
 else:
  return a

a = 'a'
print a_repr(a, 3)

