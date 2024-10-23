import zeep, operator
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
        """
        
        """
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
     # TODO da rivedere 
    def generate_models_from_wsdl(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        types = self.client.wsdl.types

        models = {}

        for name, schema in types.types.items():
            if isinstance(schema, zeep.xsd.ComplexType):
                attrs = {
                    '__tablename__': name.lower(),
                    'id': Column(Integer, primary_key=True, autoincrement=True)
                }
                for element in schema.elements:
                    field_name = element[0]
                    field_type = element[1].type
                    if isinstance(field_type, zeep.xsd.types.String):
                        attrs[field_name] = Column(String)
                    elif isinstance(field_type, zeep.xsd.types.Integer):
                        attrs[field_name] = Column(Integer)
                    # Aggiungi altri tipi di mappatura secondo necessità

                # Crea il modello dinamicamente
                model = type(name, (Base,), attrs)
                models[name] = model

        return models

    def getServices(self):
        """Elenca i servizi operazioni e altro 
        """
        # print(self.client.service())
        for service in self.client.wsdl.services.values():
            print("service:", service.name)
            for port in service.ports.values():
                operations = sorted(
                    port.binding._operations.values(),
                    key=operator.attrgetter('name'))

                for operation in operations:
                    print("method :", operation.name)
                    print("  input :", operation.input.signature())
                    print()
            print()