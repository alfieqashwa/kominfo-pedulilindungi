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
        date_update = datetime.now().strftime('%d/%m/%Y')
        provinsi = 'Jawa Tengah'
        kabkot = 'Semarang'
        # dupl_kec = response.xpath(
        #     '//*[@id="example1"]/tbody/tr/td[2]/text()').extract()
        # kecamatan = list(dict.fromkeys(dupl_kec))
        kecamatan = None
        kelurahan = None
        alamat = None
        total_odp = response.xpath(
            '//*[@id="main-wrapper"]/div[2]/div[2]/div[1]/div[5]/div/div/div[1]/div[2]/div/text()').extract_first()
        t_pdp = response.xpath(
            '//*[@id="main-wrapper"]/div[2]/div[2]/div[1]/div[6]/div/div/div[1]/div[2]/div/text()')[1].extract()
        total_pdp = t_pdp.strip('\r\n ')
        total_positif = None
        positif_sembuh = response.xpath(
            '//*[@id="main-wrapper"]/div[2]/div[2]/div[1]/div[3]/div/div/div[1]/div[2]/div/text()').extract_first()
        positif_dirawat = response.xpath(
            '//*[@id="main-wrapper"]/div[2]/div[2]/div[1]/div[2]/div/div/div[1]/div[2]/div/text()').extract_first()
        positif_isolasi = None
        positif_meninggal = response.xpath(
            '//*[@id="main-wrapper"]/div[2]/div[2]/div[1]/div[4]/div/div/div[1]/div[2]/div/text()').extract_first()
        total_otg = None
        odr_total = None
        total_pp = None
        total_ppdt = None
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


# this site is using a fuckin' ReactJS
class PurbalinggaSpider(scrapy.Spider):
    name = 'purbalingga'
    start_urls = [
        "https://corona.purbalinggakab.go.id/"
    ]

    def parse(self, response):
        scrape_date = datetime.now().strftime("%Y-%m-%d")
        types = 'kabupaten'
        user_pic = 'Alfie Qashwa'
        date_update = datetime.now().strftime('%d/%m/%Y')
        provinsi = 'Jawa Tengah'
        kabkot = 'Purbalingga'
        kecamatan = None
        kelurahan = None
        alamat = None
        t_odp = response.xpath(
            '//*[@id="et-boc"]/div/div[3]/div[2]/div[1]/div[5]/div/ul/li[2]/text()').extract_first()
        total_odp = t_odp.split()[3]
        t_pdp = response.xpath(
            '//*[@id="et-boc"]/div/div[3]/div[2]/div[2]/div[4]/div/ul/li[3]/b[2]/text()').extract_first()
        total_pdp = t_pdp.split()[2]
        t_positif = response.xpath(
            '//*[@id="et-boc"]/div/div[3]/div[2]/div[3]/div[5]/div/ul/li[3]/strong/text()').extract_first()
        total_positif = t_positif.split()[4]
        p_sembuh = response.xpath(
            '//*[@id="et-boc"]/div/div[3]/div[2]/div[3]/div[5]/div/ul/li[1]/b[1]/text()').extract_first()
        positif_sembuh = p_sembuh.split()[2]
        positif_isolasi = None
        p_meninggal = response.xpath(
            '//*[@id="et-boc"]/div/div[3]/div[2]/div[3]/div[5]/div/ul/li[2]/b[1]/text()').extract_first()
        positif_meninggal = p_meninggal.split()[2]
        p_int_dirawat = int(total_positif) - \
            (int(positif_sembuh) + int(positif_meninggal))
        positif_dirawat = str(p_int_dirawat)
        total_otg = None
        odr_total = None
        total_pp = None
        total_ppdt = None
        source_link = 'https://corona.purbalinggakab.go.id/'

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

# Kecamatan


class KudusSpider(scrapy.Spider):
    name = "kudus"
    start_urls = [
        "https://corona.kuduskab.go.id/"
    ]
    # convert months string into number
    months = dict(Januari='1', Februari='2', Maret='3', April='4', Mei='5', Juni='6',
                  Juli='7', Agustus='8', September='9', Oktober='10', November='11', Desember='12')

    def parse(self, response):
        scrape_date = datetime.now().strftime("%Y-%m-%d")
        types = "kecamatan"
        user_pic = "Alfie Qashwa"
        crawl_date = response.xpath(
            '//*[@id="monitoring"]/div/div/div/div/div[1]/span/text()').extract_first()
        day = crawl_date[18:20]
        month = crawl_date[21:30]
        year = crawl_date[31:35]
        date_update = day + '/' + self.months[month] + '/' + year
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

        for i in range(len(kecamatan)):
            yield {
                'scrape_date': scrape_date,
                'types': types,
                'user_pic': user_pic,
                'date_update': date_update,
                'provinsi': provinsi,
                'kabkot': kabkot,
                'kecamatan': kecamatan[i],
                'kelurahan': kelurahan,
                'alamat': alamat,
                'total_odp': total_odp[i],
                'total_pdp': total_pdp[i],
                'total_positif': total_positif[i],
                'positif_sembuh': positif_sembuh[i],
                'positif_dirawat': positif_dirawat[i],
                'positif_isolasi': positif_isolasi[i],
                'positif_meninggal': positif_meninggal[i],
                'total_otg': total_otg,
                'odr_total': odr_total[i],
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
        date_update = datetime.now().strftime("%d/%m/%Y")
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

        for i in range(len(kecamatan)):
            yield {
                'scrape_date': scrape_date,
                'types': types,
                'user_pic': user_pic,
                'date_update': date_update,
                'provinsi': provinsi,
                'kabkot': kabkot,
                'kecamatan': kecamatan[i],
                'kelurahan': kelurahan,
                'alamat': alamat,
                'total_odp': total_odp[i],
                'total_pdp': total_pdp,
                'total_positif': total_positif[i],
                'positif_sembuh': positif_sembuh[i],
                'positif_dirawat': positif_dirawat[i],
                'positif_isolasi': positif_isolasi,
                'positif_meninggal': positif_meninggal[i],
                'total_otg': total_otg,
                'odr_total': odr_total[i],
                'total_pp': total_pp,
                'total_ppdt': total_ppdt,
                'source_link': source_link,
            }
