# Py Soap

un semplice wrapper per chiamate Soap

[guida-zeep] Utilizzo della libreria ZEEP

in particolre riporto [comando-mzeep]
> python -m zeep $WSDL_URL

## Esempi di seriviz SOAP gratuiti

1. SOAP Web Services by Web Service Testing API

    URL WSDL: <https://www.dataaccess.com/webservicesserver/NumberConversion.wso?WSDL>

    Descrizione: Questo servizio fornisce conversioni di numeri (ad esempio, converte un numero in parole in inglese). È un servizio semplice ma utile per chi vuole sperimentare con le richieste SOAP.

    Esempi:

    - NumberToWords: Converte un numero in parole.
    - NumberToDollars: Converte un numero in un formato monetario in dollari.

2. TempConvert

    URL WSDL: <https://www.w3schools.com/xml/tempconvert.asmx?wsdl>

3. Country Info by WebServiceX

    URL WSDL: <http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL>

    Descrizione: Questo servizio fornisce informazioni relative a paesi, capitali, codici ISO e valute. È utile per ottenere dati generali su vari paesi.

    Esempi:
    - CountryISOCode: Restituisce il codice ISO di un paese.
    - CapitalCity: Restituisce la capitale di un paese.
    - Currency: Restituisce la valuta di un paese.

4. Calculator Service

    URL WSDL: <http://www.dneonline.com/calculator.asmx?WSDL>

    Descrizione: Un semplice servizio di calcolatrice SOAP. Utile per testare semplici operazioni aritmetiche tramite richieste SOAP.

    Esempi:
    - Add: Somma due numeri.
    - Subtract: Sottrae due numeri.
    - Multiply: Moltiplica due numeri.
    - Divide: Divide due numeri.

5. Book ISBN Numbers

    URL WSDL: <https://webservices.daehosting.com/services/isbnservice.wso?wsdl>

    Descrizione: SOAP APIs for book ISBN numbers.
    The test is done by calculation on the first 12 digits and compare the result with the checksum number at the end. You have to pass a 13 digits number.

    Esempi:
    - TODO

### Riferimenti

[guida-zeep]: <https://docs.python-zeep.org/en/master/>
[comando-mzeep]: <https://gist.github.com/FilBot3/7a80381c92e86f2a3b93a80b1d330710>
