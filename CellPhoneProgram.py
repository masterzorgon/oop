import CellPhoneClass as cpc

def main():
    manufact = "Apple, Inc."
    model = "Iphone 15 Pro"
    retail_price = 1000

    cellphone = cpc.CellPhone()

    cellphone.set_manufact(manufact)
    cellphone.set_model(model)
    cellphone.set_retail_price(retail_price)

    print(cellphone.get_manufact())
    print(cellphone.get_model())
    print(cellphone.get_retail_price())

main()