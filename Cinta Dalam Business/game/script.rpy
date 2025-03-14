﻿# Skrip permainan masuk ke dalam fail ini.

# Isytiharkan watak yang digunakan dalam permainan ini.
# Argumen color mewarnakan nama watak.

define e = Character("Eileen")


# Permainan bermula di sini.

label start:

    # Tunjukkan latar belakang. Ini menggunakan sandaran secara lalainya,
    # namun anda boleh menambah fail (dinamakan "bg room.png" atau "bg room.jpg")
    # ke direktori images untuk menunjukkannya.

    scene bg room

    # Ini menunjukkan peperi watak. Sandaran digunakan, tetapi anda boleh
    # menggantikannya dengan menambah fail bernama "eileen happy.png"
    # ke dalam direktori images.

    show eileen happy

    # Ini memaparkan baris dialog.

    e "Anda telah mencipta sebuah permainan Ren'Py baru."

    e "Setelah anda menambah cerita, gambar, dan muzik, anda boleh menerbitkannya untuk semua!"

    # Ini menamatkan permainan.

    return
