import random
import datetime

# Struktur data untuk menyimpan tugas
tasks = []

def add_task():
    task_name = input("Masukkan nama tugas: ")
    deadline = input("Masukkan deadline (YYYY-MM-DD): ")
    task_id = random.randint(100, 999)  # Membuat ID acak untuk tugas
    tasks.append({"id": task_id, "task": task_name, "deadline": deadline})
    print(f"Tugas '{task_name}' berhasil ditambahkan dengan ID {task_id}\n")

def view_tasks():
    if not tasks:
        print("Tidak ada tugas yang tersedia.\n")
        return
    print("Daftar Tugas:")
    for task in tasks:
        print(f"ID: {task['id']}, Tugas: {task['task']}, Deadline: {task['deadline']}")
    print("")

def delete_task():
    task_id = int(input("Masukkan ID tugas yang ingin dihapus: "))
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            print(f"Tugas dengan ID {task_id} berhasil dihapus.\n")
            return
    print("Tugas tidak ditemukan.\n")

def main():
    while True:
        print("\nMenu:")
        print("1. Tambah Tugas")
        print("2. Lihat Daftar Tugas")
        print("3. Hapus Tugas")
        print("4. Keluar")
        
        choice = input("Pilih menu (1-4): ")
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid, coba lagi.\n")

if __name__ == "__main__":
    main()
