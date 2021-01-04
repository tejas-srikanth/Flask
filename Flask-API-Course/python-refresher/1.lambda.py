sequence = [1,3,5,9]
print(list(map( lambda x: x*2, sequence )))
print([(lambda x: x*2)(x) for x in sequence])