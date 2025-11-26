from flask import Flask, render_template
import random

app = Flask(__name__)

sozler = [
    "'Derdi dünya olanın, dünya kadar derdi olur.' - Yunus Emre",
    "'Büyük şeyler küçük şeylerin bir araya gelmesidir.' - Van Gogh",
    "Rüzgar eken fırtına biçer.",
    "Tatlı dil yılanı deliğinden çıkartır.",
    "Keser döner, sap döner; gün gelir hesap döner.",
    "İşleyen demir ışıldar."
    "Sütten ağzı yanan yoğurdu üfleyerek yer."
]

@app.route('/')
def ana_sayfa():
    secilen_soz = random.choice(sozler)
    return render_template('index.html', soz=secilen_soz)

if __name__ == '__main__':
    app.run(debug=True)