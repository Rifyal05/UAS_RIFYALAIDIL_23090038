# 2D array
array = [[90, 50, 60], [80, 60, 70]]
rata_rata = sum(sum(row)
    for row in array) / (len(array) * len(array[0]))

print(f'jumlah nilai : {len(array[0])+len(array[1])}')
print(f'nilai algoritma : {array[0]}')
print(f'nilai matematika : {array[1]}')
print("Rata-rata :", rata_rata)