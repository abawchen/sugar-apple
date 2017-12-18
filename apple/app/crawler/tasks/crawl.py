
import datetime
import os
import os.path
import subprocess

import luigi


def createFolderIfNotExist(path):
     if not os.path.exists(path):
        os.makedirs(path)

class SinyiCrawlCityTask(luigi.Task):
    """
    PYTHONPATH=. luigi --module tasks.crawl SinyiCrawlCityTask --local-scheduler --city Taipei-city
    """

    date = luigi.DateParameter(default=datetime.date.today())
    city = luigi.Parameter()

    def output(self):
        output_path = os.path.join(
            "data", str(self.date), "{}-sinyi-{}.jsonl".format(self.date, self.city.lower()))
        return luigi.LocalTarget(output_path)

    def run(self):
        tmp_output_path = ".tmp" + self.output().path
        command = [
            "scrapy", "crawl", "sinyi",
            "-a", "city={}".format(self.city),
            "-o", tmp_output_path,
            "-t", "jl",
            "--logfile", "{}-sinyi-{}.log".format(self.date, self.city.lower()),
            "--loglevel", "ERROR"
        ]
        subprocess.check_output(command)
        createFolderIfNotExist(os.path.join("data", str(self.date)))
        os.rename(tmp_output_path, self.output().path)


class SinyiCrawlTask(luigi.WrapperTask):
    """
    $ PYTHONPATH=. luigi --module tasks.crawl SinyiCrawlTask --local-scheduler
    """

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
    """
    PYTHONPATH=. luigi --module tasks.crawl YungchingCrawlTask --local-scheduler
    """

    date = luigi.DateParameter(default=datetime.date.today())

    def output(self):
        output_path = os.path.join(
            "data", str(self.date), "{}-yungching.jsonl".format(self.date))
        return luigi.LocalTarget(output_path)

    def run(self):
        tmp_output_path = ".tmp" + self.output().path
        command = [
            "scrapy", "crawl", "yungching",
            "-o", tmp_output_path,
            "-t", "jl",
            "--logfile", "{}-yungching.log".format(self.date),
            "--loglevel", "ERROR"
        ]
        print(' '.join(command))
        subprocess.check_output(command)
        createFolderIfNotExist(os.path.join("data", str(self.date)))
        os.rename(tmp_output_path, self.output().path)


class AgentCrawlTask(luigi.WrapperTask):
    """
    PYTHONPATH=. luigi --module tasks.crawl AgentCrawlTask --local-scheduler
    """

    date = luigi.DateParameter(default=datetime.date.today())

    def requires(self):
        path = os.path.join("data", str(self.date))
        createFolderIfNotExist(path)

        yield SinyiCrawlTask(self.date)
        yield YungchingCrawlTask(self.date)

if __name__ == "__main__":
    luigi.run()
