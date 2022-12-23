# libs
import logging
from bs4 import BeautifulSoup

# module
from src.tools.HttpClient import HttpClient
from src.models.Location import Location


class SiteMapParser:

  http: HttpClient
  stmp_url: str
  root_url: str

  def __init__(self, url: str, root_url: str) -> None:
    self.http = HttpClient
    self.stmp_url = url
    self.root_url = root_url

  async def get_stmp_location(self) -> list[str]:
    response = self.http.get(self.stmp_url)
    soup = BeautifulSoup(response, features='xml')

    return [el.text for el in soup.findAll('loc')]

  async def check_location_stmp(self, stmp_loc: list[str]) -> dict:
    location_store_available: list[Location] = []
    location_store_unavailable: list[Location] = []

    responses = self.http.get_status_req(stmp_loc)
    
    for response in responses:
      if response.ok:
        location_store_available.append((response.url, True)); continue
      location_store_unavailable.append((response.url, False))

    return {
      'available': location_store_available,
      'unavailable': location_store_unavailable,
    }
    
