import tkinter as tk
from converter import *

root = tk.Tk()
root.title('Currency Converter')
root.geometry('300x300')
frm: tk.Frame = tk.Frame(root)
frm.grid(row=0, column=0)

# tk.Label(frm, text='Currency Converter').grid(column=0, row=0, padx=10, pady=10)
# tk.Button(frm, text='Quit', command=root.destroy).grid(column=2, row=0)
tk.Label(frm, text='Amount').grid(column=0, row=1, padx=10, pady=10)
amt = tk.StringVar()
tk.Entry(frm, width=10, textvariable=amt).grid(column=1, row=1)

baseCurrency = tk.StringVar()
tk.Entry(frm, width=10, textvariable=baseCurrency).grid(column=1, row=2)
tk.Label(frm, text='Base Currency').grid(column=0, row=2, padx=10, pady=10)

vsCurrency = tk.StringVar()
tk.Entry(frm, width=10, textvariable=vsCurrency).grid(column=1, row=3)
tk.Label(frm, text='Vs Currency').grid(column=0, row=3, padx=10, pady=10)

# baseCurrency = entBaseCurrency.get()
# vsCurrency = entVsCurrency.get()
# rates = get_rates(mock=True)

result_label = tk.Label(frm, text='Click the button to convert.')
result_label.grid(column=0, row=5, columnspan=3, pady=10)

rates = get_rates(mock=True).get('rates')

def on_convert():
    try:
        amount = float(amt.get())
        base = baseCurrency.get()
        vs = vsCurrency.get()

        converted = convert_currency(amount, base, vs, rates)

        result_label.config(text=f"Amount {amount:,.2f} {base.upper()} = {converted:,.2f} {vs.upper()}")

    except ValueError as e:
        result_label.config(text=str(e))
    except Exception:
        result_label.config(text="Something went wrong.")

tk.Button(frm, text='Convert', command=on_convert).grid(column=2, row=6, padx=10, pady=10)
root.mainloop()


# print(entAmount.get())
