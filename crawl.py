import requests
import time
import sys

def loading_effect():
    loading_text = "loading"
    while True:
        for i in range(20):
            sys.stdout.write(f"\r{loading_text}{'.' * i}")
            sys.stdout.flush()
            time.sleep(1)
        sys.stdout.write("\r")
        break

def get_archive_data(domain):
    # Format URL untuk melakukan request ke web.archive.org
    url = f'https://web.archive.org/cdx/search/cdx?url=*.{domain}/&collapse=urlkey&output=text&fl=original'
    
    # Menampilkan efek "loading..."
    loading_effect()
    
    # Mengirim permintaan HTTP GET
    response = requests.get(url)
    
    if response.status_code == 200:
        # Menampilkan hasil jika request berhasil
        print("""
PAUN HACK
V1.0
by : paun
""")
        print(f"Masukkan domain: {domain}")
        print("Hasil dari Web Archive:")
        print(response.text)

        # Menanyakan apakah ingin menyimpan hasil
        save_option = input("\nApakah ingin menyimpan hasil ini? (yes/no): ").strip().lower()
        if save_option == "yes":
            file_name = input("Masukkan nama file untuk menyimpan hasil (tanpa ekstensi): ") + ".txt"
            with open(file_name, "w") as file:
                file.write(response.text)
            print(f"Data berhasil disimpan dalam file: {file_name}")
        else:
            print("Data tidak disimpan.")
    else:
        print("Terjadi kesalahan saat mengakses Web Archive.")

def main():
    # Menampilkan ASCII art "PAUN HACK" yang sudah dicopy
    print("""


██████╗  █████╗ ██╗   ██╗███╗   ██╗    ██╗  ██╗ █████╗  ██████╗██╗  ██╗
██╔══██╗██╔══██╗██║   ██║████╗  ██║    ██║  ██║██╔══██╗██╔════╝██║ ██╔╝
██████╔╝███████║██║   ██║██╔██╗ ██║    ███████║███████║██║     █████╔╝ 
██╔═══╝ ██╔══██║██║   ██║██║╚██╗██║    ██╔══██║██╔══██║██║     ██╔═██╗ 
██║     ██║  ██║╚██████╔╝██║ ╚████║    ██║  ██║██║  ██║╚██████╗██║  ██╗
╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝    ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝
                                                                       
""")
    
    print("V 1.0")
    print("By paun\n")
    
    # Meminta input domain dari pengguna
    domain = input("Masukkan domain: ")
    
    # Mendapatkan data dari web.archive.org berdasarkan domain yang dimasukkan
    get_archive_data(domain)

if __name__ == "__main__":
    main()
