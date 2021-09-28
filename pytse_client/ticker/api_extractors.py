# utilities to extract data from APIs related to Ticker module

from collections import namedtuple
from dataclasses import dataclass
from typing import List, Tuple

Order = namedtuple('order', ['count', 'volume', 'price'])


@dataclass
class TradeSummary:
    buy_vol: float
    buy_count: float
    sell_vol: float
    sell_count: float


def get_orders(orders_raw_text: str) -> Tuple[List[Order], List[Order]]:
    if not orders_raw_text:
        return [], []
    buy_orders_set = []
    sell_orders_set = []
    orders = orders_raw_text.split(',')
    orders.pop()  # last item is empty string
    for order_text in orders:
        order_numbers = order_text.split("@")
        buy_orders_set.append(
            Order(
                order_numbers[0],  # count
                order_numbers[1],  # vol
                order_numbers[2],  # price
            )
        )
        sell_orders_set.append(
            Order(
                order_numbers[5],  # count
                order_numbers[4],  # vol
                order_numbers[3],  # price
            )
        )
    return buy_orders_set, sell_orders_set


def get_individual_trade_summary(
    individual_trade_summary_section
) -> TradeSummary:
    splitted_fields = individual_trade_summary_section.split(",")
    if len(splitted_fields) < 9:
        return None
    
    individual_buy_vol = float(splitted_fields[0])
    individual_sell_vol = float(splitted_fields[3])
    individual_buy_count = float(splitted_fields[5])
    individual_sell_count = float(splitted_fields[8])

    return TradeSummary(
        buy_vol=individual_buy_vol,
        buy_count=individual_buy_count,
        sell_vol=individual_sell_vol,
        sell_count=individual_sell_count,
    )


def get_corporate_trade_summary(corporate_trade_summary_section):
    splitted_fields = corporate_trade_summary_section.split(",")
    if len(splitted_fields) < 9:
        return None
    
    corporate_buy_vol = float(splitted_fields[1])
    corporate_sell_vol = float(splitted_fields[4])
    corporate_buy_count = float(splitted_fields[6])
    corporate_sell_count = float(splitted_fields[9])

    return TradeSummary(
        buy_vol=corporate_buy_vol,
        buy_count=corporate_buy_count,
        sell_vol=corporate_sell_vol,
        sell_count=corporate_sell_count,
    )
