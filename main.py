# libs
import logging, asyncio
from pprint import pprint

# module
from src.robots.RobotsParser import RobotsParser
from src.sitemap.SiteMapParser import SiteMapParser
from src.tools.PrettyLoging import PrettyLoging


async def app():
  logging.basicConfig(level=logging.INFO)

  rbts = RobotsParser('https://sky.pro/robots.txt', 'https://sky.pro/')
  stmp = SiteMapParser('https://sky.pro/sitemap.xml', 'https://sky.pro/')


  async def rbts_worker() -> None:
    rbts_list = await rbts.get_robots()
    check_result = await rbts.check_loc(rbts_list.get('allow'))

    logging.info(PrettyLoging.robots_result_log(check_result, rbts_list))


  async def stmp_worker() -> None:
    stmp_loc = await stmp.get_stmp_location()
    check_result = await stmp.check_location_stmp(stmp_loc)

    logging.info(PrettyLoging.stmp_result_log(stmp_loc, check_result))


  # main loop
  while True:

    tasks = [
      asyncio.create_task(rbts_worker()),
      asyncio.create_task(stmp_worker())
    ]

    await asyncio.wait(tasks)
    await asyncio.sleep(60)
  

def main():
  asyncio.run(app())


if __name__ == '__main__':
  main()

