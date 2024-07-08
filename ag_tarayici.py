"""optparse kullanılarak yapıldı"""
import scapy.all as scapy
import optparse
""" 3 iş yapacağız
1-	Arp_request : arp isteği
2-	Broadcast : yayın
3-	Response: cevap
"""

def kullanici_input():
    parse_obje = optparse.OptionParser()
    parse_obje.add_option("-i","--ipaddress", dest="ip_adresleri",help="Ağ tarayıcısı")
    (kul_input, argumanlar) = parse_obje.parse_args()
    if not kul_input.ip_adresleri:
        print("İp adresi gir.")

    return kul_input

def aglari_tara(ip):
    arp_istek_paket = scapy.ARP(pdst=ip)
    #scapy.ls(scapy.ARP()) ile terminalde kullanılacak parametreler görünür
    broadcast_paket = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    #scapy.ls(scapy.Ether()) ile terminalde kullanılacak parametreler görünür
    birlesik_paket = broadcast_paket/arp_istek_paket
    #birleştirme işlemi böyle yapılıyor
    (cevap_listesi, cevapsiz_listesi) = scapy.srp(birlesik_paket, timeout=1)
    #srp ile birleşmiş paketi alabiliyoruz. timeout 1 ise cevap vermeyende beklemesin diye
    cevap_listesi.summary()

kullanicinin_istedigi_ip = kullanici_input()
aglari_tara(kullanicinin_istedigi_ip.ip_adresleri)
