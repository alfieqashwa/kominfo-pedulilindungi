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

            # token has changed on each request i believe
            # 'token': '4yt6rul1232y2yi23'
            'token': '4yt6rul1232y2yi24'
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

            alamat = data["alamat_kelurahan"]
            total_odp = int(data["ttl_odp_isolasi_mandiri"]) + int(
                data["ttl_odp_selesai_isolasi"]) + int(data["ttl_odp_meninggal"])
            total_pdp = int(data["ttl_pdp_dirawat"]) + \
                int(data["ttl_pdp_sembuh"]) + int(data["ttl_pdp_meninggal"])

            positif_sembuh = int(data["ttl_positif_sembuh"])
            positif_dirawat = int(data["ttl_positif_dirawat"])
            positif_isolasi = int(data["ttl_positif_isolasi_mandiri"])
            positif_meninggal = int(data["ttl_positif_meninggal"])
            total_positif = positif_sembuh + positif_dirawat + \
                positif_isolasi + positif_meninggal
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
                'total_odp': str(total_odp),
                'total_pdp': str(total_pdp),
                'total_positif': str(total_positif),
                'positif_sembuh': str(positif_sembuh),
                'positif_dirawat': str(positif_dirawat),
                'positif_isolasi': str(positif_isolasi),
                'positif_meninggal': str(positif_meninggal),
                'total_otg': '',
                'odr_total': '',
                'total_pp': '',
                'total_ppdt': '',
                'source_link': source_link,
            }


class KotaMagelangSpider(scrapy.Spider):
    name = 'kotamagelang'
    start_urls = [
        'https://covid19.magelangkota.go.id'
    ]

    magelang_selatan = ["Jurangombo Selatan", "Jurangombo Utara",
                        "Magersari", "Rejowinangun Selatan", "Tidar Selatan", "Tidar Utara"]
    magelang_tengah = ["Cacaban", "Gelangan", "Kemirirejo",
                       "Magelang", "Panjang", "Rejowinangun Utara"]
    magelang_utara = ["Kedungsari", "Kramat Selatan",
                      "Kramat Utara", "Potrobangsan", "Wates"]

    months = dict(Januari='01', Februari='02', Maret='03', April='04', Mei='05', Juni='06',
                  Juli='07', Agustus='08', September='09', Oktober='10', November='11', Desember='12')

    def parse(self, response):
        scrape_date = datetime.now().strftime("%Y-%m-%d")
        types = 'kelurahan'
        user_pic = 'Alfie Qashwa'
        raw_date = response.xpath(
            '//*[@id="update"]/div/div/div/div[2]/div/div/div[2]/div/div/div/div[1]/div/div/div[1]/div/div/div/div/div/div/div[2]/div/div/p[1]/span/text()').get()
        day = raw_date[9:11]
        # because its crawl SEPTEMBER
        month = raw_date[12:21].capitalize()
        year = raw_date[22:26]
        date_update = year + '-' + self.months[month] + '-' + day
        provinsi = 'Jawa Tengah'
        kabkot = 'Kota Magelang'
        list_kelurahan = ['Jurangombo Utara', 'Jurangombo Selatan', 'Magersari', 'Rejowinangun Selatan', 'Tidar Utara', 'Tidar Selatan', 'Cacaban',
                          'Gelangan', 'Kemirirejo', 'Magelang', 'Panjang', 'Rejowinangun Utara', 'Kedungsari', 'Kramat Selatan', 'Kramat Utara', 'Potrobangsan', 'Wates']

        for q in range(len(list_kelurahan)):
            kelurahan = list_kelurahan[q]

            if kelurahan in self.magelang_selatan:
                kecamatan = 'Magelang Selatan'
            elif kelurahan in self.magelang_tengah:
                kecamatan = 'Magelang Tengah'
            elif kelurahan in self.magelang_utara:
                kecamatan = 'Magelang Utara'
            else:
                kecamatan = ''

            total_odp = response.xpath(
                '//*[@id="lengkap"]/div/div/div/div/div/div/div[2]/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div/p/text()').getall()
            total_pdp = response.xpath(
                '//*[@id="lengkap"]/div/div/div/div/div/div/div[2]/div/div/div/div[2]/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div/p/text()').getall()
            total_positif = response.xpath(
                '//*[@id="lengkap"]/div/div/div/div/div/div/div[2]/div/div/div/div[3]/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div/p/span/text()')[1:18].getall()
            positif_sembuh = response.xpath(
                '//*[@id="lengkap"]/div/div/div/div/div/div/div[2]/div/div/div/div[3]/div/div/div/div/div/div/div[5]/div/div[2]/div/div/div/p/span/text()')[1:18].getall()
            positif_dirawat = response.xpath(
                '//*[@id="lengkap"]/div/div/div/div/div/div/div[2]/div/div/div/div[3]/div/div/div/div/div/div/div[3]/div/div[2]/div/div/div/p/span/text()')[1:18].getall()
            positif_isolasi = response.xpath(
                '//*[@id="lengkap"]/div/div/div/div/div/div/div[2]/div/div/div/div[3]/div/div/div/div/div/div/div[4]/div/div[2]/div/div/div/p/span/text()')[1:18].getall()
            positif_meninggal = response.xpath(
                '//*[@id="lengkap"]/div/div/div/div/div/div/div[2]/div/div/div/div[3]/div/div/div/div/div/div/div[6]/div/div[2]/div/div/div/p/span/text()')[1:18].getall()

            source_link = 'https://covid19.magelangkota.go.id/'
            yield {
                'scrape_date': scrape_date,
                'types': types,
                'user_pic': user_pic,
                'date_update': date_update,
                'provinsi': provinsi,
                'kabkot': kabkot,
                'kecamatan': kecamatan,
                'kelurahan': kelurahan,
                'alamat': '',
                'total_odp': total_odp[q].strip(),
                'total_pdp': total_pdp[q].strip(),
                'total_positif': total_positif[q].strip(),
                'positif_sembuh': positif_sembuh[q].strip(),
                'positif_dirawat': positif_dirawat[q].strip(),
                'positif_isolasi': positif_isolasi[q].strip(),
                'positif_meninggal': positif_meninggal[q].strip(),
                'total_otg': '',
                'odr_total': '',
                'total_pp': '',
                'total_ppdt': '',
                'source_link': source_link,
            }


