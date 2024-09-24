# Permalink Fixer (Kalıcı Bağlantı Düzeltici)

Permalink Fixer, Türkçe metinleri SEO dostu ve URL'lerde kullanılabilir formata dönüştüren bir Python programıdır. Bu araç, özellikle blog yazıları, haber başlıkları veya ürün isimleri gibi metinleri içeren web siteleri için idealdir.

## Özellikler / Features

- Türkçe karakterleri Latin eşdeğerleriyle değiştirir / Replaces Turkish characters with their Latin equivalents
- Metni küçük harfe çevirir / Converts text to lowercase
- Aksanlı karakterleri kaldırır / Removes accented characters
- Yılları ve belirli kelimeleri (ay isimleri, "fiyat", "tarih" vb.) kaldırır / Removes years and specific words (month names, "price", "date", etc.)
- Alfanümerik olmayan karakterleri tire ile değiştirir / Replaces non-alphanumeric characters with hyphens
- Birden fazla tireyi tek tire ile değiştirir / Replaces multiple hyphens with a single hyphen

## Kullanım / Usage

1. Programı çalıştırın / Run the program:
   ```
   python permalinkfixer.py
   ```

2. Program, örnek metinler üzerinde çalışacak ve sonuçları gösterecektir / The program will run on sample texts and display the results.

3. Kendi metinlerinizi işlemek için, `test_strings` listesini `permalinkfixer.py` dosyasında düzenleyin / To process your own texts, edit the `test_strings` list in the `permalinkfixer.py` file.

## Örnek / Example

```python
Original / Orijinal: Ada Kent Üniversitesi Eğitim Ücretleri: Burs İmkânları 2023-2024
Normalized / Normalize edilmiş: ada-kent-universitesi-egitim-ucretleri-burs-imkanlari

Original / Orijinal: İstanbul'da 2023'te Açılan Yeni Restoranlar
Normalized / Normalize edilmiş: istanbul-da-acilan-yeni-restoranlar
```

## Katkıda Bulunma / Contributing

Katkılarınızı bekliyoruz! Lütfen bir çekme isteği göndermeden önce değişikliklerinizi tartışmak için bir konu açın.

We welcome contributions! Please open an issue to discuss your changes before submitting a pull request.

## Lisans / License

Bu proje MIT lisansı altında lisanslanmıştır. Detaylar için `LICENSE` dosyasına bakın.

This project is licensed under the MIT License. See the `LICENSE` file for details.
