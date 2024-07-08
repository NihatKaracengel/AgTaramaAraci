import scapy.all as scapy
import argparse

"""
3 iş yapacağız:
1- Arp_request : arp isteği
2- Broadcast : yayın
3- Response: cevap
"""

def kullanici_input():
    # Argümanları işlemek için argparse kütüphanesinden bir parser oluşturuyoruz.
    parser = argparse.ArgumentParser(description="Ağ tarayıcısı")
    # -i veya --ipaddress seçeneklerini tanımlıyoruz, ip_adresleri değişkenine atanacak.
    parser.add_argument("-i", "--ipaddress", dest="ip_adresleri", required=True, help="IP adreslerini girin")
    # Kullanıcının verdiği argümanları analiz ediyoruz.
    args = parser.parse_args()
    return args

def aglari_tara(ip):
    # Verilen IP adresi için ARP isteği paketi oluşturuyoruz.
    arp_istek_paket = scapy.ARP(pdst=ip)
    # Ethernet seviyesinde yayın (broadcast) paketi oluşturuyoruz.
    broadcast_paket = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    # ARP isteği paketi ile Ethernet yayın paketini birleştiriyoruz.
    birlesik_paket = broadcast_paket / arp_istek_paket
    # Birleştirilmiş paketi ağda gönderiyoruz ve cevapları alıyoruz.
    # Timeout süresini 1 saniye olarak belirliyoruz ve verbose modunu aktif hale getiriyoruz.
    (cevap_listesi, cevapsiz_listesi) = scapy.srp(birlesik_paket, timeout=1, verbose=True)

    # Her bir cevap için gelen paketleri işliyoruz.
    for sent, received in cevap_listesi:
        # Cevaplanan her bir ARP isteğinin kaynağındaki Ethernet (MAC) adresi ve
        # ARP (IP) adresini terminale yazdırıyoruz.
        print(f"{received[scapy.Ether].src} - {received[scapy.ARP].psrc}")

# Kullanıcıdan IP adresini alıyoruz.
kullanicinin_istedigi_ip = kullanici_input()
# Belirtilen IP adresi için ağ tarayıcısını çalıştırıyoruz.
aglari_tara(kullanicinin_istedigi_ip.ip_adresleri)
