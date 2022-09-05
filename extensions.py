r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={base_ticker}&tsyms={quote_ticker}')
total_base = float(json.loads(r.content)[keys[quote]])
return total_base