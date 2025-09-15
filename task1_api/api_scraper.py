import json
import logging

import requests


logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s - %(message)s",
    handlers=[logging.StreamHandler()]
)


class JobScraper:
    BASE_URL = "https://careers.ef.com"
    API_URL_TEMPLATE = (
        "https://www.ef.com/central-api/careers/job/v2/getjobs/we/"
        "?pageIndex={page}&pageSize=50&sortColumn=0"
    )

    def __init__(self):
        self.jobs = []

    def fetch_all_jobs(self):
        page = 1
        while True:
            url = self.API_URL_TEMPLATE.format(page=page)
            logging.info(f"Fetching page {page}...")
            response = requests.get(url)
            if response.status_code != 200:
                logging.error(
                    f"Failed to fetch page {page}: {response.status_code}"
                )
                break

            data = response.json()

            jobs = data.get("jobs", [])
            if not jobs:
                break

            self.jobs.extend(jobs)
            page += 1

        logging.info(f"Total jobs fetched: {len(self.jobs)}")

    def process_jobs(self):
        for job in self.jobs:
            job.pop("image", None)
            job["jobUrl"] = self.BASE_URL + job["jobUrl"]

    def save_to_json(self, filename="task1_results.json"):
        final_data = {"jobs": self.jobs}
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(final_data, f, ensure_ascii=False, indent=4)
        logging.info(f"Job data successfully saved to {filename}.")

    def run(self):
        self.fetch_all_jobs()
        self.process_jobs()
        self.save_to_json()


def main():
    scraper = JobScraper()
    scraper.run()


if __name__ == "__main__":
    main()
