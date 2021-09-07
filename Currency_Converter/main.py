#pip install forex-python
from forex_python.converter import CurrencyRates
c=CurrencyRates()
e=int(input("Enter value : "))
r=c.convert("USD","IDR",e)
print(r)
