def fpb(a,b):
    if a<b:
        smaller=a
    else:
        smaller=b
    for i in range (1,smaller+1):
        if a%i==0 and b%i==0:
            fpb=i
        # else:
        #     continue
    return fpb

def kpk(a,b):
    kpk=int(a*b/fpb(a,b))
    return kpk

a=int(input('Masukkan angka pertama : '))
b=int(input('Masukkan angka kedua   : '))

print('FPB dari ',a,' dan ',b,' adalah ',fpb(a,b))
print('KPK dari ',a,' dan ',b,' adalah ',kpk(a,b))