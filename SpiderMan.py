# coding = utf-8
import DataOutput
import HtmlDownloader
import HtmlParser
import URLManager


class SpiderMan(object):
    def __init__(self):
        self.manager = URLManager.UrlManager()
        self.downloader = HtmlDownloader.HtmlDownloader()
        self.parser = HtmlParser.HtmlParser()
        self.output = DataOutput.DataOutput()

    def crawl(self, root_url):
        self.manager.add_new_url(root_url)
        while (self.manager.has_new_url() and self.manager.old_url_size() < 100):
            try:
                new_url = self.manager.get_new_url()
                html = self.downloader.download(new_url)
                new_urls,data = self.parser(new_url)
                self.manager.add_new_url(new_urls)
                self.output.store_data(data)
                print('已经抓取了{}个连接'.format(self.manager.old_url_size()))
            except Exception:
                print('爬取失败')
        self.output.output_html()


if __name__ == '__main__':
    spider_man = SpiderMan()
    spider_man.crawl("https://baike.baidu.com/item/%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB")
# git test