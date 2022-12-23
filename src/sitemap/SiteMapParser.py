# libs
import logging
import re
from bs4 import BeautifulSoup

# module
from src.tools.HttpClient import HttpClient


class SiteMapParser:

  http: HttpClient
  stmp_url: str
  root_url: str

  def __init__(self, url: str, root_url: str) -> None:
    self.http = HttpClient
    self.stmp_url = url
    self.root_url = root_url

  def _pars_xml(self, data: str) -> dict:
    try:
      return {
        'sitemap_index': re.findall(r'sitemapindex xmlns="([\s\S]+?)"', data),
        'loc': re.findall(r'<loc>([\s\S]+?)</loc>', data)
      }
    except Exception as ex:
      logging.info(ex)
      exit()

  async def get_stmp_location(self):
    results = self.http.get(self.stmp_url)
    pars_config = self._pars_xml(results)

    return pars_config

  async def get_subloc(self, location: str) -> list[str]:
    response = self.http.get(location)
    soup = BeautifulSoup(response, features='lxml')
    
    find_loc = [el.text for el in soup.findAll('loc')]

    print(find_loc)
    exit()

  async def check_location_stmp(self, stmp_loc: list[str]) -> None:

    for location in stmp_loc:
      sub_loc = await self.get_subloc(location)
      self.http.get_status_greq(sub_loc)

