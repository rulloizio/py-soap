from soapclient import GenericWSDL

class Vies(GenericWSDL):
    
    def __init__(self):
        super().__init__(wsdl='https://ec.europa.eu/taxation_customs/vies/services/checkVatService.wsdl')
    pass

    def checkVat(self, vatnumber, countrycode='IT'):
        return super().chiama_servizio('checkVat',countrycode,vatnumber)