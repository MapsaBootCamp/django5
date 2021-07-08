class Category:
    """
    نوع غذا براساس این کلاس مشخص میشود. کتگوری با صرفا یک ويژگی نام مشخص میگردد
    """

    def __init__(self, name):
        self.name = name


class SubCategory(Category):
    def __init__(self, category: Category, name: str):
        super().__init__(name)
        self.category = category


class Food:
    """
    کلاس بیس همه ی غذاهای موجود در سیستم
    status : true ---> available, false ---> finish
    """

    def __init__(self, sub_category: SubCategory, status: bool, ):
        self.id =
        self.sub_category = sub_category
        self.price = None

    def set_price(self, price: int):
        self.price = price
