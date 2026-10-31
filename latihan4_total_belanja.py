# Program menghitung total belanja

nama_barang = str(input("Masukkan nama barang: "))
harga_satuan = float(input("Masukkan harga barang: "))
jumlah_barang = int(input("Masukkan jumlah barang: "))

subtotal = harga_satuan * jumlah_barang
PPN = subtotal * 0.11
total_bayar = subtotal + PPN

print(f"Subtotal dari barang ini {nama_barang}: {subtotal}")
print(f"PPN (11%): {PPN}")
print(f"Total yang harus dibayar: {total_bayar}")