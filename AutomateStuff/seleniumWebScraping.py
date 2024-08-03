import bs4
import requests

#res =requests.get('https://api.github.com/events', stream=True)
#print(res.raise_for_status())
#print(res.headers)
#print(res.status_code)
#print(res.text)


res = requests.get('https://www.target.com/p/tracfone-prepaid-samsung-galaxy-a03s-32gb-4g-cdma-black/-/A-86100140#lnk=sametab')
soup = bs4.BeautifulSoup(res.text,'html.parser')
print(soup)
elems =soup.select('html body div#__next div main#pageBodyContainer.PageViewWrapper__StyledPageViewWrapper-sc-10kkz01-0.erQHoz.l-container-fixed div div div.styles__GalleryAndAddToCartWrapper-sc-2vujr8-2.fvBaxk div.styles__StyledAddToCartColumn-sc-2vujr8-4.eHltcA div.styles__StyledAddToCartContainer-sc-y0ahq4-0.cOihGl div#above-the-fold-information div.h-margin-b-default div.styles__PriceFullLineHeight-sc-1mh0sjm-0.dIfIJG.style__StyledPriceFull-sc-1o3i6gc-1.OpJYy span.h-text-red span.styles__CurrentPriceFontSize-sc-1mh0sjm-1.kwKAiv')
print(elems)


