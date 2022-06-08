import requests
import xmltodict
import json

class BMKG:
    # Gempa terbaru
    def gempaTerbaru(self):
        url = "https://data.bmkg.go.id/DataMKG/TEWS/autogempa.json"
        return requests.get(url).json()
    
    # 15 Gempa terbaru
    def gempaTerbaru15(self):
        url = "https://data.bmkg.go.id/DataMKG/TEWS/gempadirasakan.json"
        return requests.get(url).json()
    
    # 15 gempa terbaru diatas 5.0 magnitude
    def gempaTerbaru15_M5(self):
        url = "https://data.bmkg.go.id/DataMKG/TEWS/gempaterkini.json"
        return requests.get(url).json()
    
    # mendapatkan gambar shakemap
    def getShakemap(self, name):
        url = "https://data.bmkg.go.id/DataMKG/TEWS/" + name
        return requests.get(url).content
    
    # mendapatkan perkiraan cuaca berdasarkan nama provinsi
    def cuaca(self, nama_provinsi):
        url = "https://data.bmkg.go.id/DataMKG/MEWS/DigitalForecast/DigitalForecast-" + nama_provinsi + ".xml"
        req = requests.get(url)
        return req.status_code, req.content