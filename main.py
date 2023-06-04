from currency_converter import CurrencyConverter
from tkinter import *

def exchange():
    e_usd.delete(0,END)
    e_gbp.delete(0,END)

    e_usd.insert(0, '%.2f' % currency.convert(e_input.get(), to_currency, "USD"))
    e_gbp.insert(0, '%.2f' % currency.convert(e_input.get(), to_currency, 'GBP'))

# The default supported currencies are:
# {'GBP', 'THB', 'HRK', 'INR', 'NOK', 'KRW', 'ILS', 'BGN', 'CZK', 'TRL', 'PHP', 'USD', 'ZAR',
#  'ROL', 'TRY', 'AUD', 'SIT', 'CNY', 'LTL', 'MYR', 'SEK', 'RON', 'MXN', 'EUR', 'CAD', 'SGD',
#  'HUF', 'CHF', 'EEK', 'LVL', 'MTL', 'PLN', 'SKK', 'IDR', 'DKK', 'JPY', 'ISK', 'HKD', 'RUB',
#  'BRL', 'NZD', 'CYP'}
# Defined here
# https://github.com/alexprengere/currencyconverter/blob/master/currency_converter/eurofxref.csv
tk_root = Tk()
tk_root.title('konverter valut')
tk_root.geometry('400x300+300+300')
tk_root.resizable(width=False, height=False)
#tk_root['bg'] = 'black'

currency = CurrencyConverter()
to_currency = "EUR"
header_frame = tk_root # Tk() #Frame(tk_root)
#header_frame.pack(fill=X)
header_frame.grid_columnconfigure(0, weight=1)
header_frame.grid_columnconfigure(1, weight=1)
header_frame.grid_columnconfigure(2, weight=1)
Label(header_frame, text='Валюта', bg='black', fg='lime', font='Areal 12 bold').\
    grid(row=0, column=0, columnspan=2, sticky=EW)
Label(header_frame, text='Курс', bg='black', fg='lime', font='Areal 12 bold').\
    grid(row=0, column=2, sticky=EW)

# USD
Label(header_frame, text="USD", font='Areal 10').\
    grid(row=1, column=0, sticky=EW)
Label(header_frame, text='1', font='Areal 10').\
    grid(row=1, column=1, sticky=EW)
Label(header_frame, text='%.2f' % currency.convert(1, "USD", to_currency), font='Areal 10').\
    grid(row=1, column=2, sticky=EW)

# GBP
Label(header_frame, text='GBP', font='Areal 10').\
    grid(row=3, column=0, sticky=EW)
Label(header_frame, text='1', font='Areal 10').\
    grid(row=3, column=1, sticky=EW)
Label(header_frame, text='%.2f' % currency.convert(1, 'GBP', to_currency), font='Areal 10').\
    grid(row=3, column=2, sticky=EW)

calc_frame = header_frame # Frame(tk_root, bg='white')
#calc_frame.pack(expand=1, fill=BOTH)
#calc_frame.grid_columnconfigure(1, weight=1)

# UA
Label(calc_frame, text='Grivni: ', bg='black', fg='lime', font='Arial 12 bold').\
    grid(row=4, column=0, padx=10)
e_input = Entry(calc_frame, justify=CENTER, font='Arial 10')
e_input.grid(row=4, column=1, columnspan=2, pady=10, padx=10, sticky=EW)

btn_calc = Button(calc_frame, text='converter', command=exchange).\
    grid(row=5, column=0,  columnspan=3)
#btn_calc.pack(expand=1, fill=BOTH, pady=5)

res_frame = header_frame # Frame(tk_root)
#res_frame.pack(expand=1, fill=BOTH, pady=5)

# res_frame.grid_columnconfigure(1, weight=1)

# USD
Label(res_frame, text="USD", font='Arial 10 bold').\
    grid(row=6, column=0)
e_usd = Entry(res_frame, justify=CENTER, font='Arial 10')
e_usd.grid(row=6, column=1, padx=10, sticky=EW)

# GBP
Label(res_frame, text='GBP', font='Arial 10 bold').\
    grid(row=7, column=0)
e_gbp = Entry(res_frame, justify=CENTER, font='Arial 10')
e_gbp.grid(row=7, column=1, padx=10, sticky=EW)





tk_root.mainloop()