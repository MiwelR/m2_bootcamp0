from funciones1nivel import sumaTodos

# Lambda puede definirse en variable:
'''
triple = lambda x: x*3
print(sumaTodos(3, triple))
'''
print(sumaTodos(3, lambda x: x*2))
print(sumaTodos(100, lambda x: x*3))



