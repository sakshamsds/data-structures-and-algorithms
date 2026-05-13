# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        hostname = startUrl.split('/')[2]
        allUrls = set()

        def dfs(curUrl):
            allUrls.add(curUrl)
            for nbr in htmlParser.getUrls(curUrl):
                if nbr not in allUrls and hostname == nbr.split('/')[2]:
                    dfs(nbr)

        dfs(startUrl)
        return list(allUrls)