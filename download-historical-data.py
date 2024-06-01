from tinkoff.invest import Client
from tinkoff.invest import InstrumentType
import requests

def yesNoPrompt(q):
    if q == 'Y' or q == '' or q == 'y':
        return True
    elif q != 'n':
        q = input("Unrecognizable option. Type only y or n: ")
        return yesNoPrompt(q)
    return False

def findFinstrumentByTicker():
    share = None
    with Client(TOKEN) as client:
        company_name = input("Type in the ticker: ")
        findInstrumentResp = client.instruments.find_instrument(query=company_name, instrument_kind=InstrumentType.INSTRUMENT_TYPE_SHARE)
        for instrument in findInstrumentResp.instruments:
            if instrument.class_code == 'TQBR':
                q = input(f"Found shares of {instrument.name}. Is that correct? [Y/n] ")
                flag = yesNoPrompt(q)
                if flag:
                    share = instrument
    return share

def downloadData(share):
    year = input("Type in the year of interest: ")
    payload = {'figi': share.figi, 'year': year}
    header = {'Authorization': f'Bearer {TOKEN}'}
    r = requests.get('https://invest-public-api.tinkoff.ru/history-data', params=payload, headers=header)
    if r.status_code != 200:
        q = input(f"The data for the year {year} company is not available. Would you like to try another year? [Y/n] ")
        flag = yesNoPrompt(q)
        if flag:
            return downloadData(share)
        else:
            return
    archive_name = f'{share.ticker}{year}.zip'
    print(f"Successfully downloaded market data of {share.ticker} for {year}. Saved to {archive_name}")
    with open(f'.\\{archive_name}', 'wb') as f:
        f.write(r.content)
        

token_filepath = input("Input token filepath [default is .\\token.txt] ")
if token_filepath == '':
    token_filepath = '.\\token.txt'
TOKEN = open(token_filepath, 'r').read()

with Client(TOKEN) as client:
    share = findFinstrumentByTicker()
    if share == None:
        print("Sorry, there is no such security in the database :(")
    else:
        downloadData(share)