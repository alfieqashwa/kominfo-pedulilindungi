import scrapy
import urllib
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
        crawl_date = response.xpath(
            '//*[@id="why-us"]/div[1]/header/p/text()').extract_first().split()[5]
        year = crawl_date[-4:]
        month = crawl_date[3:5]
        day = crawl_date[:2]
        date_update = year + '-' + month + '-' + day
        provinsi = 'Jawa Tengah'
        kabkot = 'Boyolali'
        kecamatan = ''
        kelurahan = ''
        alamat = ''
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
        total_otg = ''
        odr_total = response.xpath(
            '//*[@id="why-us"]/div[2]/div/div[5]/div[1]/span/text()').extract_first()
        total_pp = ''
        total_ppdt = ''
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
        date_update = datetime.now().strftime("%Y-%m-%d")
        provinsi = 'Jawa Tengah'
        kabkot = 'Grobogan'
        kecamatan = ''
        kelurahan = ''
        alamat = ''
        total_odp = data['odp']
        total_pdp = data['pdp']
        total_positif = data['positif']
        positif_sembuh = ''
        positif_dirawat = ''
        positif_isolasi = ''
        positif_meninggal = data['dead']
        total_otg = ''
        odr_total = ''
        total_pp = ''
        total_ppdt = ''
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


class SemarangSpider(scrapy.Spider):
    name = "semarang"
    start_urls = [
        "https://siagacorona.semarangkota.go.id/halaman/odppdpv2"
    ]

    def parse(self, response):
        scrape_date = datetime.now().strftime("%Y-%m-%d")
        types = 'kabupaten'
        user_pic = 'Alfie Qashwa'
        # cannot crawl date_update
        date_update = datetime.now().strftime('%Y-%m-%d')
        provinsi = 'Jawa Tengah'
        kabkot = 'Semarang'
        # dupl_kec = response.xpath(
        #     '//*[@id="example1"]/tbody/tr/td[2]/text()').extract()
        # kecamatan = list(dict.fromkeys(dupl_kec))
        kecamatan = ''
        kelurahan = ''
        alamat = ''
        total_odp = response.xpath(
            '//*[@id="main-wrapper"]/div[2]/div[2]/div[1]/div[5]/div/div/div[1]/div[2]/div/text()').extract_first()
        t_pdp = response.xpath(
            '//*[@id="main-wrapper"]/div[2]/div[2]/div[1]/div[6]/div/div/div[1]/div[2]/div/text()')[1].extract()
        total_pdp = t_pdp.strip('\r\n ')
        total_positif = ''
        positif_sembuh = response.xpath(
            '//*[@id="main-wrapper"]/div[2]/div[2]/div[1]/div[3]/div/div/div[1]/div[2]/div/text()').extract_first()
        positif_dirawat = response.xpath(
            '//*[@id="main-wrapper"]/div[2]/div[2]/div[1]/div[2]/div/div/div[1]/div[2]/div/text()').extract_first()
        positif_isolasi = ''
        positif_meninggal = response.xpath(
            '//*[@id="main-wrapper"]/div[2]/div[2]/div[1]/div[4]/div/div/div[1]/div[2]/div/text()').extract_first()
        total_otg = ''
        odr_total = ''
        total_pp = ''
        total_ppdt = ''
        source_link = 'https://siagacorona.semarangkota.go.id/halaman/odppdpv2'

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


################################# KECAMATAN #####################################


