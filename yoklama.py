import json
import os
import sys
kacan_dersler = []

ders_listesi = []

if os.path.exists("yoklamaxd.json") and os.path.getsize("yoklamaxd.json") > 0:
    with open("yoklamaxd.json", "r", encoding="utf-8") as dosya:
        veri = json.load(dosya)
else:
    veri = {
        "mesaj": "Ders kaçırma takibi",
        "ders_listesi": [
            {"ders_adi": "AYRIK YAPILAR", "kaç_derse_girmedim": 0},
            {"ders_adi": "FIZIK II", "kaç_derse_girmedim": 0},
            {"ders_adi": "AKADEMIK INGILIZCE", "kaç_derse_girmedim": 0},
            {"ders_adi": "MATEMATIK II", "kaç_derse_girmedim": 0},
            {"ders_adi": "SECMELI DERS", "kaç_derse_girmedim": 0},
            {"ders_adi": "JAVA", "kaç_derse_girmedim": 0}
        ]
    }


print("Yoklama kontrol paneli ..")

print("Kayıtlı dersleriniz ve kaçırılan ders sayıları:")
print()
for index, ders in enumerate(veri["ders_listesi"], start=1):
    print(f"{index}. {ders['ders_adi']} - Kaçırılan ders sayısı: {ders['kaç_derse_girmedim']}")
print("\n\n\n")
print("yeni yoklama eklemek için ders seç kral")
print()
print("çıkmak için 'q' basınız")
print("\n\n\n")

kontrol = input()
if kontrol == "q":
    sys.exit()

kacan_dersler = int(input("kaç derse girmedim"))

if kontrol == "1":
    for ders in veri["ders_listesi"]:
        if ders["ders_adı"] == "AYRIK YAPILAR":
            ders["kaç_derse_girmedim"] += kacan_dersler
        break
elif kontrol == "2":
    for ders in veri["ders_listesi"]:
        if ders["ders_adi"] == "FIZIK II":
            ders["kaç_derse_girmedim"] += kacan_dersler
            break
elif kontrol == "3":
    for ders in veri["ders_listesi"]:
        if ders["ders_adi"] == "AKADEMIK INGILIZCE":
            ders["kaç_derse_girmedim"] += kacan_dersler
            break
elif kontrol == "4":
    for ders in veri["ders_listesi"]:
        if ders["ders_adi"] == "MATEMATIK II":
            ders["kaç_derse_girmedim"] += kacan_dersler
            break
elif kontrol == "5":
    for ders in veri["ders_listesi"]:
        if ders["ders_adi"] == "SECMELI DERS":
            ders["kaç_derse_girmedim"] += kacan_dersler
            break
elif kontrol == "6":
    for ders in veri["ders_listesi"]:
        if ders["ders_adi"] == "JAVA":
            ders["kaç_derse_girmedim"] += kacan_dersler
            break

with open("yoklamaxd.json", "w", encoding="utf-8") as dosya:
    json.dump(veri, dosya, indent=4, ensure_ascii=False)

print("\nVeriler kaydedildi. Program kapatılıyor...")
input()