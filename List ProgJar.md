[Membuat FTP Server dan Klien]
Ketentuannya adalah mengimplementasikan RFC 959 (dituliskan dengan subbab) sebagai berikut
- Membuat aplikasi FTP klien dan server
- Autentikasi (USER dan PASS: 4.1.1) (sudah)
- Mengubah direktori aktif (CWD: 4.1.1) (sudah)
- Keluar aplikasi (QUIT: 4.1.1) (sudah)
- Unduh (RETR: 4.1.3)
- Unggah (STOR: 4.1.3)
- Mengganti nama file (RNTO: 4.1.3) (sudah)
- Menghapus file (DELE: 4.1.3) (sudah)
- Menghapus direktori (RMD: 4.1.3) (sudah)
- Membuat direktori (MKD: 4.1.3) (sudah)
- Mencetak direktori aktif (PWD: 4.1.3) (sudah)
- Mendaftar file dan direktori (LIST: 4.1.3) (sudah)
- HELP: 4.1.3
- Reply codes (200, 500, 202, 230, 530: 4.2.1)
- Menerapkan teknik multiclient dengan modul select DAN thread (sudah)