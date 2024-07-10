data = []
while True:
    nim = int(input('masukan nim : '))
    nama = input('masukan nama : ')
    data.append([nim,nama])

    print('ingin tambah lagi ? : ')
    jawab = input('y/n :')
    if jawab == 'y':
        continue
    else:
        print('terimakasih')
        break