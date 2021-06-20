# Algoritma Unsupervised Learning
Algoritma *unsupervised learning* adalah algoritma yang membantu dalam mengambil keputusan berdasarkan input yang didapatkan sebelumnya, tetapi tanpa label.

# Cara menjalankan
Pastikan komputer Anda memiliki Python dengan versi 3.9.2 ke atas. Pastikan juga Anda telah memasang pustaka `matplotlib`. Selain itu, siapkan data CSV yang ingin diuji dengan syarat setidaknya memiliki dua kolom dengan nilai bilangan real.

Kemudian, pada terminal, jalankan salah satu dari perintah berikut untuk menggunakan, bergantung pada algoritma yang ingin digunakan:
```
py main.py --data <nama atau direktori ke data> --dbscan --eps <nilai epsilon> --min_pts <nilai titik minimum> --x <nama kolom x yang digunakan> --y <nama kolom y yang digunakan>
py main.py --data <nama atau direktori ke data> --kmeans --k <nilai k> --x <nama kolom x yang digunakan> --y <nama kolom y yang digunakan>
py main.py --data <nama atau direktori ke data> --kmedoids --k <nilai k> --x <nama kolom x yang digunakan> --y <nama kolom y yang digunakan>
```
Sebagai contoh:
```
py main.py --data beavers.csv --dbscan --min_pts 20 --eps .5 --x temp --y time
```
Opsi ``--x`` dan ``--y`` adalah opsional. Jika tidak ada, kolom pertama dan kedua akan digunakan.

# Pembuat
M. Abdi Haryadi. H (13519156)