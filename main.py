from art import logo
print(logo)

dict={}
def bid(name, price):
  dict[name]=price
  high_price=0
  for name in dict:
    if dict[name]> high_price:
      high_price= dict[name]
  print(f"The highest value is bid by {name} with the price ${high_price}")
    
Continue = True
while Continue:
  name= input("Please enter the name: ")
  price = int(input("Please enter the price: $"))

  more = input("Are there any more bidders? yes or no?")
  if ( more=="no"):
    Continue=False
    bid(name,price)