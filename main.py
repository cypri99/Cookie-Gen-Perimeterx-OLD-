import requests
import uuid
import base64
import random
from random import randint
from random import choice
import requests, threading
from fake_useragent import UserAgent
ua = UserAgent()

headers = {'User-Agent':str(ua.random)}
number = str(randint(1000, 2500))
uuid = uuid.uuid1()
link = "https://www.solebox.com/"
tc = int(30)

proxyList = []


def get_proxy2(proxy_list):
    '''
    (list) -> dict
    Given a proxy list <proxy_list>, a proxy is selected and returned.
    '''
    # Choose a random proxy
    f = open('proxies.txt')
    dividiStiProxy = f.read()

    m = dividiStiProxy.strip().split(':')
    if len(m) == 4:
        base = f"{':'.join(m[:2])}"  # ip:port
        if len(m) == 4:
            proxies = {
                'http': f"http://{':'.join(m[-2:])}@{base}" + '/',
                'https': f"http://{':'.join(m[-2:])}@{base}" + '/'
            }
    else:
        # Set up the proxy to be used
        proxies = {
            "http": str(dividiStiProxy),
            "https": str(dividiStiProxy)
        }
    # Return the proxy
    proxyList.append(proxies)

loadProxy()


def getSID():
  n = 1000
  while n > 0:
    try:
      n -= 1
      print(n)
      s = requests.session()
      s.proxies = choice(proxyList)
      endpoint = "https://www.solebox.com/uR63h57Z/xhr/api/v2/collector"
      payload = """[{\"t":"PX2","d":{"PX96":\"""" + link + """\","PX63":"Win32","PX850":0,"PX851":\"""" + number + """\","PX371":true}}]"""
      bPayload = bytes(payload, encoding='utf-8')

      data = {
              "payload": base64.b64encode(bPayload),
              "appId": "PXuR63h57Z",
              "tag": "v5.0.1",
              "uuid": uuid,
              "ft": 109,
              "seq": 0,
              "pc": 6302180037851772
          }

      resp = s.post(endpoint, data=data, headers=headers)
      resp = resp.json()
      _px3 = resp['do'][0][14:345]
      print("created cookie number:" + str(n))
      with open('pxpx.txt', 'a') as cookie:

          cookie.write(_px3 + '\n')

          cookie.flush()
    except:
      print("error")
        
for i in range(tc):

    threading.Thread(target=getSID).start()
