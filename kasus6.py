ada_pulsa = False
ada_wifi = True

bisa_chat = ada_pulsa or ada_wifi

if bisa_chat:
    print("Bisa menghubungi teman")
else:
    print("Tidak bisa menghubungi teman")