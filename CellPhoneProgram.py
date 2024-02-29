import CellPhoneClass as cpc

def main():
    manufact = "Apple, Inc."
    model = "Iphone 15 Pro"
    retail_price = 1000

    cellphone = cpc.CellPhone(manufact, model, retail_price)

    print(cellphone.get_manufact())
    print(cellphone.get_model())
    print(cellphone.get_retail_price())

    cellphone.set_manufact("Black Berry")
    cellphone.set_model("123eedD")
    cellphone.set_retail_price(400)

    print(cellphone.get_manufact())
    print(cellphone.get_model())
    print(cellphone.get_retail_price())

main()