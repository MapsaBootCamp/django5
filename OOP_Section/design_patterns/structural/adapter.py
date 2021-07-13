from abc import ABC, abstractmethod


class Target(ABC):
    """
    define abstract method that implement in concrete adapter
    """
    @abstractmethod
    def operation(self):
        pass


class Adaptee:

    def specific_opertation(self):
        return "in Adaptee, JSON"


class Adaptee2:
    def specific_operation(self):
        return "in adaptee, YAML"


class Adapter(Target, Adaptee):

    def operation(self):
        print(f"in adapter XML To {self.specific_opertation()}")


class Adapter2(Target, Adaptee2):

    def operation(self):
        print(f"in adapter XML To {self.specific_operation()}")


def client(target):
    target.operation()


if __name__ == "__main__":
    print("-"*20, "xml to json", "-"*20)
    target = Adapter()
    client(target)
    print("-"*20, "xml to yaml", "-"*20)
    target2 = Adapter2()
    client(target2)
