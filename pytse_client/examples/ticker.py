"""
This example is about getting data for a ticker.
use this example if you want to get data for one ticker
"""

from pytse_client import Ticker, download
import pandas as pd

# to be able to see whole DataFrame columns
pd.set_option('display.max_columns', 20)

download(symbols="نوری", write_to_csv=True)  # optional
ticker = Ticker("نوری")
print(ticker.history)  # سابقه قیمت سهم
print(ticker.client_types)  # حقیقی حقوقی
print(ticker.title)  # نام شرکت
print(ticker.url)  # آدرس صفحه سهم
print(ticker.group_name)  # نام گروه
print(ticker.fiscal_year)  # سال مالی
print(ticker.eps)  # eps
print(ticker.p_e_ratio)  # P/E
print(ticker.group_p_e_ratio)  # group P/E
print(ticker.nav)  # NAV خالص ارزش دارایی‌ها ویژه صندوق‌ها می‌باشد
print(ticker.nav_date)  # last date of NAV ویژه صندوق‌ها می‌باشد
print(ticker.psr)  # PSR این نسبت ویژه شرکت‌های تولیدی است
print(ticker.p_s_ratio)  # P/S این نسبت ویژه شرکت‌های تولیدی است
print(ticker.base_volume)  # حجم مبنا
print(ticker.last_price)  # آخرین معامله
print(ticker.adj_close)  # قیمت پایانی
print(ticker.shareholders)  # اطلاعات سهام داران عمده
print(ticker.shareholders.percentage.sum())  # جمع سهام داران
print(ticker.total_shares)

real_time_data = ticker.get_ticker_real_time_info_response()
print(real_time_data.individual_trade_summary.buy_count)
print(real_time_data.individual_trade_summary.buy_vol)
print(real_time_data.individual_trade_summary.sell_count)
print(real_time_data.individual_trade_summary.sell_vol)
print(real_time_data.corporate_trade_summary.buy_count)
print(real_time_data.corporate_trade_summary.buy_vol)
print(real_time_data.corporate_trade_summary.sell_count)
print(real_time_data.corporate_trade_summary.sell_vol)
