def greet(name):
    """
    This function greets to
    the person passed in as
    a parameter
    """
    print("Hello, " + name + ". Good morning!")

greet('Paul')

def perkenalan(nama,umur):
    print("Nama saya adalah "+nama)
    print("Umur saya adalah "+umur)

nama = input("Masukkan nama kamu : ")
umur = int(input("Masukkan umur kamu : "))
perkenalan(nama,umur)
#perkenalan(nama,umur)
#perkenalan(umur = "20", nama="pretty")