class KudusSpider(scrapy.Spider):
    name = "kudus"
    start_urls = [
        "https://corona.kuduskab.go.id/"
    ]
    # convert months string into number
    months = dict(Januari='01', Februari='02', Maret='03', April='04', Mei='05', Juni='06',
                  Juli='07', Agustus='08', September='09', Oktober='10', November='11', Desember='12')

    def parse(self, response):
        scrape_date = datetime.now().strftime("%Y-%m-%d")
        types = "kecamatan"
        user_pic = "Alfie Qashwa"
        crawl_date = response.xpath(
            '//*[@id="monitoring"]/div/div/div/div/div[1]/span/text()').extract_first()
        # s**t dirty code
        day = crawl_date[18:20]
        month = crawl_date[21:30]
        year = crawl_date[31:35]
        date_update = year + '-' + self.months[month] + '-' + day
        provinsi = 'Jawa Tengah'
        kabkot = 'Kudus'
        kecamatan = response.xpath(
            '//*[@id="about"]/div/div/div/div/div/div/span/div/div/table/tbody/tr/td[1]/text()').extract()
        kelurahan = ''
        alamat = ''
        total_odp = response.xpath(
            '//*[@id="about"]/div/div/div/div/div/div/span/div/div/table/tbody/tr/td[3]/text()').extract()
        total_pdp = response.xpath(
            '//*[@id="about"]/div/div/div/div/div/div/span/div/div/table/tbody/tr/td[4]/text()').extract()
        total_positif = response.xpath(
            '//*[@id="about"]/div/div/div/div/div/div/span/div/div/table/tbody/tr/td[5]/text()').extract()
        positif_dirawat = response.xpath(
            '//*[@id="about"]/div/div/div/div/div/div/span/div/div/table/tbody/tr/td[6]/text()').extract()
        positif_isolasi = response.xpath(
            '//*[@id="about"]/div/div/div/div/div/div/span/div/div/table/tbody/tr/td[7]/text()').extract()
        positif_sembuh = response.xpath(
            '//*[@id="about"]/div/div/div/div/div/div/span/div/div/table/tbody/tr/td[8]/text()').extract()
        positif_meninggal = response.xpath(
            '//*[@id="about"]/div/div/div/div/div/div/span/div/div/table/tbody/tr/td[9]/text()').extract()
        total_otg = ''
        odr_total = response.xpath(
            '//*[@id="about"]/div/div/div/div/div/div/span/div/div/table/tbody/tr/td[2]/text()').extract()
        total_pp = ''
        total_ppdt = ''
        source_link = 'https://corona.kuduskab.go.id/'

        for q in range(len(kecamatan)):
            yield {
                'scrape_date': scrape_date,
                'types': types,
                'user_pic': user_pic,
                'date_update': date_update,
                'provinsi': provinsi,
                'kabkot': kabkot,
                'kecamatan': kecamatan[q].capitalize(),
                'kelurahan': kelurahan,
                'alamat': alamat,
                'total_odp': total_odp[q],
                'total_pdp': total_pdp[q],
                'total_positif': total_positif[q],
                'positif_sembuh': positif_sembuh[q],
                'positif_dirawat': positif_dirawat[q],
                'positif_isolasi': positif_isolasi[q],
                'positif_meninggal': positif_meninggal[q],
                'total_otg': total_otg,
                'odr_total': odr_total[q],
                'total_pp': total_pp,
                'total_ppdt': total_ppdt,
                'source_link': source_link,
            }


