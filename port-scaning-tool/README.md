# Port Tarama Aracı (Port Scanner Tool)

🔍 **Port Tarama Aracı**, sistemlerdeki açık portları tespit etmek için kullanılan bir Python uygulamasıdır.

## Özellikleri

✅ **Kritik Portlar Taraması** - 9 adet tehlikeli portu otomatik analiz eder  
✅ **Genel Port Taraması** - 1-1024 aralığındaki tüm portları tarar  
✅ **Servis Tanımlama** - Açık portlar için servis bilgisi ve güvenlik uyarıları gösterir  
✅ **Hızlı Tarama** - Timeout ayarlanmış socket bağlantıları ile hızlı sonuç  
✅ **Detaylı Rapor** - Tarama sonunda tüm açık portların özet listesi

## Kurulum

```bash
# Projeyi klonlayın
git clone https://github.com/devonicCEO/cyber-security-tools/Port Tarama.git
cd Port-Tarama

# Python 3.6+ gereklidir
python main.py
```

## Kullanım

```bash
python main.py
```

Ardından domain veya IP adresini girin:

```
Domain veya IP: example.com
```

### Tarama Adımları

1. **Kritik Portlar** - FTP, SSH, Telnet, HTTP, HTTPS, SMB, MySQL, RDP, Metasploit gibi önemli portlar ilk olarak taranır
2. **Genel Portlar** - 1-1024 aralığındaki diğer portlar taranır
3. **Sonuç Raporu** - Bulunan açık portlar ve bunların risk seviyeleri gösterilir

## Scanned Portlar Listesi

| Port | Servis     | Risk Seviyesi |
| ---- | ---------- | ------------- |
| 21   | FTP        | Yüksek        |
| 22   | SSH        | Orta          |
| 23   | Telnet     | ⚠️ ÇOK YÜKSEK |
| 80   | HTTP       | Orta          |
| 443  | HTTPS      | Orta          |
| 445  | SMB        | ⚠️ ÇOK YÜKSEK |
| 3306 | MySQL      | Yüksek        |
| 3389 | RDP        | Yüksek        |
| 4444 | Metasploit | Kritik        |

## Güvenlik Notları

⚠️ **Bu araç sadece kendi sistemleriniz veya izniniz olduğu sistemlerde kullanılmalıdır.**

- Başkasının sistemine izinsiz giriş **yasal değildir**
- Ruhsatsız port taraması **siber suça girebilir**
- Sadece eğitim ve kendi sistem yönetimi amaçlı kullanın

## Sistem Gereksinimleri

- Python 3.6 veya üstü
- Windows, macOS veya Linux işletim sistemi
- İnternet bağlantısı

## Lisans

Bu proje MIT Lisansı altında lisanslanmıştır. Detaylar için [LICENSE](LICENSE) dosyasına bakın.

## Katkıda Bulunma

Katkılar açıktır! Lütfen:

1. Fork yapın
2. Feature branch'i açın (`git checkout -b feature/AmazingFeature`)
3. Değişiklikleri commit edin (`git commit -m 'Add some AmazingFeature'`)
4. Branch'e push yapın (`git push origin feature/AmazingFeature`)
5. Pull Request açın

## İletişim

Sorularınız ve önerileriniz için issue açabilirsiniz.

## Uyarı

Bu araç siber güvenlik eğitim amaçlıdır. Kullanıcı tüm yasal sorumlulukları taşır.

---

**Versiyon:** 1.0  
**Son Güncelleme:** 10.06.2026
