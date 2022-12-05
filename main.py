# libs
import logging

# module
from src.robots.RobotsParser import RobotsParser
from src.sitemap.SiteMapParser import SiteMapParser


def main():
  logging.basicConfig(level=logging.INFO)

  # robots
  rbts = RobotsParser('https://www.google.com/robots.txt')
  rbts.check_robots()

  # sitemap
  stmp = SiteMapParser('https://www.google.com/sitemap.xml') 
  stmp.check_map()