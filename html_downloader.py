import urllib.request

class HtmlDownloader(object):
    def download(self, url):
        if url is None:
            return None
        reponse = urllib.request.urlopen(url)

        if reponse.getcode() != 200:
            return None
        return reponse.read()