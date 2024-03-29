class Mobile:
    def __init__(self, model, company, price):
        setattr(self, "model", model)
        setattr(self, "company", company)
        setattr(self, "price", price)

    def print_info(self):
        print(f"model:{getattr(self, 'model')}")
        print(f"model:{getattr(self, 'company')}")
        print(f"model:{getattr(self, 'price')}")

    def can_affordable(self):
        if getattr(self, 'price') >= 20:
            print(f"afforable price")
        else:
            print(f"unafordable")


m1 = Mobile("i-14", "iphone", 60)
m1.can_affordable()
m2 = Mobile("m-25", "samsung", 25)
m2.print_info()