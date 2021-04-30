def luas(x): 
    return 22/7*x**2 
print(luas(7)) 

def keliling(x): 
    return 22/7*2*x
print(keliling(7)) 

print("====================")
#dengan input
def menghitung_lingkaran(r):
    phi = 22/7
    L = phi*r*r
    K = phi*(r*2)
    return L,K

r = int(input("Masukkan jari-jari : "))
lingkaran = menghitung_lingkaran(r)
# print(lingkaran)
text = "Luas lingkaran adalah {:.2f} cm\u00b2 dan keliling lingkaran adalah {:.2f} cm".format(lingkaran[0],lingkaran[1])
print(text)