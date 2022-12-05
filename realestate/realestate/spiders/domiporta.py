import scrapy
from bs4 import BeautifulSoup
import requests
import re


class DomiportaSpider(scrapy.Spider):
    name = "domiporta"
    allowed_domains = ["domiporta.pl"]
    start_urls = ["https://www.domiporta.pl/mieszkanie/sprzedam"]

    def parse(self, response):
        soup = BeautifulSoup(response.text, "lxml")
        next_page_url = self.get_next_page(soup)
        if next_page_url:
            yield scrapy.Request(next_page_url)
            for li in soup.find_all("li", {"class": "grid-item grid-item--cover"}):
                offer_link = "https://www.domiporta.pl" + li.find(
                    "a", {"class": "sneakpeak__title"}
                ).get("href")
                offer_soup = self.html_access(offer_link)
                condition = offer_soup.find(
                    "span",
                    {"class": "features__item_value features__item_value--price"},
                )
                yield {
                    "price": "" if not condition else condition.get_text(strip=True),
                    "material": ""
                    if not offer_soup.find("span", string=re.compile("Materiał"))
                    else offer_soup.find("span", string=re.compile("Materiał"))
                    .find_next("span")
                    .get_text(),
                    "offer_name": ""
                    if not offer_soup.find("span", string=re.compile("Numer oferty"))
                    else offer_soup.find("span", string=re.compile("Numer oferty"))
                    .find_next("span")
                    .get_text(),
                    "construction_year": ""
                    if not offer_soup.find("span", string=re.compile("Rok budowy"))
                    else offer_soup.find("span", string=re.compile("Rok budowy"))
                    .find_next("span")
                    .get_text(),
                    "square_footage": ""
                    if not offer_soup.find(
                        "span", string=re.compile("Powierzchnia całkowita")
                    )
                    else offer_soup.find(
                        "span", string=re.compile("Powierzchnia całkowita")
                    )
                    .find_next("span")
                    .get_text(),
                    "number_of_rooms": ""
                    if not offer_soup.find("span", string=re.compile("Liczba pokoi"))
                    else offer_soup.find("span", string=re.compile("Liczba pokoi"))
                    .find_next("span")
                    .get_text(),
                    "price_per_m2": ""
                    if not soup.find(
                        "span",
                        {
                            "class": "sneakpeak__details_item sneakpeak__details_item--price"
                        },
                    )
                    else soup.find(
                        "span",
                        {
                            "class": "sneakpeak__details_item sneakpeak__details_item--price"
                        },
                    )
                    .get_text()
                    .strip()
                    .replace("\xa0", "")
                    .replace("zł/m2", ""),
                    "city": ""
                    if not offer_soup.find("span", itemprop="addressLocality")
                    else offer_soup.find("span", itemprop="addressLocality").get_text(),
                    "address": ""
                    if not offer_soup.find("span", itemprop="streetAddress")
                    else offer_soup.find("span", itemprop="streetAddress").get_text(),
                    "region": ""
                    if not offer_soup.find("meta", itemprop="addressRegion")
                    else offer_soup.find("meta", itemprop="addressRegion")["content"],
                }

    def get_next_page(self, soup):
        next_page = soup.find(
            "li", {"class": "pagination__link pagination__link--right"}
        ).a.get("href")
        if next_page is None:
            return None
        next_url = "https://www.domiporta.pl" + next_page
        return next_url

    def html_access(self, url):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
        }
        r = requests.get(url, headers=headers)
        soup = BeautifulSoup(r.content, "lxml")
        return soup
