sudah_daftar = True
sudah_bayar = False

boleh_ujian = sudah_daftar and sudah_bayar

if boleh_ujian:
    print("Boleh mengikuti ujian")
else:
    print("Tidak boleh mengikuti ujian")