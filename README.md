# CARA PAKAI APLIKASI

### STEP 1 Install requirements
---
1. Buka terminal di vscode (pastiin directory udah betul)
2. Run `pip install -r requirements.txt`

### STEP 2 Setting Database
---
1. Pastikan udah install mongodb (karena database yg dipakai mongodb)
2. Install juga mongodb Compass
3. Connect ke mongodb
    * Buka mongodb Compass
    ![mongodbCompass](static\img\ss1.PNG)
    * klik connect

### STEP 3 Migration Database
---
1. Buka terminal di vscode (pastiin directory udah betul)
2. Run `py manage.py makemigrations` atau `python manage.py makemigrations` terus tunggu sampai selesai
3. Run `py manage.py migrate` tunggu juga sampai selesai

### STEP 4 Buat Akun Admin
---
1. Buka terminal di vscode (pastiin directory udah betul)
2. Run `py manage.py createsuperuser` atau `python manage.py createsuperuser` terus buat nama, email sama passwordnya. Contoh dibawah.
    * ![createuser](static\img\ss2.PNG)
    * *NOTE password emang ga kelihatan

### STEP 5 Jalanin Aplikasi
---
1. Buka terminal di vscode (pastiin directory udah betul)
2. Run `py manage.py runserver` atau `python manage.py runserver`
3. Buka http://127.0.0.1:8000/

## SELESAI
