# FOTOKITABLUUUUUUUUUUUR 🎥✌️

Hand gesture detection dengan blur otomatis saat menunjukkan peace sign menggunakan dua tangan.

## 📋 Deskripsi

Program ini menggunakan MediaPipe untuk mendeteksi tangan dan jari secara real-time dari webcam. Ketika kedua tangan menunjukkan peace sign (✌️) secara bersamaan, kamera akan blur secara otomatis.

### Fitur:
- ✅ Deteksi 2 tangan secara bersamaan
- ✅ Pengenalan gesture peace sign (telunjuk + tengah terbuka)
- ✅ Blur otomatis saat kondisi terpenuhi
- ✅ Visualisasi landmark tangan di frame
- ✅ Display status deteksi real-time

## 🛠️ Instalasi

### 1. Prasyarat
- Python 3.7 atau lebih tinggi
- Webcam yang terhubung

### 2. Clone Repository
```bash
git clone https://github.com/Cheszyalsohere/FOTOKITABLUUUUUUUUUUUR.git
cd FOTOKITABLUUUUUUUUUUUR
```

### 3. Install Dependencies
```bash
pip install opencv-python mediapipe
```

Atau jika menggunakan `requirements.txt`:
```bash
pip install -r requirements.txt
```

## ▶️ Cara Menjalankan

```bash
python main.py
```

Program akan membuka webcam dan menampilkan feed kamera dengan:
- **Skeleton tangan** — garis yang menghubungkan landmark jari
- **Status deteksi** — menampilkan jumlah tangan terdeteksi dan berapa banyak yang membuat peace sign
- **Blur otomatis** — frame di-blur saat kedua tangan membuat peace sign

### Kontrol:
- **Q** — Keluar dari program

## 🎮 Cara Menggunakan

1. Jalankan program
2. Tunjukkan satu atau dua tangan ke webcam
3. Buat gesture **peace sign** (✌️) dengan kedua tangan:
   - Telunjuk dan tengah **TERBUKA**
   - Manis dan kelingking **TERTUTUP**
   - Jempol bisa dalam posisi apa saja
4. Ketika kedua tangan membuat peace sign, kamera akan **blur**

## 🔧 Teknologi

- **OpenCV** — Video capture dan image processing
- **MediaPipe** — Hand tracking dan landmark detection
- **Python** — Bahasa pemrograman

## 📝 Penjelasan Kode

### `is_finger_extended(landmarks, tip_idx, pip_idx, wrist)`
Mengecek apakah sebuah jari dalam keadaan terbuka dengan membandingkan jarak dari tip jari ke wrist dengan jarak PIP (Proximal Interphalangeal) ke wrist.

### `is_peace_sign(hand_landmarks)`
Mendeteksi apakah tangan membuat peace sign:
- Telunjuk terbuka (extended)
- Tengah terbuka (extended)
- Manis tertutup (not extended)
- Kelingking tertutup (not extended)

### Loop Utama
Setiap frame:
1. Baca frame dari webcam
2. Flip frame (mirror mode)
3. Deteksi tangan dengan MediaPipe
4. Gambar landmark tangan
5. Cek peace sign per tangan
6. Blur jika kedua tangan peace sign
7. Tampilkan frame

## ⚙️ Konfigurasi

Di `main.py`, Anda bisa mengubah:

```python
# Confidence threshold untuk deteksi
min_detection_confidence=0.5  # 0-1, lebih rendah = lebih sensitif
min_tracking_confidence=0.5   # 0-1, lebih rendah = lebih sensitif

# Model complexity (0=lite, 1=full)
model_complexity=1
```

## 🐛 Troubleshooting

### "No hand detected"
- Pastikan tangan berada di dalam frame
- Cukupkan pencahayaan
- Jangan gerakin tangan terlalu cepat

### Deteksi jari tidak akurat
- Kalibrasi kamera sehingga sudut pandang optimal
- Pastikan tangan tidak terlalu jauh dari kamera
- Coba turunkan nilai `min_detection_confidence`

### Blur tidak trigger
- Pastikan kedua tangan terdeteksi (lihat status di frame)
- Buat peace sign dengan jelas (telunjuk + tengah harus benar-benar terbuka)
- Tahan gesture selama minimal 1-2 frame

## 📄 Lisensi

MIT License

## 👤 Author

Cheszyalsohere

---

**Tips:** Untuk hasil terbaik, gunakan di tempat yang cukup cahaya dan posisikan kamera pada level mata. 📷
