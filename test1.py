import zeep

wsdl_url = 'http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL'
client = zeep.Client(wsdl=wsdl_url)
print(client.wsdl.dump())
tt = client.get_type('ns0:CelsiusToFahrenheit')
print (tt)
