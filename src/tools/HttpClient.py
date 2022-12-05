import requests as req
import logging


class HttpClient:

  url: str = None

  def __init__(self, url: str) -> None:
    self.url = url


  def get(self):
    try:
      response = req.get(self.url)

      if response.status_code < 300:
        return response.text
      
      raise f'Response code: {response.status_code}'
    except Exception as ex:
      logging.critical(ex)
      exit()