class CilacapSpider(scrapy.Spider):
    name = 'cilacap'
    start_urls = [
        "https://docs.google.com/spreadsheets/d/e/2PACX-1vRjGxvSiQjtQO7qSLj3umHBjodq0bTqOLnyYmvgXilPYoXj405WjVTOCumvl_yWg3bYWlV8oau0B_eK/pubhtml"
    ]

    def parse(self, response):
        scrape_date = datetime.now().strftime("%Y-%m-%d")
        types = 'kecamatan'
        user_pic = 'Alfie Qashwa'
        date_update = datetime.now().strftime("%Y-%m-%d")
        provinsi = 'Jawa Tengah'
        kabkot = 'Cilacap'
        kecamatan = response.xpath(
            '//*[@id="1603347864"]/div/table/tbody/tr/td[1]/text()')[4:-2].extract()
        kelurahan = ''
        alamat = ''
        total_odp = response.xpath(
            '//*[@id="1603347864"]/div/table/tbody/tr/td[8]/text()')[2:-2].extract()
        total_pdp = ''
        total_positif = response.xpath(
            '//*[@id="1603347864"]/div/table/tbody/tr/td[12]/text()')[1:-2].extract()
        positif_sembuh = response.xpath(
            '//*[@id="1603347864"]/div/table/tbody/tr/td[11]/text()')[3:-2].extract()
        positif_dirawat = response.xpath(
            '//*[@id="1603347864"]/div/table/tbody/tr/td[10]/text()')[2:-2].extract()
        positif_isolasi = ''
        positif_meninggal = response.xpath(
            '//*[@id="1603347864"]/div/table/tbody/tr/td[9]/text()')[2:-2].extract()
        total_otg = ''
        odr_total = response.xpath(
            '//*[@id="1603347864"]/div/table/tbody/tr/td[4]/text()')[3:-2].extract()
        total_pp = ''
        total_ppdt = ''
        source_link = 'http://corona.cilacapkab.go.id/'

        for q in range(len(kecamatan)):
            yield {
                'scrape_date': scrape_date,
                'types': types,
                'user_pic': user_pic,
                'date_update': date_update,
                'provinsi': provinsi,
                'kabkot': kabkot,
                'kecamatan': kecamatan[q],
                'kelurahan': kelurahan,
                'alamat': alamat,
                'total_odp': total_odp[q],
                'total_pdp': total_pdp,
                'total_positif': total_positif[q],
                'positif_sembuh': positif_sembuh[q],
                'positif_dirawat': positif_dirawat[q],
                'positif_isolasi': positif_isolasi,
                'positif_meninggal': positif_meninggal[q],
                'total_otg': total_otg,
                'odr_total': odr_total[q],
                'total_pp': total_pp,
                'total_ppdt': total_ppdt,
                'source_link': source_link,
            }


class MagelangSpider(scrapy.Spider):
    name = 'magelang'
    start_urls = [
        "https://infocorona.magelangkab.go.id/"
    ]

    months = dict(Januari='01', Februari='02', Maret='03', April='04', Mei='05', Juni='06',
                  Juli='07', Agustus='08', September='09', Oktober='10', November='11', Desember='12')

    def parse(self, response):
        scrape_date = datetime.now().strftime("%Y-%m-%d")
        types = 'kecamatan'
        user_pic = 'Alfie Qashwa'
        crawl_date = response.xpath(
            '//*[@id="statistik"]/div/div[1]/div[1]/div/div/text()').extract_first()
        # s**t dirty code
        day = crawl_date[9:11]
        month = crawl_date[12:21]
        year = crawl_date[22:26]
        date_update = year + '-' + self.months[month] + '-' + day
        provinsi = 'Jawa Tengah'
        kabkot = 'Magelang'
        kecamatan = response.xpath(
            '//*[@id="collapseTwo"]/div/div/div[4]/div/table/tbody/tr/td[1]/text()').extract()
        kelurahan = ''
        alamat = ''
        total_odp = response.xpath(
            '//*[@id="collapseTwo"]/div/div/div[4]/div/table/tbody/tr/td[2]/text()').extract()
        total_pdp = response.xpath(
            '//*[@id="collapseTwo"]/div/div/div[4]/div/table/tbody/tr/td[3]/text()').extract()
        total_positif = ''
        positif_sembuh = response.xpath(
            '//*[@id="collapseTwo"]/div/div/div[4]/div/table/tbody/tr/td[7]/text()').extract()
        positif_dirawat = response.xpath(
            '//*[@id="collapseTwo"]/div/div/div[4]/div/table/tbody/tr/td[6]/text()').extract()
        positif_isolasi = ''
        positif_meninggal = response.xpath(
            '//*[@id="collapseTwo"]/div/div/div[4]/div/table/tbody/tr/td[8]/text()').extract()
        total_otg = ''
        odr_total = ''
        total_pp = ''
        total_ppdt = ''
        source_link = 'https://infocorona.magelangkab.go.id/'

        for q in range(len(kecamatan)):
            yield {
                'scrape_date': scrape_date,
                'types': types,
                'user_pic': user_pic,
                'date_update': date_update,
                'provinsi': provinsi,
                'kabkot': kabkot,
                'kecamatan': kecamatan[q].capitalize(),
                'kelurahan': kelurahan,
                'alamat': alamat,
                'total_odp': total_odp[q],
                'total_pdp': total_pdp[q],
                'total_positif': total_positif,
                'positif_sembuh': positif_sembuh[q],
                'positif_dirawat': positif_dirawat[q],
                'positif_isolasi': positif_isolasi,
                'positif_meninggal': positif_meninggal[q],
                'total_otg': total_otg,
                'odr_total': odr_total,
                'total_pp': total_pp,
                'total_ppdt': total_ppdt,
                'source_link': source_link,
            }


