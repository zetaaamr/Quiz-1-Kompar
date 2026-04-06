import multiprocessing
import time

# TUGAS 1: Menghitung Faktorial
def hitung_faktorial(n):
    print(f"[Task 1 - Faktorial] Memulai perhitungan faktorial untuk {n}...")
    hasil = 1
    for i in range(1, n + 1):
        hasil *= i
        time.sleep(0.2) # Simulasi proses komputasi agar terlihat berjalan paralel
    print(f"[Task 1 - Faktorial] Selesai. Faktorial dari {n} adalah {hasil}")

# TUGAS 2: Menghitung Jumlah Kuadrat
def hitung_jumlah_kuadrat(n):
    print(f"[Task 2 - Kuadrat] Memulai perhitungan jumlah kuadrat 1 sampai {n}...")
    hasil = 0
    for i in range(1, n + 1):
        hasil += (i * i)
        time.sleep(0.3) # Waktu simulasi berbeda untuk menunjukkan task independen
    print(f"[Task 2 - Kuadrat] Selesai. Jumlah kuadrat 1 sampai {n} adalah {hasil}")

if __name__ == "__main__":
    print("=== IMPLEMENTASI TASK PARALLELISM ===")
    print("Menjalankan DUA TUGAS BERBEDA secara bersamaan...\n")
    
    # Inisialisasi dua proses dengan target fungsi yang berbeda (Task Parallelism)
    proses1 = multiprocessing.Process(target=hitung_faktorial, args=(5,))
    proses2 = multiprocessing.Process(target=hitung_jumlah_kuadrat, args=(5,))
    
    # Memulai eksekusi kedua tugas secara bersamaan
    proses1.start()
    proses2.start()
    
    # Menunggu kedua tugas selesai dieksekusi sebelum program utama berhenti
    proses1.join()
    proses2.join()
    
    print("\n=== SEMUA TUGAS SUDAH SELESAI DIEKSEKUSI ===")