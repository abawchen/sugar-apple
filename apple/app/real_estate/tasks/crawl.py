
import datetime
import os
import os.path
import subprocess

import luigi

class SinyiCrawlCityTask(luigi.Task):
    # PYTHONPATH=. luigi --module tasks.crawl SinyiCrawlCityTask --local-scheduler --city Taipei-city

    date = luigi.DateParameter(default=datetime.date.today())
    city = luigi.Parameter()

    def output(self):
        output_path = os.path.join(
            "data", "{}-{}.jsonl".format(self.date, self.city))
        return luigi.LocalTarget(output_path)

    def run(self):
        tmp_output_path = ".tmp" + self.output().path
        command = [
            "scrapy", "crawl", "sinyi",
            "-a", "city={}".format(self.city),
            "-o", tmp_output_path,
            "-t", "jl",
            "--logfile", "{}-sinyi-{}.log".format(self.date, self.city.lower()),
            "--loglevel", "DEBUG"
        ]
        print(" ".join(command))
        subprocess.check_output(command)
        os.rename(tmp_output_path, self.output().path)


class SinyiCrawlTask(luigi.WrapperTask):
    # PYTHONPATH=. luigi --module tasks.crawl SinyiCrawlTask --local-scheduler

    date = luigi.DateParameter(default=datetime.date.today())

    def requires(self):
        cities = [
            'Taipei-city', 'NewTaipei-city', 'Taoyuan-city',
            'Hsinchu-city', 'Hsinchu-county', 'Keelung-city',
            'Taichung-city', 'Changhua-county', 'Miaoli-county',
            'Nantou-county', 'Yunlin-county',
            'Kaoshiung-city', 'Tainan-city', 'Chiayi-city',
            'Chiayi-county', 'Pingtung-county',
            'Yilan-county', 'Hualien-city', 'Taitung-county',
            'Penghu-county', 'Kinmen-county'
        ]
        for city in cities:
            yield SinyiCrawlCityTask(self.date, city)


class YungchingCrawlTask(luigi.Task):

    date = luigi.DateParameter(default=datetime.date.today())


if __name__ == "__main__":
    luigi.run()