from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from models import Parser


def main():
    parser = Parser()
    args = parser.get_args()
    QUERY = "%20".join(args.query)
    STORES = parser.get_store(args)
    print(STORES)

    settings = get_project_settings()

    process = CrawlerProcess(settings)
    for STORE in STORES:
        process.crawl(STORE, query=QUERY)
    process.start()


if __name__ == "__main__":
    main()
