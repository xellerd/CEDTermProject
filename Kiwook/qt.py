class test:
    element = 0

one = test()
two = one
two.element = 2

print(one.element)
print(two.element)
