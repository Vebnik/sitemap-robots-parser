# libs
import logging
import re
import pprint as pp

# module
from src.tools.HttpClient import HttpClient


class SiteMapParser:

  http: HttpClient

  def __init__(self, url: str) -> None:
    self.http = HttpClient(url)


  def _pars_xml(self, data: str) -> list[str]:
    try:
      return {
        'sitemap_index': re.findall(r'sitemapindex xmlns="([\s\S]+?)"', data),
        'loc': re.findall(r'<loc>([\s\S]+?)</loc>', data)
      }
    except Exception as ex:
      logging.info(ex)
      exit()


  def check_map(self):
    results = self.http.get()
    pars_config = self._pars_xml(results)

    pp.pprint(pars_config)

