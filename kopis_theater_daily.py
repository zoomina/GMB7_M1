import config

import requests
import pandas as pd

import datetime

import xml.etree.ElementTree as elemTree

"""
공연시설별 일간 데이터 추출

service : 서비스키
stdate : 검색시작기간 (YYYYMMDD)
eddate : 종료검색기간 (YYYYMMDD)
sharea : 지역(시도)코드 - 서울 : 11
shprfnmfct : 공연시설명
"""

service = config.service

stdate = config.stdate
eddate = config.eddate
place = config.place

result = pd.DataFrame()

while stdate <= eddate:
  check_date = stdate.strftime('%Y%m%d')

  # get xml from kopis
  url = f'http://www.kopis.or.kr/openApi/restful/prfstsPrfByFct?service={service}&cpage=1&rows=10&stdate={check_date}&eddate={check_date}&sharea=11&shprfnmfct={place}'

  response = requests.get(url)
  contents = response.text

  # xml parsing
  tree = elemTree.fromstring(contents)

  prfst = tree.findall("./prfst")

  prfnmplc = [x.findtext("prfnmplc") for x in prfst]  # 공연장명
  prfdtcnt = [x.findtext("prfdtcnt") for x in prfst]  # 상영 횟수
  totnmrs = [x.findtext("totnmrs") for x in prfst]    # 총 관객수

  for plc, cnt, tot in zip(prfnmplc, prfdtcnt, totnmrs):
    re = {'date':stdate, 'plc':plc, 'cnt':cnt, 'tot':tot}
    print(re)
    result = result.append(re, ignore_index=True)

  stdate += datetime.timedelta(days=1)

result.to_csv(config.save_path, index=False)