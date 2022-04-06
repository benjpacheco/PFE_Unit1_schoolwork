#Name: Benyir J Pacheco
#Email: benyir.pacheco60@myhunter.cuny.edu.

nameList = ['WILL', 'JACK', 'SLADE', 'STEW', 'BENYIR']
surList = ['WILLIAMS', 'JACKSON', 'STEWART', 'PACHECO']
for name in nameList:
    print(name)
print('---')
for sur in surList:
    print(sur)
print('---')
for name in nameList:
    for sur in surList:
        print(name, sur)
print('---')
for name in nameList:
    for sur in surList:
        if name in sur:
            print(name, sur)

