import socket
import time
import sys

target_ports = {
    21: "FTP - Zayıf şifreleme, Brute Force ve Anonim Giriş riski.",
    22: "SSH - Uzaktan yönetim; kaba kuvvet saldırıları ve eski versiyon açıkları.",
    23: "Telnet - Çok yüksek risk! Veriler şifrelenmeden (clear-text) gönderilir.",
    80: "HTTP - Web servisi; SQL Injection, XSS ve LFI açıkları taranmalı.",
    443: "HTTPS - SSL/TLS sertifika zafiyetleri ve Heartbleed riski.",
    445: "SMB - WannaCry/EternalBlue gibi fidye yazılımlarının ana giriş kapısı!",
    3306: "MySQL - Veritabanı; dışarıya açıksa SQL yetki yükseltme saldırıları.",
    3389: "RDP - Uzak Masaüstü; BlueKeep zafiyeti ve kaba kuvvet riski.",
    4444: "Metasploit - Muhtemel bir Backdoor (Arka Kapı) veya Payload belirtisi!"
}

print("===================================")
print("=   devonicCEO Port Tarama v1.0   =")
print("===================================")

ip = input("Domain veya IP: ")

time.sleep(2)
print(" ")

open_ports = []

ports = [21, 22, 23, 25, 53, 80, 110, 443, 445, 3306, 3389, 4444, 8080, 8443, 31337, 6667]


chars = ["/", "-", "\\", "|"]
for i in range(20):
    sys.stdout.write(f"\rKritik Portlar Taraniyor.. {chars[i % len(chars)]}")
    sys.stdout.flush()
    time.sleep(0.1)
print(" ")


for port, info in target_ports.items():
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    
    result = s.connect_ex((ip, port))
    
    if result == 0:
        print(f"[!] PORT {port} AÇIK! ⚠️")
        print(f"    --> Servis: {info}")
        open_ports.append(port)
        print("-" * 40)
    else:
        print(f"[-] Port {port} kapalı.")
        pass
        
    


print(" ")
chars = ["/", "-", "\\", "|"]
for i in range(20):
    sys.stdout.write(f"\rGenel Portlar Taraniyor.. {chars[i % len(chars)]}")
    sys.stdout.flush()
    time.sleep(0.1)
print(" ")

for ports in range(1,1025):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.1)
    sonuc = s.connect_ex((ip,ports))

    if sonuc == 0:
        print(f"[!] PORT {ports} AÇIK! ⚠️")
        open_ports.append(ports)
    else:
        print(f"[-] Port {ports} kapalı.")
        pass

    s.close()

print("\n" + "="*35)
print("          TARAMA TAMAMLANDI       ")
print("="*35)

if open_ports:
    print(f"[*] Toplam {len(open_ports)} adet açık port bulundu:")
    
    open_ports.sort()
    for p in open_ports:
       
        desc = target_ports.get(p, "Bilinmeyen Servis")
        print(f"  > Port {p} : {desc}")
else:
    print("[✓] Hiç açık port bulunamadı. Sistem temiz görünüyor.")

print("="*35)
    


print("")
