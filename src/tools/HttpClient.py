# libs
import grequests
from requests import Response
import requests as req
import logging

# module
from src.tools.PrettyLoging import PrettyLoging


class HttpClient:

  @staticmethod
  def get(url: str) -> str:
    try:
      response = req.get(url)

      if response.status_code < 300:
        return response.text

      raise f'Response code: {response.status_code}'
    except Exception as ex:
      logging.critical(ex)
      exit()

  @staticmethod
  def get_status(url: str) -> int:
    try:
      response = req.get(url)

      return response.status_code
    except Exception as ex:
      logging.critical(ex)
      exit()

  @staticmethod
  def get_status_greq(urls: list[str], root_url: str = '') -> list[Response]:

    computed_responses = (grequests.get(f'{root_url}{loc}') for loc in urls)
    completed_response = grequests.map(computed_responses)

    return completed_response

  @staticmethod
  def get_status_req(urls: list[str], root_url: str = '') -> list[Response]:
    completed_response: list[Response] = []

    for url in urls:
      response = req.get(url)
      completed_response.append(response)

      logging.info(PrettyLoging.requset_log(response))

    return completed_response