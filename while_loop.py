i=0
while i<=5 :
    print(i)
    i+=1


fruit=['banana','mango','lichi','jackFruit']
price={
    'banana':10,
    'mango':20,
    'lichi':30,
    'jackFruit':40
}
for i in fruit:
    print(i)

for i in range(0,6):
    print(i)

for i in price:
    print(f"The price of {i} is {price[i]}")

choice=input("Enter what you want to buy:")

for i in price:
    if(i==choice):
        print(f"your bill is {price[i]}") 