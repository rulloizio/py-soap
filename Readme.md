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

2. Global Weather by WebServiceX

    URL WSDL: <http://www.webservicex.net/globalweather.asmx?WSDL>

    Descrizione: Questo servizio SOAP gratuito fornisce dati meteorologici in tutto il mondo. È utile per ottenere informazioni sul meteo attuale per una determinata città o paese.

    Esempi:
    - GetWeather: Restituisce le informazioni meteo per una specifica città.
    - GetCitiesByCountry: Restituisce l'elenco delle città per un determinato paese.

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

5. Bank BLZ Service

    URL WSDL: <http://www.thomas-bayer.com/axis2/services/BLZService?wsdl>

    Descrizione: Fornisce informazioni su banche tedesche a partire dal codice BLZ (Bankleitzahl). È particolarmente utile per test relativi ai servizi bancari o per ottenere informazioni sulle banche.

    Esempi:
    - getBank: Restituisce le informazioni di una banca partendo dal codice BLZ.

6. Currency Converter by WebServiceX

    URL WSDL: <http://www.webservicex.net/CurrencyConvertor.asmx?WSDL>

    Descrizione: Un servizio che permette di convertire valute da una valuta all'altra utilizzando tassi di cambio attuali. Questo servizio può essere usato per applicazioni finanziarie o semplicemente per testare conversioni di valuta.

    Esempi:
    - ConversionRate: Restituisce il tasso di cambio corrente tra due valute specificate.

7. United States ZIP Code Information

    URL WSDL: <http://www.webservicex.net/uszip.asmx?WSDL>

    Descrizione: Fornisce informazioni relative ai codici postali (ZIP) degli Stati Uniti, compresi dettagli come la città e lo stato corrispondente.

    Esempi:
    - GetInfoByZIP: Restituisce informazioni relative a un determinato codice ZIP.

8. Email Validation SOAP API

    URL WSDL: <https://www.brettle.com/webservices/emailverification.asmx?WSDL>

    Descrizione: Questo servizio permette di validare indirizzi email. Può essere utile per integrazioni in applicazioni dove è necessario verificare la validità degli indirizzi email degli utenti.

    Esempi:
    - IsValidEmail: Verifica se un indirizzo email è valido.

9. IP Location SOAP Service

    URL WSDL: <http://www.webservicex.net/geoipservice.asmx?WSDL>

    Descrizione: Un servizio che restituisce informazioni sulla posizione geografica (città, regione, paese) di un indirizzo IP. Utile per test di localizzazione e geolocalizzazione.

    Esempi:
    - GetGeoIP: Restituisce informazioni geografiche di un indirizzo IP.

10. Random Quote SOAP Service

    URL WSDL: <http://www.randomquotes.net/webservice/quotes.asmx?WSDL>

    Descrizione: Fornisce una citazione casuale. Utile per semplici applicazioni che desiderano visualizzare frasi motivazionali o casuali.

    Esempi:
    - GetQuote: Restituisce una citazione casuale.

### Riferimenti

[guida-zeep]: <https://docs.python-zeep.org/en/master/>
[comando-mzeep]: <https://gist.github.com/FilBot3/7a80381c92e86f2a3b93a80b1d330710>
