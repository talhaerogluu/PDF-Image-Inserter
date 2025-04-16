import fitz  # PyMuPDF

# --- Dosyalar ---
pdf_path = "is-yeri-uygulama-egitimi-ara-raporu-14176TR.pdf"   # Üzerine resim eklenecek PDF
output_path = "sonuc.pdf"                          # Sonuç PDF
image_path = "archmirimza.jpg"                     # Eklenecek imza/kaşe görseli

# --- Ayarlar ---
sayfa_numarasi = 0
x = 430          # Sol kenar
y = 640          # Alt kenar
genislik = 120   # Genişlik
yukseklik = 65   # Yükseklik

# --- PDF aç ve düzenle ---
doc = fitz.open(pdf_path)
sayfa = doc[sayfa_numarasi]

# Resim yerleştirilecek alan
rect = fitz.Rect(x, y, x + genislik, y + yukseklik)

# Resmi ekle
sayfa.insert_image(rect, filename=image_path)

# Kaydet
doc.save(output_path)
doc.close()

print("✅ Resim eklendi ve kaydedildi:", output_path)