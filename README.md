# UTS-KecerdasanBuatan
Sistem Pakar Diagnosa Penyakit Tanaman
Sistem pakar sederhana berbasis aturan (rule-based system) untuk mendiagnosis penyakit dan serangan hama pada tanaman berdasarkan gejala yang diamati.

Fitur
Diagnosa tanaman berdasarkan 4 gejala utama:
Daun menguning
Bercak hitam
Daun berlubang
Tanaman layu
Memberikan hasil diagnosis:
Kekurangan nutrisi
Busuk akar
Serangan ulat
Penyakit bintik daun
Serangan thrips
Kondisi tanaman sehat
Pesan jika gejala tidak sesuai data

Langkah Pengerjaan
Identifikasi Gejala
Tentukan gejala tanaman yang sering muncul seperti daun menguning, bercak hitam, dll.
Membangun Basis Pengetahuan
Setiap kombinasi gejala dibuat menjadi aturan (Rule) menggunakan library experta.
Membuat Input User
Program meminta pengguna untuk menjawab pertanyaan "yes" atau "no" untuk setiap gejala.
Proses Inferensi
Gejala pengguna dikonversi menjadi fakta (Fact) di dalam engine Diagnosis.
experta mencocokkan fakta dengan aturan untuk menghasilkan diagnosis.
Memberikan Output
Menampilkan hasil diagnosis ke pengguna.
Penanganan Kasus Tidak Sesuai
Jika tidak ada aturan yang cocok, program akan menampilkan pesan default.
