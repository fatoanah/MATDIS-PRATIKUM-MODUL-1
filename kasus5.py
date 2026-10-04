uang_tunai = False
saldo_qris = True

bisa_bayar = uang_tunai or saldo_qris

if bisa_bayar:
    print("Bisa membeli makanan")
else:
    print("Tidak bisa membeli makanan")