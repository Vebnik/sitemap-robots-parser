# libs
import logging
import re
import pprint as pp

# module
from src.tools.HttpClient import HttpClient


class RobotsParser:

  http: HttpClient

  def __init__(self, url: str) -> None:
    self.http = HttpClient(url)


  def _pars_text(self, data: str) -> list[str]:
    try:
      return {
        'disallow': [*map(lambda el: el.strip(), re.findall(r'Disallow: ([\s\S]+?)\n', data))],
        'allow': [*map(lambda el: el.strip(), re.findall(r'Allow: ([\s\S]+?)\n', data))]
      }
    except Exception as ex:
      logging.info(ex)
      exit()


  def check_robots(self):
    results = self.http.get()
    pars_config = self._pars_text(results)

    pp.pprint(pars_config.get('allow'))