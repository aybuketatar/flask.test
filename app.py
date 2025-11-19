from flask import Flask, render_template, request

app = Flask(__name__)

# Anasayfa: Formu gösterir
@app.route('/')
def anasayfa():
    return render_template('index.html')

# Sonuç Sayfası: Formdan gelen veriyi işler
@app.route('/olustur', methods=['POST'])
def lisans_olustur():
    # 1. Formdan verileri al (Senin input() komutların yerine)
    eser_adi = request.form['eser_adi']
    yazar_adi = request.form['yazar_adi']
    yil = request.form['yil']
    eser_url = request.form['url']
    lisans_turu = request.form['lisans_turu']

    # 2. Lisans Metnini Oluştur (Senin if/else mantığın)
    if lisans_turu == "CC0":
        baslik = "Kamu Malı (CC0 1.0)"
        metin = f"{eser_adi} by {yazar_adi} is marked CC0 1.0"
        aciklama = "Bu eser Kamu Malıdır. Telif hakkı yoktur."
    elif lisans_turu == "CC-BY":
        baslik = "Atıf (CC BY 4.0)"
        metin = f"{eser_adi} © {yil} by {yazar_adi} is licensed under CC BY 4.0"
        aciklama = "Kaynak göstererek paylaşabilir ve değiştirebilirsiniz."
    elif lisans_turu == "CC-BY-SA":
        baslik = "Atıf-AynıLisanslaPaylaş (CC BY-SA 4.0)"
        metin = f"{eser_adi} © {yil} by {yazar_adi} is licensed under CC BY-SA 4.0"
        aciklama = "Aynı lisansla paylaşmak şartıyla değiştirebilirsiniz."
    elif lisans_turu == "CC-BY-ND":
        baslik = "Atıf-Türetilemez (CC BY-ND 4.0)"
        metin = f"{eser_adi} © {yil} by {yazar_adi} is licensed under CC BY-ND 4.0"
        aciklama = "Değiştiremezsiniz, sadece olduğu gibi paylaşabilirsiniz."
    elif lisans_turu == "CC-BY-NC":
        baslik = "Atıf-GayriTicari (CC BY-NC 4.0)"
        metin = f"{eser_adi} © {yil} by {yazar_adi} is licensed under CC BY-NC 4.0"
        aciklama = "Ticari amaçla kullanamazsınız."
    else:
        baslik = "Bilinmeyen Lisans"
        metin = "Hata: Geçersiz lisans türü."
        aciklama = ""

    # 3. Sonucu HTML sayfasına gönder (Senin print() komutun yerine)
    return render_template('sonuc.html', 
                           baslik=baslik, 
                           metin=metin, 
                           aciklama=aciklama,
                           eser=eser_adi,
                           url=eser_url)

if __name__ == '__main__':
    app.run(debug=True)