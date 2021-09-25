import json
from collections import OrderedDict
from pathlib import Path
from typing import List
import locale

from pytse_client import config
from pytse_client.scraper.symbol_scraper import (
    MarketSymbol,
    get_market_symbols_from_market_watch_page,
    get_market_symbols_from_symbols_list_page,
    add_old_indexes_to_market_symbols,
)


def write_symbols_to_json(
    market_symbols: List[MarketSymbol], filename: str, path: str
) -> None:
    Path(path).mkdir(parents=True, exist_ok=True)
    with open(f'{path}/{filename}', 'w', encoding='utf8') as file:
        data = {
            obj.symbol: {
                "index": obj.index,
                "code": obj.code,
                "name": obj.name,
                "old": obj.old
            }
            for obj in market_symbols
        }
        json.dump(data, file, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    market_symbols = (
        get_market_symbols_from_symbols_list_page() +
        get_market_symbols_from_market_watch_page()
    )
    deduplicated_market_symbols = list(OrderedDict.fromkeys(market_symbols))
    # fetch old indexes of symbols
    deduplicated_market_symbols = add_old_indexes_to_market_symbols(
        deduplicated_market_symbols
    )
    # sort by sybmol
    locale.setlocale(locale.LC_COLLATE, "fa_IR.UTF-8")
    deduplicated_market_symbols = sorted(
        deduplicated_market_symbols,
        key=lambda i: locale.strxfrm(i.symbol)
    )
    write_symbols_to_json(
        deduplicated_market_symbols, "symbols_name.json",
        f"{config.pytse_dir}/data"
    )