class KendalSpider(scrapy.Spider):
    name = "kendal"
    start_urls = [
        "https://corona.kendalkab.go.id/"
    ]

    months = dict(Januari='01', Februari='02', Maret='03', April='04', Mei='05', Juni='06',
                  Juli='07', Agustus='08', September='09', Oktober='10', November='11', Desember='12')

    def parse(self, response):
        scrape_date = datetime.now().strftime("%Y-%m-%d")
        types = 'kecamatan'
        user_pic = 'Alfie Qashwa'
        crawl_date = response.xpath(
            '/html/body/div[1]/section[2]/div[1]/div/div/div[1]/p/text()')[4].re(r', (\w+) (\w+) (\w+)')
        day = crawl_date[0]
        month = crawl_date[1]
        year = crawl_date[2]
        date_update = year + '-' + self.months[month] + '-' + day
        provinsi = 'Jawa Tengah'
        kabkot = 'Kendal'
        kecamatan = response.xpath(
            '//*[@id="example1"]/tbody/tr/td[2]/text()').getall()
        total_odp = response.xpath(
            '//*[@id="example1"]/tbody/tr/td[5]/text()').getall()
        total_pdp = response.xpath(
            '//*[@id="example1"]/tbody/tr/td[6]/text()').getall()
        total_positif = response.xpath(
            '//*[@id="example1"]/tbody/tr/td[7]/text()').getall()
        odr_total = response.xpath(
            '//*[@id="example1"]/tbody/tr/td[4]/text()').getall()
        source_link = 'https://corona.kendalkab.go.id/'

        for q in range(len(kecamatan)):
            yield {
                'scrape_date': scrape_date,
                'types': types,
                'user_pic': user_pic,
                'date_update': date_update,
                'provinsi': provinsi,
                'kabkot': kabkot,
                'kecamatan': kecamatan[q].capitalize().strip(),
                'kelurahan': '',
                'alamat': '',
                'total_odp': total_odp[q].strip(),
                'total_pdp': total_pdp[q].strip(),
                'total_positif': total_positif[q].strip(),
                'positif_sembuh': '',
                'positif_dirawat': '',
                'positif_isolasi': '',
                'positif_meninggal': '',
                'total_otg': '',
                'odr_total': odr_total[q].strip(),
                'total_pp': '',
                'total_ppdt': '',
                'source_link': source_link,
            }


