TSE_TICKER_EXPORT_DATA_ADDRESS = (
    "http://tsetmc.com/tsev2/data/Export-txt.aspx?t=i&a=1&b=0&i={}"
)
TSE_TICKER_ADDRESS = ("http://tsetmc.com/Loader.aspx?ParTree=151311&i={}")

# FIXME: c should be cSecVal (group code of instrument)
# remove e parameter when instrument has not NAV value
TSE_ISNT_INFO_URL = (
    "http://www.tsetmc.com/tsev2/data/instinfofast.aspx?i={}&c=0&e=1"
)
TSE_TICKER_INTRODUCTION_URL = (
    "http://www.tsetmc.com/Loader.aspx?Partree=15131V&s={}"
)
TSE_CLIENT_TYPE_DATA_URL = (
    "http://www.tsetmc.com/tsev2/data/clienttype.aspx?i={}"
)
TSE_SYMBOL_ID_URL = ("http://www.tsetmc.com/tsev2/data/search.aspx?skey={}")

# use instrument id as argument
TSE_SHAREHOLDERS_URL = (
    "http://www.tsetmc.com/Loader.aspx?Partree=15131T&c={}"
)

# returns all the instrument data for a specific date
# date should be formatted like YYYYMMDD
INSTRUMENT_DAY_INFO_URL = (
    "http://cdn.tsetmc.com/Loader.aspx?ParTree=15131P&i={index}&d={date}"
)

# returns list of all symbols
SYMBOLS_LIST_URL = ("http://www.tsetmc.com/Loader.aspx?ParTree=111C1417")

# market watch init, has initial data for market watch like symbols name etc.
MARKET_WATCH_INIT_URL = (
    "http://www.tsetmc.com/tsev2/data/MarketWatchInit.aspx?h=0&r=0"
)

# get day share holder data
SYMBOL_DAY_INFO_SHAREHOLDERS_DATA = (
    "http://cdn.tsetmc.com/api/Shareholder/{index}/{date}"
)

DATE_FORMAT = "%Y%m%d"
MIN_DATE = 20010321
