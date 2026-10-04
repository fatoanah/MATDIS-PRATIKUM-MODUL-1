naik_motor = True
naik_bus = False

bisa_pergi = naik_motor or naik_bus

if bisa_pergi:
    print("Bisa pergi ke kampus")
else:
    print("Tidak bisa pergi")