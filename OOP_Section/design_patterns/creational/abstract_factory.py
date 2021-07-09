from abc import ABC, abstractmethod


class AbstractFactory(ABC):
    """
    in this system we have two product. every product
    has different type.
    example: A = Chair , B = Sofa
    """
    @abstractmethod
    def create_product_A(self):
        pass

    @abstractmethod
    def create_product_B(self):
        pass

    @abstractmethod
    def create_product_C(self):
        pass


class ConcreteFactory1(AbstractFactory):
    """
    generate product for art type
    """

    def create_product_A(self):
        return ProductA1()

    def create_product_B(self):
        return ProductB1()

    def create_product_C(self):
        return ProductC1()


class ConcreteFactory2(AbstractFactory):
    """
    generate product for victorian type
    """

    def create_product_A(self):
        return ProductA2()

    def create_product_B(self):
        return ProductB2()

    def create_product_C(self):
        return ProductC2()


class ConcreteFactory3(AbstractFactory):
    """
    generate product for modern type
    """

    def create_product_A(self):
        return ProductA3()

    def create_product_B(self):
        return ProductB3()

    def create_product_C(self):
        return ProductC3()


class AbstractProductA(ABC):
    """
    functionality of product 1
    """

    @abstractmethod
    def sit_on(self):
        pass


class ProductA1(AbstractProductA):

    def sit_on(self):
        print("man chair artam")


class ProductA2(AbstractProductA):

    def sit_on(self):
        print("man chair victorianam")


class ProductA3(AbstractProductA):

    def sit_on(self):
        print("man chair modernam")


class AbstractProductB(ABC):

    @abstractmethod
    def khabidan(self):
        pass


class ProductB1(AbstractProductB):

    def khabidan(self):
        print("man sofa artam")


class ProductB2(AbstractProductB):

    def khabidan(self):
        print("man sofa victorianam")


class ProductB3(AbstractProductB):

    def khabidan(self):
        print("man sofa modernam")


class AbstractProductC(ABC):

    @abstractmethod
    def ghaza_khordan(self):
        pass


class ProductC1(AbstractProductC):

    def ghaza_khordan(self):
        print("man miz ghazakhori honariam!")


class ProductC2(AbstractProductC):

    def ghaza_khordan(self):
        print("man miz ghazakhori victorian!")


class ProductC3(AbstractProductC):

    def ghaza_khordan(self):
        print("man miz ghazakhori modernam!")


def client(factory):
    """
    get the type of factory. for example in this structure we have
    3 types of factories. art, victorian and modern type.
    """

    obj_a = factory.create_product_A()
    obj_b = factory.create_product_B()
    obj_c = factory.create_product_C()

    obj_a.sit_on()
    obj_b.khabidan()
    obj_c.ghaza_khordan()


if __name__ == '__main__':
    print("type honari: ")
    client(ConcreteFactory1())

    print("type victorian: ")
    client(ConcreteFactory2())

    print("type modern: ")
    client(ConcreteFactory3())
