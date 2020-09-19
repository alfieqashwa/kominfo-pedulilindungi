import scrapy
from datetime import datetime


class BoyolaliSpider(scrapy.Spider):
    name = "boyolali"
    start_urls = [
        "https://covid19.boyolali.go.id/"
        # "https://quotes.toscrape.com/"
    ]

    def parse(self, response):
        scrape_date = datetime.now().strftime("%Y-%m-%d")
        types = 'kabupaten'
        user_pic = 'Alfie Qashwa'
        date_update = response.xpath(
            '//*[@id="why-us"]/div[1]/header/p/text()').extract_first().split()[5].replace('-', '/')
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
