import argparse, dotenv
import vies

def getParser():
    pass

if __name__== '__main__':
    config = dotenv.dotenv_values(".env")
    # t=vies.GenericWSDL(config["countryinfo"])
    # t.getRequest()
    # print(t.chiama_servizio('CurrencyName','EUR'))
    
    v= vies.Vies()
    # v.getWSDL()
    print(v.chiama_servizio('checkVat','IT'))
    v.getRequest()