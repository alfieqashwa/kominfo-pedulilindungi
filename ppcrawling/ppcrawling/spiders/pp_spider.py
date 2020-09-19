import scrapy
from datetime import datetime
import json


class BoyolaliSpider(scrapy.Spider):
    name = "boyolali"
    start_urls = [
        "https://covid19.boyolali.go.id/"
    ]

    def parse(self, response):
        scrape_date = datetime.now().strftime("%Y-%m-%d")
        types = 'kabupaten'
        user_pic = 'Alfie Qashwa'
        date_update = response.xpath(
            '//*[@id="why-us"]/div[1]/header/p/text()').extract_first().split()[5].replace('-', '/')
        provinsi = 'Jawa Tengah'
        kabkot = 'Boyolali'
        kecamatan = None
        kelurahan = None
        alamat = None
        total_odp = response.xpath(
            '//*[@id="why-us"]/div[2]/div/div[2]/div/span/text()').extract_first()
        total_pdp = response.xpath(
            '//*[@id="why-us"]/div[2]/div/div[4]/div[1]/span/text()').extract_first()
        total_positif = response.xpath(
            '//*[@id="why-us"]/div[2]/div/div[1]/div[1]/div[1]/div/span/text()').extract_first()
        positif_sembuh = response.xpath(
            '//*[@id="why-us"]/div[2]/div/div[1]/div[1]/div[2]/div[3]/span/text()').extract_first()
        positif_dirawat = response.xpath(
            '//*[@id="why-us"]/div[2]/div/div[1]/div[1]/div[2]/div[1]/span/text()').extract_first()
        positif_isolasi = response.xpath(
            '//*[@id="why-us"]/div[2]/div/div[1]/div[1]/div[2]/div[2]/span/text()').extract_first()
        positif_meninggal = response.xpath(
            '//*[@id="why-us"]/div[2]/div/div[1]/div[1]/div[2]/div[4]/span/text()').extract_first()
        total_otg = None
        odr_total = response.xpath(
            '//*[@id="why-us"]/div[2]/div/div[5]/div[1]/span/text()').extract_first()
        total_pp = None
        total_ppdt = None
        source_link = 'https://covid19.boyolali.go.id/'

        yield {
            'scrape_date': scrape_date,
            'types': types,
            'user_pic': user_pic,
            'date_update': date_update,
            'provinsi': provinsi,
            'kabkot': kabkot,
            'kecamatan': kecamatan,
            'kelurahan': kelurahan,
            'alamat': alamat,
            'total_odp': total_odp,
            'total_pdp': total_pdp,
            'total_positif': total_positif,
            'positif_sembuh': positif_sembuh,
            'positif_dirawat': positif_dirawat,
            'positif_isolasi': positif_isolasi,
            'positif_meninggal': positif_meninggal,
            'total_otg': total_otg,
            'odr_total': odr_total,
            'total_pp': total_pp,
            'total_ppdt': total_ppdt,
            'source_link': source_link,
        }


# This website is SPA
class GroboganSpider(scrapy.Spider):
    name = 'grobogan'
    start_urls = [
        "https://corona.grobogan.go.id/data.json"
    ]
    headers = {
        "Accept": "Accept: application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
        "Referer": "https://corona.grobogan.go.id/",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (X11 Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
    }

    def parse(self, response):
        raw_data = response.body
        data = json.loads(raw_data)

        scrape_date = datetime.now().strftime("%Y-%m-%d")
        types = 'kabupaten'
        user_pic = 'Alfie Qashwa'
        # they will fetch the datas everyday automatically as data-fetching habits
        date_update = datetime.now().strftime("%d/%m/%Y")
        provinsi = 'Jawa Tengah'
        kabkot = 'Grobogan'
        kecamatan = None
        kelurahan = None
        alamat = None
        total_odp = data['odp']
        total_pdp = data['pdp']
        total_positif = data['positif']
        positif_sembuh = None
        positif_dirawat = None
        positif_isolasi = None
        positif_meninggal = data['dead']
        total_otg = None
        odr_total = None
        total_pp = None
        total_ppdt = None
        source_link = 'https://corona.grobogan.go.id/'

        yield {
            'scrape_date': scrape_date,
            'types': types,
            'user_pic': user_pic,
            'date_update': date_update,
            'provinsi': provinsi,
            'kabkot': kabkot,
            'kecamatan': kecamatan,
            'kelurahan': kelurahan,
            'alamat': alamat,
            'total_odp': total_odp,
            'total_pdp': total_pdp,
            'total_positif': total_positif,
            'positif_sembuh': positif_sembuh,
            'positif_dirawat': positif_dirawat,
            'positif_isolasi': positif_isolasi,
            'positif_meninggal': positif_meninggal,
            'total_otg': total_otg,
            'odr_total': odr_total,
            'total_pp': total_pp,
            'total_ppdt': total_ppdt,
            'source_link': source_link,
        }
