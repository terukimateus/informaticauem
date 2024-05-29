notas = [10.0,7.0,8.0,9.0,10.0]

media = 0

for num in notas:
    if num >= 9.0:
        media = media + 1

if media > ((len(notas)/3)*2):
    print('True')
else:
    print('False')