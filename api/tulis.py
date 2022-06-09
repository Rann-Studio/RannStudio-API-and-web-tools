from PIL import Image, ImageDraw, ImageFont
import datetime

class Tulis:
    def __init__(self, teks, kertas, font, nama, kelas, tanggal):
        self.config = {
            "kertas": {
                "1": {"nama": "kertas1.jpg", "baris": 25, "perEnter":92,  "lokasi": [531, 347], "info":[310, 170, 60], "tgl": [335, 1675], "nomor": [529,212]},
                "2": {"nama": "kertas2.jpg", "baris": 25, "perEnter":104, "lokasi": [570, 322], "info":[305, 170, 56], "tgl": [375, 1815], "nomor": [551,169]},
                "3": {"nama": "kertas3.jpg", "baris": 25, "perEnter":103, "lokasi": [605, 305], "info":[320, 170, 60], "tgl": [410, 1780], "nomor": [598,153]},
                "4": {"nama": "kertas4.jpg", "baris": 31, "perEnter":92,  "lokasi": [505, 280], "info":[255, 130, 56], "tgl": [315, 1695], "nomor": [491,100]},
                "5": {"nama": "kertas5.jpg", "baris": 31, "perEnter":94,  "lokasi": [515, 313], "info":[300, 140, 60], "tgl": [320, 1720], "nomor": [518,145]}
            },
            "font": {
                "1": {"nama": "font1.ttf", "ukuran":48, "autoEnter": {"1": 79, "2": 86, "3": 86, "4": 85, "5": 89}},
                "2": {"nama": "font2.ttf", "ukuran":67, "autoEnter": {"1": 74, "2": 82, "3": 82, "4": 78, "5": 78}},
                "3": {"nama": "font3.ttf", "ukuran":61, "autoEnter": {"1": 67, "2": 73, "3": 73, "4": 75, "5": 76}}
            }
        }
        
        self.text = teks
        self.noKertas = kertas
        self.cfgkertas = self.config["kertas"][str(kertas)]
        self.cfgfont = self.config["font"][str(font)]
        
        if ( nama == "false" ) and ( kelas == "false" ) and ( tanggal == "false" ):
            self.info = {"": "", "": "", "": ""}
            
        elif ( nama != "false" ) and ( kelas == "false" ) and ( tanggal == "false" ):
            self.info = {"nama": nama, "": "", "": ""}
            
        elif ( nama == "false" ) and ( kelas != "false" ) and ( tanggal == "false" ):
            self.info = {"": "", "kelas": kelas, "": ""}
            
        elif ( nama == "false" ) and ( kelas == "false" ) and ( tanggal != "false" ):
            self.info = {"": "", "": "", "tanggal": tanggal}
            
        elif ( nama != "false" ) and ( kelas != "false" ) and ( tanggal == "false" ):
            self.info = {"nama": nama, "kelas": kelas, "": ""}
        
        elif ( nama == "false" ) and ( kelas != "false" ) and ( tanggal != "false" ):
            self.info = {"": "", "kelas": kelas, "tanggal": tanggal}
        
        elif ( nama != "false" ) and ( kelas == "false" ) and ( tanggal != "false" ):
            self.info = {"nama": nama, "": "", "tanggal": tanggal}
            
        elif ( nama != "false" ) and ( kelas != "false" ) and ( tanggal != "false" ):
            self.info = {"nama": nama, "kelas": kelas, "tanggal": tanggal}

    def buatGambar(self):
        self.countLoop = 1
        self.kertas = Image.open("api/src/img/" + self.cfgkertas["nama"])
        self.draw1 = ImageDraw.Draw(self.kertas)
        self.ukuranFont = self.cfgfont["ukuran"]
        self.namaFont = ImageFont.truetype("api/src/font/" + self.cfgfont["nama"], self.ukuranFont)
        
        infoAtas = self.cfgkertas["info"][0]
        infoSamping = self.cfgkertas["info"][1]
        
        for data in self.info.keys():
            if data == "nama":
                self.draw1.text((infoSamping, infoAtas), "Nama : " + str(self.info[data]), font = self.namaFont, fill = (42, 43, 43))
                infoAtas += self.cfgkertas["info"][2]
            elif data == "kelas":
                self.draw1.text((infoSamping, infoAtas), "Kelas : " + str(self.info[data]), font = self.namaFont, fill = (42, 43, 43))
                infoAtas += self.cfgkertas["info"][2]
            elif data == "tanggal":
                self.draw1.text((infoSamping, infoAtas), "Tanggal : " + str(self.info[data]), font = self.namaFont, fill = (42, 43, 43))
            else:
                self.draw1.text((infoSamping, infoAtas), (data + " " + str(self.info[data])), font = self.namaFont, fill = (42, 43, 43))
                infoAtas += self.cfgkertas["info"][2]
                
        process = self.processText()
        return process
        
    def processText(self):
        inpText = self.text.split("\n")
        jlhText = len(inpText)
        
        if jlhText > (self.cfgkertas["baris"] * 2):
            kirim = {"status": "gagal", "message": "Jumlah baris melebihi batas maksimal. silahkan menggunakan kertas lain.", "kertas_tersedia": ["Kertas " +  str(x) for x in self.config["kertas"].keys()]}
            return kirim
        else:
            awalAtas = self.cfgkertas["lokasi"][0]
            self.hasilText = []
            maxChar = self.cfgfont["autoEnter"][str(self.noKertas)]
            
            for i in inpText:
                pjgChar = len(str(i))
                txtPerLine = []
                while pjgChar > maxChar:
                    self.hasilText.append(i[:maxChar])
                    i = i[maxChar:]
                    pjgChar -= maxChar
                else:
                    self.hasilText.append(i)
                    
            if len(self.hasilText) > (self.cfgkertas["baris"] * 2):
                 kirim = {"status": "gagal", "message": "Jumlah baris melebihi batas maksimal. silahkan menggunakan kertas lain.", "kertas_tersedia": ["Kertas " + str(x) for x in self.config["kertas"].keys()]}
                 return kirim
             
            return self.processTulis()
        
    def processTulis(self):
        jlhText = len(self.hasilText)
        if len(self.hasilText) > self.cfgkertas["baris"]:
            self.countLoop += 2
        namaFilePjg = []
        namaFile = []
        awal = 0
        
        for i in range(self.countLoop):
            awalAtas, awalSamping = self.cfgkertas["lokasi"]
            nomorAtas, nomorSamping = self.cfgkertas["nomor"]
            for j, k in enumerate(self.hasilText[awal:self.cfgkertas["baris"]*(i+1)]):
                pjgChar = len(str(k))
                self.draw1.text((awalSamping, awalAtas), str(k), font = self.namaFont, fill = (42, 43, 43))
                awalAtas += self.cfgkertas["perEnter"]
                nomorAtas += self.cfgkertas["perEnter"]
                
            awal = self.cfgkertas["baris"]
            
            __namafile =  datetime.datetime.now().strftime("%H%M%S%d%m%Y") + ".png"
            __lok = "api/src/output/" + __namafile
            
            namaFile.append(__namafile)
            namaFilePjg.append(__lok)
            
            self.kertas.save(__lok)
            
            self.kertas = Image.open("api/src/img/" + self.cfgkertas["nama"])
            self.d1 = ImageDraw.Draw(self.kertas)
            
        kirim = {"status": "sukses", "message": "Sukses membuat gambar", "filename": namaFile}
        return kirim