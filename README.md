# ASL-HandDetection
Tugas Kelompok Kecerdasan Buatan


1. Silahkan clone repo ini terlebih dahulu
2. Ekstrak file train.zip
3. Konfigurasi ulang path setiap file.py dan file.ipynb yang tersedia sesuai lokasi penyimpanan ekstrasi train.zip


Sebelum mulai :
1. Pastikan anda sudah melakukan virtual enviroment terlebih dahulu
2. Mengaktifkan vitrual enviroment nya
3. Baru menginstall library yang di butuhkan


Pada file vs_CodeNN.ipynb :
1. Pastikan sudah masuk kedalam virtual enviroment python
2. Instalasi ilbrary ultralytics dengan cara 
```console
(venv):~$ pip install ultralytics
```
3. Run setiap bagian kolom nya
4. Buka file data.yaml dan sesuaikan path folder penyimpanan train/images nya
5. Run seluruh kolom yang ada
6. Bagian ini untuk mengtraining ulang data yang sudah ada
(Bisa di skip jika menggunakan model yang default)


Pada file pridect.py dan live.py :
1. Pastikan mengubah bagian ini sesuai dengan path penyimpanan anda
```console
model_path = '../ASL-HandDetection/beste11.pt'
```
2. Untuk bagian file pridect.py, kalian bisa mengubah path folder penyimpanan video nya.
```console
model.predict(source="../ASL-HandDetection/TestVideoASL.mp4", show=True, conf=0.5)
```
3. Jika ingin mengubah file .pt sesuai dengan hasil tarining sendiri, bisa mencari file nya di folder weight yang di generate setelah training data


Selamat Mencoba

