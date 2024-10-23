import argparse, dotenv
import soapclient as soap
from vies import Vies

def getParser():
    pass

if __name__== '__main__':
    config = dotenv.dotenv_values(".env")
    t=soap.GenericWSDL(config["countryinfo"])
    # t.getWSDL()
    t.getServices()
    # print( t.chiama_servizio('CapitalCity','IT') )
    # print( t.chiama_servizio('CountriesUsingCurrency','EUR') )
    # print( t.chiama_servizio('CountryCurrency','IT') )
    # print( t.chiama_servizio('CountryFlag','IT') )
    # print( t.chiama_servizio('CountryISOCode','Italy') )
    # print( t.chiama_servizio('CountryIntPhoneCode','IT') )
    # print( t.chiama_servizio('CountryName','IT') )
    # print( t.chiama_servizio('CurrencyName','EUR') )
    # print( t.chiama_servizio('FullCountryInfo','IT') )
    # print( t.chiama_servizio('FullCountryInfoAllCountries') )
    # print( t.chiama_servizio('LanguageISOCode','Italian') )
    # TODO print( t.chiama_servizio('LanguageName','it')) 
    # print( t.chiama_servizio('ListOfContinentsByCode') )
    # print( t.chiama_servizio('ListOfContinentsByName') )
    # print( t.chiama_servizio('ListOfCountryNamesByCode') )
    # print( t.chiama_servizio('ListOfCountryNamesByName') )
    # print( t.chiama_servizio('ListOfCountryNamesGroupedByContinent') )
    # print( t.chiama_servizio('ListOfCurrenciesByCode') )
    # print( t.chiama_servizio('ListOfCurrenciesByName') )
    # print( t.chiama_servizio('ListOfLanguagesByCode') )
    # print( t.chiama_servizio('ListOfLanguagesByName') )
    
    
    # v= Vies()
    # v.getWSDL()
    # print(v.checkVat('07660901211'))
    # v.getRequest()