from zeep.plugins import HistoryPlugin
from zeep import Client
from lxml import etree

wsdl_url = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL"

history = HistoryPlugin()
client = Client(wsdl_url, plugins=[history])
client.service.CurrencyName('GBP')
your_pretty_xml = etree.tostring(history.last_received["envelope"], encoding="unicode", pretty_print=True)
print(your_pretty_xml)