STORY_TEMPLATES = {
    "petualangan": {
        "title": "Petualangan di Hutan Ajaib",
        "template": """
Pada suatu hari yang {adjective1}, seorang {noun1} bernama {name} 
memutuskan untuk {verb1} ke dalam hutan yang penuh misteri. 

Di tengah perjalanan, {name} bertemu dengan {noun2} yang sangat {adjective2}.
"{noun2} ini bisa {verb2}!" teriak {name} dengan penuh {emotion}.

Tanpa pikir panjang, {name} mengajak {noun2} untuk {verb3} bersama.
Mereka menemukan {noun3} yang {adjective3} di balik pohon besar.

"Ini adalah hari yang paling {adjective4} dalam hidupku!" seru {name}.
Dan sejak itu, {name} dan {noun2} menjadi sahabat yang saling {verb4}.
        """,
        "inputs": [
            ("name", "Nama karakter utama"),
            ("adjective1", "Kata sifat (contoh: cerah, dingin, aneh)"),
            ("noun1", "Kata benda/profesi (contoh: petani, penyihir, robot)"),
            ("verb1", "Kata kerja (contoh: berlari, terbang, menyelam)"),
            ("noun2", "Kata benda/makhluk (contoh: naga, kucing, alien)"),
            ("adjective2", "Kata sifat (contoh: lucu, menakutkan, ramah)"),
            ("verb2", "Kata kerja (contoh: bernyanyi, memasak, menari)"),
            ("emotion", "Emosi (contoh: takjub, kaget, gembira)"),
            ("verb3", "Kata kerja (contoh: berpetualang, bermain, berburu)"),
            ("noun3", "Kata benda/harta (contoh: harta karun, peta, kunci)"),
            ("adjective3", "Kata sifat (contoh: berkilau, tua, ajaib)"),
            ("adjective4", "Kata sifat (contoh: seru, aneh, berbahaya)"),
            ("verb4", "Kata kerja (contoh: membantu, menghibur, melindungi)")
        ]
    },
    
    "komedi": {
        "title": "Kekacauan di Rumah",
        "template": """
Pagi ini, {name} bangun dan menemukan {noun1} di atas {noun2}.
"Kenapa {noun1} bisa {verb1} di sana?!" teriak {name} sambil {verb2}.

{name} mencoba untuk {verb3}, tapi malah membuat {noun3} menjadi {adjective1}.
Tetangga sebelah, Pak {neighbor_name}, datang dan berkata, 
"Wah, rumahmu {adjective2} sekali hari ini!"

Akhirnya {name} harus memanggil {noun4} profesional untuk {verb4}.
Biayanya {adjective3} sekali, tapi setidaknya sekarang rumah sudah {adjective4}.

Pelajaran hari ini: Jangan pernah {verb5} sebelum {verb6}!
        """,
        "inputs": [
            ("name", "Nama karakter utama"),
            ("noun1", "Benda aneh (contoh: kulkas, sepeda, piano)"),
            ("noun2", "Tempat aneh (contoh: atap, kolam, pohon)"),
            ("verb1", "Kata kerja (contoh: terbang, berenang, menari)"),
            ("verb2", "Kata kerja emosi (contoh: tertawa, menangis, berteriak)"),
            ("verb3", "Kata kerja aksi (contoh: memperbaiki, membersihkan, mengangkat)"),
            ("noun3", "Benda lain (contoh: dinding, lantai, meja)"),
            ("adjective1", "Kata sifat (contoh: biru, lengket, berbulu)"),
            ("neighbor_name", "Nama tetangga"),
            ("adjective2", "Kata sifat (contoh: ramai, berantakan, unik)"),
            ("noun4", "Profesi (contoh: tukang, dokter, detektif)"),
            ("verb4", "Kata kerja (contoh: menyelesaikan, memperbaiki, menyelidiki)"),
            ("adjective3", "Kata sifat (contoh: mahal, murah, fantastis)"),
            ("adjective4", "Kata sifat (contoh: normal, rapi, sempurna)"),
            ("verb5", "Kata kerja (contoh: melompat, makan, tidur)"),
            ("verb6", "Kata kerja (contoh: berpikir, menelpon, berdoa)")
        ]
    },
    
    "fantasi": {
        "title": "Kerajaan yang Terlupakan",
        "template": """
Di kerajaan {adjective1} yang bernama {kingdom_name}, hiduplah 
seorang {noun1} yang memiliki kekuatan untuk {verb1}.

Suatu malam, {noun2} yang {adjective2} muncul di langit dan berkata,
"Wahai {name}, kau harus {verb2} untuk menyelamatkan {noun3}!"

Dengan membawa {noun4} yang {adjective3}, {name} memulai perjalanan.
Dalam perjalanan, {name} harus {verb3} melewati {noun5} yang {adjective4}.

Setelah berpetualang selama {number} hari, akhirnya {name} berhasil {verb4}.
Seluruh kerajaan {verb5} dengan penuh {emotion}, dan {name} dianugerahi 
gelar sebagai {title} yang paling {adjective5} sepanjang masa!
        """,
        "inputs": [
            ("kingdom_name", "Nama kerajaan fantasi"),
            ("adjective1", "Kata sifat (contoh: megah, tersembunyi, terkutuk)"),
            ("noun1", "Profesi fantasi (contoh: penyihir, ksatria, pedagang)"),
            ("verb1", "Kata kerja kekuatan (contoh: mengendalikan api, memanggil hujan)"),
            ("noun2", "Makhluk mistis (contoh: naga, peri, roh)"),
            ("adjective2", "Kata sifat (contoh: bijaksana, menakutkan, bercahaya)"),
            ("name", "Nama karakter utama"),
            ("verb2", "Kata kerja misi (contoh: bertarung, mencari, menyelamatkan)"),
            ("noun3", "Yang diselamatkan (contoh: putri, harta, rakyat)"),
            ("noun4", "Item magis (contoh: pedang, tongkat, jimat)"),
            ("adjective3", "Kata sifat (contoh: sakti, kuno, berkilau)"),
            ("verb3", "Kata kerja tantangan (contoh: melompat, berenang, terbang)"),
            ("noun5", "Rintangan (contoh: gunung, sungai, gua)"),
            ("adjective4", "Kata sifat (contoh: berbahaya, gelap, tinggi)"),
            ("number", "Angka (contoh: 7, 40, 100)"),
            ("verb4", "Kata kerja kemenangan (contoh: mengalahkan, menemukan, menyelesaikan)"),
            ("verb5", "Kata kerja perayaan (contoh: berpesta, bersorak, menari)"),
            ("emotion", "Emosi (contoh: kegembiraan, haru, syukur)"),
            ("title", "Gelar kehormatan (contoh: pahlawan, pelindung, penyelamat)"),
            ("adjective5", "Kata sifat (contoh: berani, bijaksana, hebat)")
        ]
    }
}


def get_available_stories():
    return list(STORY_TEMPLATES.keys())


def get_story_template(story_type: str):
    return STORY_TEMPLATES.get(story_type)