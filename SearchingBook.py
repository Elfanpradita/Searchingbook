library = [
    {"title": "Cara menang by one sama python", "author": "Udin Jotos", "year": 2015},
    {"title": "Cara masak ular python", "author": "Udin Jotos", "year": 2017},
    {"title": "Cara mengubah hari kiamat jadi hari senin", "author": "Udin Jotos", "year": 2020},
    {"title": "Cara menang by one sama kominfo", "author": "Cecep Jamsot", "year": 2015},
    {"title": "Cara masak telor python", "author": "Cecep Jamsot", "year": 2017},
    {"title": "Cara mengubah hari kerja jadi hari kiamat", "author": "Cecep Jamsot", "year": 2020},
    {"title": "Cara menang by one sama ibu-ibu", "author": "Abdul Kocok", "year": 2015},
    {"title": "Cara masak telor burung elang", "author": "Abdul Kocok", "year": 2017},
    {"title": "Cara mengubah musim panas menjadi musim durian", "author": "Abdul Kocok", "year": 2020},
    {"title": "Cara menang by one sama polisi tidur", "author": "Agus Usus", "year": 2015},
    {"title": "Cara masak katak gulai", "author": "Agus Usus", "year": 2017},
    {"title": "Cara mengubah dosa jadi saldo kredivo", "author": "Agus Usus", "year": 2020},
    {"title": "Cara menang by one sama bocil madura", "author": "Abdul Ilham", "year": 2015},
    {"title": "Cara masak nasi goreng kuah", "author": "Abdul Ilham", "year": 2017},
    {"title": "Cara mengubah Ryzen menjadi Intel", "author": "Abdul Ilham", "year": 2020}
]

def search_books(keyword, field):
    results = []
    for book in library:
        if keyword.lower() in str(book[field]).lower():
            results.append(book)
    return results

def display_books(books):
    if not books:
        print("Buku yang anda cari tidak ditemukan.")
    else:
        print("Buku yang ditemukan:")
        for book in books:
            print(f"Judul: {book['title']}, Penulis: {book['author']}, Tahun: {book['year']}")

def main():
    while True:
        print("Selamat datang di pencarian buku")
        print("1. Cari berdasarkan judul")
        print("2. Cari berdasarkan penulis")
        print("3. Cari berdasarkan tahun")
        choice = input("Masukkan pilihan anda (1/2/3): ")
        
        if choice == '1':
            keyword = input("Masukkan kata kunci judul buku yang ingin dicari: ")
            field = "title"
        elif choice == '2':
            keyword = input("Masukkan nama penulis yang ingin dicari: ")
            field = "author"
        elif choice == '3':
            keyword = input("Masukkan tahun buku yang ingin dicari: ")
            field = "year"
        else:
            print("Pilihan tidak valid, silakan coba lagi.")
            continue

        results = search_books(keyword, field)
        display_books(results)
        
        lagi = input("Apakah anda ingin mencari data buku yang lain? (Y/N): ")
        if lagi.lower() != 'y':
            break

if __name__ == "__main__":
    main()