class BanjarnegaraSpider(scrapy.Spider):
    name = "banjarnegara"
    start_urls = [
        "http://corona.banjarnegarakab.go.id/"
    ]

    months = dict(Januari='01', Februari='02', Maret='03', April='04', Mei='05', Juni='06',
                  Juli='07', Agustus='08', September='09', Oktober='10', November='11', Desember='12')

    def parse(self, response):
        scrape_date = datetime.now().strftime("%Y-%m-%d")
        types = 'kelurahan'
        user_pic = 'Alfie Qashwa'
        crawl_date = response.css(
            '#sebaran .mt-2::text').re(r': (\w+) (\w+) (\w+)')
        day = crawl_date[0]
        month = self.months[crawl_date[1]]
        year = crawl_date[2]
        date_update = year + '-' + month + '-' + day
        provinsi = 'Jawa Tengah'
        kabkot = 'Banjarnegara'
        list_kecamatan = response.xpath(
            '//*[@id="accordion1"]/td[2]/text()').getall()
        banjarmangu = response.css(
            '#detail1 .align-middle:nth-child(2)::text')[2:].getall()
        banjarnegara = response.css(
            '#detail11 .align-middle:nth-child(2)::text')[2:].getall()
        batur = response.css(
            '#detail6 .align-middle:nth-child(2)::text')[2:].getall()
        bawang = response.css(
            '#detail12 .align-middle:nth-child(2)::text')[2:].getall()
        kalibening = response.css(
            '#detail4 .align-middle:nth-child(2)::text')[2:].getall()
        karangkobar = response.css(
            '#detail3 .align-middle:nth-child(2)::text')[2:].getall()
        madukara = response.css(
            '#detail10 .align-middle:nth-child(2)::text')[2:].getall()
        mandiraja = response.css(
            '#detail16 .align-middle:nth-child(2)::text')[2:].getall()
        pagedongan = response.css(
            '#detail23 .align-middle:nth-child(2)::text')[2:].getall()
        pagentan = response.css(
            '#detail8 .align-middle:nth-child(2)::text')[2:].getall()
        pandanarum = response.css(
            '#detail19 .align-middle:nth-child(2)::text')[2:].getall()
        pejawaran = response.css(
            '#detail7 .align-middle:nth-child(2)::text')[2:].getall()
        punggelan = response.css(
            '#detail18 .align-middle:nth-child(2)::text')[2:].getall()
        purwanegara = response.css(
            '#detail13 .align-middle:nth-child(2)::text')[2:].getall()
        purwarejaklampok = response.css(
            '#detail15 .align-middle:nth-child(2)::text')[2:].getall()
        rakit = response.css(
            '#detail17 .align-middle:nth-child(2)::text')[2:].getall()
        sigaluh = response.css(
            '#detail9 .align-middle:nth-child(2)::text')[2:].getall()
        susukan = response.css(
            '#detail14 .align-middle:nth-child(2)::text')[2:].getall()
        wanadadi = response.css(
            '#detail2 .align-middle:nth-child(2)::text')[2:].getall()
        wanayasa = response.css(
            '#detail5 .align-middle:nth-child(2)::text')[2:].getall()

        list_kelurahan = []
        list_kelurahan.extend(banjarmangu+banjarnegara+batur+bawang+kalibening+karangkobar+madukara+mandiraja+pagedongan +
                              pagentan+pandanarum+pejawaran+punggelan+purwanegara +
                              purwarejaklampok+rakit+sigaluh+susukan+wanadadi+wanayasa)

        odp_banjarmangu = response.css(
            '#detail1 .align-middle:nth-child(11)::text').getall()
        odp_banjarnegara = response.css(
            '#detail11 .align-middle:nth-child(11)::text').getall()
        odp_batur = response.css(
            '#detail6 .align-middle:nth-child(11)::text').getall()
        odp_bawang = response.css(
            '#detail12 .align-middle:nth-child(11)::text').getall()
        odp_kalibening = response.css(
            '#detail4 .align-middle:nth-child(11)::text').getall()
        odp_karangkobar = response.css(
            '#detail3 .align-middle:nth-child(11)::text').getall()
        odp_madukara = response.css(
            '#detail10 .align-middle:nth-child(11)::text').getall()
        odp_mandiraja = response.css(
            '#detail16 .align-middle:nth-child(11)::text').getall()
        odp_pagedongan = response.css(
            '#detail23 .align-middle:nth-child(11)::text').getall()
        odp_pagentan = response.css(
            '#detail8 .align-middle:nth-child(11)::text').getall()
        odp_pandanarum = response.css(
            '#detail19 .align-middle:nth-child(11)::text').getall()
        odp_pejawaran = response.css(
            '#detail7 .align-middle:nth-child(11)::text').getall()
        odp_punggelan = response.css(
            '#detail18 .align-middle:nth-child(11)::text').getall()
        odp_purwanegara = response.css(
            '#detail13 .align-middle:nth-child(11)::text').getall()
        odp_purwarejaklampok = response.css(
            '#detail15 .align-middle:nth-child(11)::text').getall()
        odp_rakit = response.css(
            '#detail17 .align-middle:nth-child(11)::text').getall()
        odp_sigaluh = response.css(
            '#detail9 .align-middle:nth-child(11)::text').getall()
        odp_susukan = response.css(
            '#detail14 .align-middle:nth-child(11)::text').getall()
        odp_wanadadi = response.css(
            '#detail2 .align-middle:nth-child(11)::text').getall()
        odp_wanayasa = response.css(
            '#detail5 .align-middle:nth-child(11)::text').getall()

        list_total_odp = odp_banjarmangu+odp_banjarnegara+odp_batur+odp_bawang+odp_kalibening+odp_karangkobar+odp_madukara+odp_mandiraja+odp_pagedongan + \
            odp_pagentan+odp_pandanarum+odp_pejawaran+odp_punggelan+odp_purwanegara + \
            odp_purwarejaklampok+odp_rakit+odp_sigaluh+odp_susukan+odp_wanadadi+odp_wanayasa

        # pdp_dirawat_banjarmangu = response.css(
        #     '#detail1 .align-middle:nth-child(3)::text')[2:].getall()
        # pdp_dirawat_banjarnegara = response.css(
        #     '#detail1 .align-middle:nth-child(3)::text')[2:].getall()
        # pdp_dirawat_batur = response.css(
        #     '#detail1 .align-middle:nth-child(3)::text')[2:].getall()
        # pdp_dirawat_bawang = response.css(
        #     '#detail1 .align-middle:nth-child(3)::text')[2:].getall()
        # pdp_dirawat_kalibening = response.css(
        #     '#detail1 .align-middle:nth-child(3)::text')[2:].getall()
        # pdp_dirawat_karangkobar = response.css(
        #     '#detail1 .align-middle:nth-child(3)::text')[2:].getall()
        # pdp_dirawat_madukara = response.css(
        #     '#detail1 .align-middle:nth-child(3)::text')[2:].getall()
        # pdp_dirawat_mandiraja = response.css(
        #     '#detail1 .align-middle:nth-child(3)::text')[2:].getall()
        # pdp_dirawat_pagedongan = response.css(
        #     '#detail1 .align-middle:nth-child(3)::text')[2:].getall()
        # pdp_dirawat_pagentan = response.css(
        #     '#detail1 .align-middle:nth-child(3)::text')[2:].getall()
        # pdp_dirawat_pandanarum = response.css(
        #     '#detail1 .align-middle:nth-child(3)::text')[2:].getall()
        # pdp_dirawat_pejawaran = response.css(
        #     '#detail1 .align-middle:nth-child(3)::text')[2:].getall()
        # pdp_dirawat_punggelan = response.css(
        #     '#detail1 .align-middle:nth-child(3)::text')[2:].getall()
        # pdp_dirawat_purwanegara = response.css(
        #     '#detail1 .align-middle:nth-child(3)::text')[2:].getall()
        # pdp_dirawat_purwarejaklampok = response.css(
        #     '#detail1 .align-middle:nth-child(3)::text')[2:].getall()
        # pdp_dirawat_rakit = response.css(
        #     '#detail1 .align-middle:nth-child(3)::text')[2:].getall()
        # pdp_dirawat_sigaluh = response.css(
        #     '#detail1 .align-middle:nth-child(3)::text')[2:].getall()
        # pdp_dirawat_susukan = response.css(
        #     '#detail1 .align-middle:nth-child(3)::text')[2:].getall()
        # pdp_dirawat_wanadadi = response.css(
        #     '#detail1 .align-middle:nth-child(3)::text')[2:].getall()
        # pdp_dirawat_wanayasa = response.css(
        #     '#detail1 .align-middle:nth-child(3)::text')[2:].getall()

        # pdp_sembuh_banjarmangu = response.css(
        #     '#detail1 .align-middle:nth-child(4)::text')[2:].getall()
        # pdp_sembuh_banjarnegara = response.css(
        #     '#detail1 .align-middle:nth-child(4)::text')[2:].getall()
        # pdp_sembuh_batur = response.css(
        #     '#detail1 .align-middle:nth-child(4)::text')[2:].getall()
        # pdp_sembuh_bawang = response.css(
        #     '#detail1 .align-middle:nth-child(4)::text')[2:].getall()
        # pdp_sembuh_kalibening = response.css(
        #     '#detail1 .align-middle:nth-child(4)::text')[2:].getall()
        # pdp_sembuh_karangkobar = response.css(
        #     '#detail1 .align-middle:nth-child(4)::text')[2:].getall()
        # pdp_sembuh_madukara = response.css(
        #     '#detail1 .align-middle:nth-child(4)::text')[2:].getall()
        # pdp_sembuh_mandiraja = response.css(
        #     '#detail1 .align-middle:nth-child(4)::text')[2:].getall()
        # pdp_sembuh_pagedongan = response.css(
        #     '#detail1 .align-middle:nth-child(4)::text')[2:].getall()
        # pdp_sembuh_pagentan = response.css(
        #     '#detail1 .align-middle:nth-child(4)::text')[2:].getall()
        # pdp_sembuh_pandanarum = response.css(
        #     '#detail1 .align-middle:nth-child(4)::text')[2:].getall()
        # pdp_sembuh_pejawaran = response.css(
        #     '#detail1 .align-middle:nth-child(4)::text')[2:].getall()
        # pdp_sembuh_punggelan = response.css(
        #     '#detail1 .align-middle:nth-child(4)::text')[2:].getall()
        # pdp_sembuh_purwanegara = response.css(
        #     '#detail1 .align-middle:nth-child(4)::text')[2:].getall()
        # pdp_sembuh_purwarejaklampok = response.css(
        #     '#detail1 .align-middle:nth-child(4)::text')[2:].getall()
        # pdp_sembuh_rakit = response.css(
        #     '#detail1 .align-middle:nth-child(4)::text')[2:].getall()
        # pdp_sembuh_sigaluh = response.css(
        #     '#detail1 .align-middle:nth-child(4)::text')[2:].getall()
        # pdp_sembuh_susukan = response.css(
        #     '#detail1 .align-middle:nth-child(4)::text')[2:].getall()
        # pdp_sembuh_wanadadi = response.css(
        #     '#detail1 .align-middle:nth-child(4)::text')[2:].getall()
        # pdp_sembuh_wanayasa = response.css(
        #     '#detail1 .align-middle:nth-child(4)::text')[2:].getall()

        # pdp_meninggal_banjarmangu = response.css(
        #     '#detail1 .align-middle:nth-child(5)::text')[2:].getall()
        # pdp_meninggal_banjarnegara = response.css(
        #     '#detail1 .align-middle:nth-child(5)::text')[2:].getall()
        # pdp_meninggal_batur = response.css(
        #     '#detail1 .align-middle:nth-child(5)::text')[2:].getall()
        # pdp_meninggal_bawang = response.css(
        #     '#detail1 .align-middle:nth-child(5)::text')[2:].getall()
        # pdp_meninggal_kalibening = response.css(
        #     '#detail1 .align-middle:nth-child(5)::text')[2:].getall()
        # pdp_meninggal_karangkobar = response.css(
        #     '#detail1 .align-middle:nth-child(5)::text')[2:].getall()
        # pdp_meninggal_madukara = response.css(
        #     '#detail1 .align-middle:nth-child(5)::text')[2:].getall()
        # pdp_meninggal_mandiraja = response.css(
        #     '#detail1 .align-middle:nth-child(5)::text')[2:].getall()
        # pdp_meninggal_pagedongan = response.css(
        #     '#detail1 .align-middle:nth-child(5)::text')[2:].getall()
        # pdp_meninggal_pagentan = response.css(
        #     '#detail1 .align-middle:nth-child(5)::text')[2:].getall()
        # pdp_meninggal_pandanarum = response.css(
        #     '#detail1 .align-middle:nth-child(5)::text')[2:].getall()
        # pdp_meninggal_pejawaran = response.css(
        #     '#detail1 .align-middle:nth-child(5)::text')[2:].getall()
        # pdp_meninggal_punggelan = response.css(
        #     '#detail1 .align-middle:nth-child(5)::text')[2:].getall()
        # pdp_meninggal_purwanegara = response.css(
        #     '#detail1 .align-middle:nth-child(5)::text')[2:].getall()
        # pdp_meninggal_purwarejaklampok = response.css(
        #     '#detail1 .align-middle:nth-child(5)::text')[2:].getall()
        # pdp_meninggal_rakit = response.css(
        #     '#detail1 .align-middle:nth-child(5)::text')[2:].getall()
        # pdp_meninggal_sigaluh = response.css(
        #     '#detail1 .align-middle:nth-child(5)::text')[2:].getall()
        # pdp_meninggal_susukan = response.css(
        #     '#detail1 .align-middle:nth-child(5)::text')[2:].getall()
        # pdp_meninggal_wanadadi = response.css(
        #     '#detail1 .align-middle:nth-child(5)::text')[2:].getall()
        # pdp_meninggal_wanayasa = response.css(
        #     '#detail1 .align-middle:nth-child(5)::text')[2:].getall()

        # total_pdp_banjarmangu = int(
        #     pdp_dirawat_banjarmangu)+int(pdp_sembuh_banjarmangu)+int(pdp_meninggal_banjarmangu)
        # total_pdp_banjarnegara = int(
        #     pdp_dirawat_banjarnegara)+int(pdp_sembuh_banjarnegara)+int(pdp_meninggal_banjarnegara)
        # total_pdp_batur = int(
        #     pdp_dirawat_batur)+int(pdp_sembuh_batur)+int(pdp_meninggal_batur)
        # total_pdp_bawang = int(
        #     pdp_dirawat_bawang)+int(pdp_sembuh_bawang)+int(pdp_meninggal_bawang)
        # total_pdp_kalibening = int(
        #     pdp_dirawat_kalibening)+int(pdp_sembuh_kalibening)+int(pdp_meninggal_kalibening)
        # total_pdp_karangkobar = int(
        #     pdp_dirawat_karangkobar)+int(pdp_sembuh_karangkobar)+int(pdp_meninggal_karangkobar)
        # total_pdp_madukara = int(
        #     pdp_dirawat_madukara)+int(pdp_sembuh_madukara)+int(pdp_meninggal_madukara)
        # total_pdp_mandiraja = int(
        #     pdp_dirawat_mandiraja)+int(pdp_sembuh_mandiraja)+int(pdp_meninggal_mandiraja)
        # total_pdp_pagedongan = int(
        #     pdp_dirawat_pagedongan)+int(pdp_sembuh_pagedongan)+int(pdp_meninggal_pagedongan)
        # total_pdp_pagentan = int(
        #     pdp_dirawat_pagentan)+int(pdp_sembuh_pagentan)+int(pdp_meninggal_pagentan)
        # total_pdp_pandanarum = int(
        #     pdp_dirawat_pandanarum)+int(pdp_sembuh_pandanarum)+int(pdp_meninggal_pandanarum)
        # total_pdp_pejawaran = int(
        #     pdp_dirawat_pejawaran)+int(pdp_sembuh_pejawaran)+int(pdp_meninggal_pejawaran)
        # total_pdp_punggelan = int(
        #     pdp_dirawat_punggelan)+int(pdp_sembuh_punggelan)+int(pdp_meninggal_punggelan)
        # total_pdp_purwanegara = int(
        #     pdp_dirawat_purwanegara)+int(pdp_sembuh_purwanegara)+int(pdp_meninggal_purwanegara)
        # total_pdp_purwarejaklampok = int(
        #     pdp_dirawat_purwarejaklampok)+int(pdp_sembuh_purwarejaklampok)+int(pdp_meninggal_purwarejaklampok)
        # total_pdp_rakit = int(
        #     pdp_dirawat_rakit)+int(pdp_sembuh_rakit)+int(pdp_meninggal_rakit)
        # total_pdp_sigaluh = int(
        #     pdp_dirawat_sigaluh)+int(pdp_sembuh_sigaluh)+int(pdp_meninggal_sigaluh)
        # total_pdp_susukan = int(
        #     pdp_dirawat_susukan)+int(pdp_sembuh_susukan)+int(pdp_meninggal_susukan)
        # total_pdp_wanadadi = int(
        #     pdp_dirawat_wanadadi)+int(pdp_sembuh_wanadadi)+int(pdp_meninggal_wanadadi)
        # total_pdp_wanayasa = int(
        #     pdp_dirawat_wanayasa)+int(pdp_sembuh_wanayasa)+int(pdp_meninggal_wanayasa)

        # list_total_pdp = total_pdp_banjarmangu+total_pdp_banjarnegara+total_pdp_batur + \
        #     total_pdp_bawang+total_pdp_kalibening+total_pdp_karangkobar+total_pdp_madukara+total_pdp_mandiraja+total_pdp_pagedongan+total_pdp_pagentan+total_pdp_pandanarum + \
        #     total_pdp_pejawaran+total_pdp_punggelan+total_pdp_purwanegara+total_pdp_purwarejaklampok + \
        #     total_pdp_rakit+total_pdp_sigaluh+total_pdp_susukan + \
        #     total_pdp_wanadadi+total_pdp_wanayasa
        source_link = 'http://corona.banjarnegarakab.go.id/'

        for q in range(len(list_kelurahan)):
            kelurahan = list_kelurahan[q]

            # why there is no switch-case in Python?!
            if kelurahan in banjarmangu:
                kecamatan = list_kecamatan[0]
            elif kelurahan in banjarnegara:
                kecamatan = list_kecamatan[1]
            elif kelurahan in batur:
                kecamatan = list_kecamatan[2]
            elif kelurahan in bawang:
                kecamatan = list_kecamatan[3]
            elif kelurahan in kalibening:
                kecamatan = list_kecamatan[4]
            elif kelurahan in karangkobar:
                kecamatan = list_kecamatan[5]
            elif kelurahan in madukara:
                kecamatan = list_kecamatan[6]
            elif kelurahan in mandiraja:
                kecamatan = list_kecamatan[7]
            elif kelurahan in pagedongan:
                kecamatan = list_kecamatan[8]
            elif kelurahan in pagentan:
                kecamatan = list_kecamatan[9]
            elif kelurahan in pandanarum:
                kecamatan = list_kecamatan[10]
            elif kelurahan in pejawaran:
                kecamatan = list_kecamatan[11]
            elif kelurahan in punggelan:
                kecamatan = list_kecamatan[12]
            elif kelurahan in purwanegara:
                kecamatan = list_kecamatan[13]
            elif kelurahan in purwarejaklampok:
                kecamatan = list_kecamatan[14]
            elif kelurahan in rakit:
                kecamatan = list_kecamatan[15]
            elif kelurahan in sigaluh:
                kecamatan = list_kecamatan[16]
            elif kelurahan in susukan:
                kecamatan = list_kecamatan[17]
            elif kelurahan in wanadadi:
                kecamatan = list_kecamatan[18]
            elif kelurahan in wanayasa:
                kecamatan = list_kecamatan[19]
            else:
                kecamatan = ''

            total_odp = list_total_odp[q]
            # total_pdp = list_total_pdp[q]
            yield {
                'scrape_date': scrape_date,
                'types': types,
                'user_pic': user_pic,
                'date_update': date_update,
                'provinsi': provinsi,
                'kabkot': kabkot,
                'kecamatan': kecamatan.strip().capitalize(),
                'kelurahan': kelurahan.strip().capitalize(),
                'alamat': '',
                'total_odp': total_odp,
                'total_pdp': '',
                'source_link': source_link
            }
