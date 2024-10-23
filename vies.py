import zeep
from zeep.plugins import HistoryPlugin
from zeep import Client
from lxml import etree

class GenericWSDL():
    def __init__(self, wsdl) -> None:
        self.wsdl= wsdl
        self.client = zeep.Client(wsdl= wsdl)

    def getWSDL(self, file_save=None):
        if not file_save:
            print (self.client.wsdl.dump())
        else:
            raise Exception
    def getRequest(self):
        history = HistoryPlugin()
        client = zeep.Client(self.wsdl, plugins=[history])
        client.service.checkVat('IT','07660901211')
        your_pretty_xml = etree.tostring(history.last_received["envelope"], encoding="unicode", pretty_print=True)
        print(your_pretty_xml)
        
    def chiama_servizio(self, servizio, *args, **kwargs):
        """
        Chiama un metodo del servizio SOAP basato sul nome del servizio passato come stringa.
        :param servizio: Nome del metodo del servizio da chiamare (stringa).
        :param args: Argomenti posizionali per il metodo del servizio.
        :param kwargs: Argomenti keyword per il metodo del servizio.
        :return: Risultato del metodo chiamato.
        """
        # Ottieni il metodo del servizio dal client usando getattr
        metodo = getattr(self.client.service, servizio)
        
        # Chiama il metodo passando eventuali argomenti
        
        try:
            return metodo(*args, **kwargs)
        except zeep.exceptions.ValidationError as e:
            print (f"errore {e}")
            return None
pass

class Vies(GenericWSDL):
    
    def __init__(self):
        super().__init__(wsdl='https://ec.europa.eu/taxation_customs/vies/services/checkVatService.wsdl')
    
    
    pass