class KebumenSpider(scrapy.Spider):
    name = "kebumen"
    start_urls = [
        "https://corona.kebumenkab.go.id/index.php/web/peta_sebaran"
    ]

    def parse(self, response):
        scrape_date = datetime.now().strftime('%Y-%m-%d')
        types = 'kecamatan'
        user_pic = 'Alfie Qashwa'
        date_update = datetime.now().strftime('%Y-%m-%d')
        provinsi = 'Jawa Tengah'
        kabkot = 'Kebumen'
        kecamatan = response.xpath(
            '//*[@id="lgx-news"]/div/div/div/div/div[1]/text()')[5:].re(r'n (\w+)')
        kelurahan = ''
        alamat = ''
        total_odp = response.xpath(
            '//*[@id="lgx-news"]/div/div/div/div/div[2]/p[1]/text()')[1:].re(r': (\w+)')
        total_pdp = response.xpath(
            '//*[@id="lgx-news"]/div/div/div/div/div[2]/p[2]/text()')[1:].re(r': (\w+)')
        total_positif = response.xpath(
            '//*[@id="lgx-news"]/div/div/div/div/div[2]/p[3]/text()')[1:].re(r': (\w+)')
        positif_sembuh = ''
        positif_dirawat = ''
        positif_isolasi = ''
        positif_meninggal = ''
        total_otg = ''
        odr_total = ''
        total_pp = ''
        total_ppdt = ''
        source_link = 'https://corona.kebumenkab.go.id/'

        for q in range(len(kecamatan)):
            yield {
                'scrape_date': scrape_date,
                'types': types,
                'user_pic': user_pic,
                'date_update': date_update,
                'provinsi': provinsi,
                'kabkot': kabkot,
                'kecamatan': kecamatan[q].strip(),
                'kelurahan': kelurahan,
                'alamat': alamat,
                'total_odp': total_odp[q],
                'total_pdp': total_pdp[q],
                'total_positif': total_positif[q],
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


class PurbalinggaSpider(scrapy.Spider):
    name = 'purbalingga'
    start_urls = [
        "https://petatematik.purbalinggakab.go.id/api/corona/data/geoJSON"
    ]
    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
        "Referer": "https://petatematik.purbalinggakab.go.id/peta/monitoring-corona",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (X11 Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
    }

    def parse(self, response):
        raw_data = response.body
        datas = json.loads(raw_data)
        scrape_date = datetime.now().strftime("%Y-%m-%d")
        types = 'kecamatan'
        user_pic = 'Alfie Qashwa'
        date_update = datetime.now().strftime("%Y-%m-%d")
        provinsi = 'Jawa Tengah'
        kabkot = 'Purbalingga'
        source_link = 'https://corona.purbalinggakab.go.id/'

        for data in datas:
            yield {
                'scrape_date': scrape_date,
                'types': types,
                'user_pic': user_pic,
                'date_update': date_update,
                'provinsi': provinsi,
                'kabkot': kabkot,
                'kecamatan': data["properties"]["name"],
                'kelurahan': '',
                'alamat': '',
                'total_odp': data["properties"]["odp_total"],
                'total_pdp': data["properties"]["pdp_total"],
                'total_positif': data["properties"]["positif_total"],
                'positif_sembuh': data["properties"]["positif_sembuh"],
                'positif_dirawat': data["properties"]["positif_dirawat"],
                'positif_isolasi': '',
                'positif_meninggal': data["properties"]["positif_meninggal"],
                'total_otg': '',
                'odr_total': '',
                'total_pp': '',
                'total_ppdt': '',
                'source_link': source_link,
            }


################################# KELURAHAN #####################################


class TegalSpider(scrapy.Spider):
    name = "tegal"
    start_urls = "https://corona.tegalkota.go.id/index.php/Api/api_getDataPetaCovid"

    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
        "Referer": "https://corona.tegalkota.go.id/?page=peta",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (X11 Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
    }

# there's information about `kelurahan` only but no `kecamatan` classification.
# source:
# https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kota_Tegal

    margadana = ["Cabawan", "Kaligangsa", "Kalinyamat Kulon",
                 "Krandon", "Margadana", "Pesurungan Lor", "Sumurpanggang"]
    tegalbarat = ["Debong Lor", "Kemandungan", "Kraton",
                  "Muarareja", "Pekauman", "Pesurungan Kidul", "Tegalsari"]
    tegalselatan = ["Bandung", "Debong Kidul", "Debong Kulon",
                    "Debong Tengah", "Kalinyamat Wetan", "Keturen", "Randugunting", "Tunon"]
    tegaltimur = ["Kejambon", "Mangkukusuman",
                  "Mintaragen", "Panggung", "Slerok"]

    def start_requests(self):
        params = {
            # Query String Paramaters on Headers is required,
            # otherwise the response status would be "ERROR".
            'token': '4yt6rul1232y2yi23'
        }

        # Reminder:
        # f'some string {some_variables}' in Python
        # are similar as
        # `some strings ${someVariables}` in JavaScript.

        url = f'{self.start_urls}?{urllib.parse.urlencode(params)}'
        request = scrapy.Request(url=url, callback=self.parse)
        request.meta['params'] = params
        return [request]

    def parse(self, response):
        raw_data = response.body
        datas = json.loads(raw_data)
        scrape_date = datetime.now().strftime("%Y-%m-%d")
        types = 'kelurahan'
        user_pic = 'Alfie Qashwa'
        date_update = datetime.now().strftime("%Y-%m-%d")
        provinsi = 'Jawa Tengah'
        kabkot = 'Tegal'
        source_link = 'https://corona.tegalkota.go.id/'

        for data in datas["response"]["data"]:
            kelurahan = data["nama_kelurahan"]
            if kelurahan in self.margadana:
                kecamatan = 'Marganda'
            elif kelurahan in self.tegalbarat:
                kecamatan = 'Tegal Barat'
            elif kelurahan in self.tegalselatan:
                kecamatan = 'Tegal Selatan'
            elif kelurahan in self.tegaltimur:
                kecamatan = 'Tegal Timur'
            else:
                kecamatan = ''
            yield {
                'scrape_date': scrape_date,
                'types': types,
                'user_pic': user_pic,
                'date_update': date_update,
                'provinsi': provinsi,
                'kabkot': kabkot,
                'kecamatan': kecamatan,
                'kelurahan': kelurahan,

                ############# // TODOS //#############

                # 'alamat': '',
                # 'total_odp':,
                # 'total_pdp':,
                # 'total_positif':,
                # 'positif_sembuh':,
                # 'positif_dirawat':,
                # 'positif_isolasi': '',
                # 'positif_meninggal':,
                # 'total_otg': '',
                # 'odr_total': '',
                # 'total_pp': '',
                # 'total_ppdt': '',
                'source_link': source_link,
            }
