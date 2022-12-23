# libs
import logging
import re

# module
from src.tools.HttpClient import HttpClient
from src.tools.Config import Config


class Location:
  __slots__ = ('url', 'ok')

  def __init__(self, url: str, ok: bool) -> None:
    self.url = url; self.ok = ok

  def __repr__(self) -> str:
    return f'{self.url} -> {self.ok}'


class RobotsParser:
  http: HttpClient
  robots_url: str
  root_url: str

  def __init__(self, url: str, root_url: str) -> None:
    self.http = HttpClient
    self.robots_url = url
    self.root_url = root_url

  async def _pars_text(self, data: str) -> list[str]:
    try:
      return {
        'disallow': [*map(lambda el: el.strip(), re.findall(r'Disallow: ([\s\S]+?)\n', data))],
        'allow': [*map(lambda el: el.strip(), re.findall(r'Allow: ([\s\S]+?)\n', data))]
      }
    except Exception as ex:
      logging.info(ex)
      exit()

  async def get_robots(self):
    results = self.http.get(self.robots_url)
    pars_config = await self._pars_text(results)

    return pars_config

  async def check_loc(self, allow_loc: list[str]) -> dict:

    location_store_available: list[Location] = []
    location_store_unavailable: list[Location] = []

    responses = self.http.get_status_greq(allow_loc, self.root_url)
    
    for response in responses:
      if response.ok:
        location_store_available.append((response.url, True)); continue
      location_store_unavailable.append((response.url, False))

    return {
      'available': location_store_available,
      'unavailable': location_store_unavailable,
    }