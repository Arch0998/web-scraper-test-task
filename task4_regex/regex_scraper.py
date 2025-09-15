import re
import json


class RegexScraper:
    def __init__(self, input_file):
        self.input_file = input_file
        self.text = self.read_file()
        self.urls = []
        self.emails = []
        self.bots = []
        self.parentheses = []

    def read_file(self):
        with open(self.input_file, "r", encoding="utf-8") as f:
            return f.read()

    def find_urls(self):
        self.urls = [
            url.rstrip(".")
            for url in re.findall(r'https?://\S+', self.text)
        ]

    def find_emails(self):
        self.emails = re.findall(r'\b[\w.-]+@[\w.-]+\.\w+\b', self.text)

    def find_bots(self):
        self.bots = re.findall(r'@\w+_bot', self.text)

    def find_parentheses(self):
        self.parentheses = re.findall(r'\((.*?)\)', self.text)

    def save_to_json(self, filename="task4_results.json"):
        output_data = {
            "urls": self.urls,
            "emails": self.emails,
            "bots": self.bots,
            "parentheses": self.parentheses
        }
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(output_data, f, ensure_ascii=False, indent=4)


def main():
    scraper = RegexScraper("text.txt")
    scraper.find_urls()
    scraper.find_emails()
    scraper.find_bots()
    scraper.find_parentheses()
    scraper.save_to_json()


if __name__ == "__main__":
    main()
