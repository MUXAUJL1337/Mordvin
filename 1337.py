import requests
from lxml import etree

def count_air_company(air_company, page=0):
    response = s.get(main_url, params={'p': page})
    counter = 0
    tree = etree.HTML(response.text)
    els = tree.xpath('//table[@id = "result_list"]/tbody/tr/td/table/tr[1]/td')  #
    for el in els:
        if el.text.find(air_company):
            counter += 1
    return counter


payload = {'username': 'admin', 'password': '', 'this_is_the_login_form': 1}
login_url = 'https://anyadm.anyticket24.ru/admin/'
main_url = 'https://anyadm.anyticket24.ru/admin/online/order/'

#requests.post(login_url, data=payload)

with requests.session() as s:
    response = s.get(login_url)
    payload['csrfmiddlewaretoken'] = response.cookies['csrftoken']
    s.post(login_url, data=payload, headers={'Referer': login_url})
    #print response.text
    #response = s.get(main_url)
    #print response.text



    #counter = 0
    #tree = etree.HTML(response.text)
    #els = tree.xpath('//table[@id = "result_list"]/tbody/tr/td/table/tr[1]/td')  #
    #for el in els:
    #    if el.text.find("AEROFLOT"):
    #        counter += 1

    for i in range(700):
        print (count_air_company('AEROFLOT', i))