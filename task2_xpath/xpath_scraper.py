import json

import requests
from lxml import html


URL = (
    "https://marketdino.pl/kariera/wyniki?page=1&page_size=32"
)


class AddressScraper:
    def __init__(self, url):
        self.url = url
        self.result = []

    def fetch(self):
        response = requests.get(self.url)
        tree = html.fromstring(response.content)
        job_cards = tree.xpath(
            "//div[contains(@class, 'job-offer-card relative items-start "
            "justify-between')]"
        )
        for card in job_cards:
            bottom = card.xpath(
                ".//div[contains(@class, 'job-offer-card-bottom')]"
            )
            if not bottom:
                continue
            bottom = bottom[0]
            address_parts = bottom.xpath(
                ".//span[@class='block' or @class='block text-xs']"
            )
            address = ", ".join(
                part.text_content().strip()
                for part in address_parts
                if part.text_content().strip()
            )
            if address:
                self.result.append(address)

    def save_to_json(self, filename="task2_results.json"):
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(self.result, f, ensure_ascii=False, indent=4)


def main():
    scraper = AddressScraper(URL)
    scraper.fetch()
    scraper.save_to_json()


if __name__ == "__main__":
    main()
