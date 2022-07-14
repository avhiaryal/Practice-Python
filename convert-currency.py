#kapeed
#import required module pytube > use "pip install forex_python" to install the module first

from forex_python.converter import CurrencyRates
rate = CurrencyRates()

value= int(input("Enter the amount of currency you want to convert:  "))
current_code = input("Code of current currency (eg USD, EUR, GBP): ").upper()
final_code = input("Code of currency you want to convert to eg USD, EUR, GBP): ").upper()
print("Converting", value, "from" ,current_code,"to",final_code)
conversion= rate.convert(current_code, final_code, value)
print(conversion)


