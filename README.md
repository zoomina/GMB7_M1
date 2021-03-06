# 코드스테이츠 GM 부트캠프 개인 프로젝트

<br>

## 1. 조사를 진행할 브랜드

[![image](https://user-images.githubusercontent.com/39390943/150282355-d0b4954e-0e91-4d2f-ad3f-b8e93dfd617d.png)](https://zoomina.github.io/2022/01/16/GM_pre2/)

- [SWOT & STP](https://zoomina.github.io/2022/01/18/GM_SWOT_STP/)
- [Persona & User Journey Map](https://zoomina.github.io/2022/01/19/GM_Persona_UJM/)

<br>

## 2. 정량조사 기획안

공연예술 통합전산망(KOPIS)에서 제공하는 데이터와 쇼노트 SNS에서 진행된 마케팅 캠페인 및 배우들의 미디어 노출을 바탕으로 판매 매수 및 판매 금액 추적  

- KOPIS에서는 2019년부터 극장별 판매 매수 및 금액 정보를 제공하고 있음
  - 제작사에서 진행한 공연의 진행 기간 및 극장 정보를 바탕으로 집계 가능
- 기간별로 진행된 공연 중간에 배우가 미디어에 노출된 날짜를 바탕으로 변동추이 파악

- 공연법 4조(공연예술통합전산망)에 의해 2019. 6. 25.부터 공연정보를 제공하고 있기 때문에 2019/08/16 부터 시작한 헤드윅부터 집계 시작
  - 공연장 규모를 맞추기 위해 서울/뮤지컬로 한정하여 데이터 수집

> **해당 공연 리스트**  
>   
> 헤드윅(홍익대 대학로 아트센터 대극장) : 2019/08/16 ~ 2019/11/03  
> 리지(대학로 드림아트센터 1관) : 2020/04/02 ~ 2020/06/21  
> 제이미(LG아트센터) : 2020/07/04 ~ 2020/09/12  
> 젠틀맨스 가이드:사랑과 살인편(홍익대 대학로 아트센터 대극장) : 2020/11/20 ~ 2021/09/01  
> 그레이트 코멧(유니버셜아트센터) : 2021/03/20 ~ 2021/05/30  
> 헤드윅(충무아트센터 대극장) : 2021/07/30 ~ 2021/10/31  
> 젠틀맨스 가이드:사랑과 살인편(광림아트센터 BBCH홀) : 2021/11/13 ~ 진행중   

<br>

> KOPIS OPEN API 관련 링크
> 
> [KOPIS OPEN API](https://www.kopis.or.kr/por/cs/openapi/openApiInfo.do?menuId=MNU_00074&searchType=total&searchWord=)  
> [개발가이드](https://www.kopis.or.kr/upload/openApi/%EA%B3%B5%EC%97%B0%EC%98%88%EC%88%A0%ED%86%B5%ED%95%A9%EC%A0%84%EC%82%B0%EB%A7%9DOpenAPI%EA%B0%9C%EB%B0%9C%EA%B0%80%EC%9D%B4%EB%93%9C.pdf)  
> [공통코드](https://www.kopis.or.kr/upload/openApi/%EA%B3%B5%EC%97%B0%EC%98%88%EC%88%A0%ED%86%B5%ED%95%A9%EC%A0%84%EC%82%B0%EB%A7%9DOpenAPI%EA%B3%B5%ED%86%B5%EC%BD%94%EB%93%9C.pdf)  

<br>

#### kopis_theater_daily.py  

: 서울지역 공연시설에 한하여 설정된 기간 내 일별 관객 수 추출  

1. Requirements

```
requests
pandas
datetime
xml.etree.ElementTree
```

2. config

```
service : kopis open api key
stdate : start date / type = datetime.date
eddate : end date / type = datetime.date
place : 공연시설명 / type = str  # 공통코드 참고
```

<br>

## 3. 정성조사 기획안

<br>

### 1) 현장 직접관찰

- 2021.11.13. ~ 2021.12.31. 총 48일 동안 26회차의 공연
  - 물품보관소, 로비, 객석 1층 로비, 객석 2층 로비, 객석 1층 내부, 객석 2층 내부에서 하우스 어셔로 근무하며 관객에 대한 직접 관찰을 진행


<br>

### 2) 1:1 케이스 인터뷰

카카오톡을 이용한 개인별 심층 인터뷰 진행 예정  

- `아이돌 팬덤 → 관심 고객`으로 전환된 고객
- `충성 고객 → 이탈 고객`으로 전환된 고객
- `무관심 고객 → 관심 고객`으로 전환된 고객
- 관극 경험이 있으나 `무관심 고객`으로 남아있는 고객 (2)

<br>

### 3) 트위터 크롤링

scweet 사용  
https://pypi.org/project/Scweet/  

- 트위터에서 '쇼노트', '쇼놋' 키워드로 크롤링을 진행
- 형용사 어간 추출하여 고객이 가지고 있는 브랜드에 대한 이미지 파악
- 경쟁사에 대한 분석도 함께 진행(EMK-엠개 / OD-진행x / 신시컴퍼니-신시 / S&CO-설컴 / 씨뮤-진행x)

<br>

## 4. 분석 결과

<br>

### 1) Tableau를 이용한 시각화

https://public.tableau.com/views/kopis_cnt/1_1?:language=ko-KR&publish=yes&:display_count=n&:origin=viz_share_link  

<br>

### 2) 분석 보고서

https://www.notion.so/M1-ed13c8d3e36a496cb2748e0c76dde861
