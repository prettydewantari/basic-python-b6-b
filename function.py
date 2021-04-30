def sapa():
    print("Hallo gaes!")

def say_hay():
    print("Hallo juga")

def tanya_kabar():
    print("Gimana kabarmu ?")

def perkenalan(nama,umur):
    print("Nama saya adalah "+nama)
    print("Umur saya adalah {}".format(umur))
    #print("Umur saya adalah "+umur) kenapa ya?? ga bisa kalo pake "+"??

nama = input("Masukkan nama kamu : ")
umur = int(input("Masukkan umur kamu : "))
perkenalan(nama,umur)

#perkenalan(umur = "20", nama="pretty")

# print("Hai bro")
# jawab = int(input("Masukkan Jawaban !"))
# if (jawab == 1):
#     sapa()
# elif (jawab == 2):
#     say_hay()
# elif (jawab == 3):
#     tanya_kabar()