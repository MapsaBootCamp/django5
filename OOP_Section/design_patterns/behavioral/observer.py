# state manager  (subject) ---> notify all subscribed objects that state changed

from abc import ABC, abstractmethod


class Manager(ABC):
    '''
        subject interface that declares methods that concrete manage implement them
    '''
    @abstractmethod
    def subscribe(self, observer_obj) -> None:
        pass

    @abstractmethod
    def unsubscribe(self, observer_obj):
        pass

    @abstractmethod
    def notify(self):
        pass

    @abstractmethod
    def state_changer(self):
        pass


class ConcreteManager(Manager):

    state = {'goals': 0, 'fault': 0}

    subscribers = []

    def subscribe(self, observer_obj):
        print(f'subscribed an observer with name {observer_obj.name}')
        self.subscribers.append(observer_obj)

    def unsubscribe(self, observer_obj):
        print(f'Khodafez {observer_obj.name}')
        self.subscribers.remove(observer_obj)

    def notify(self):
        print('notification')
        for subs in self.subscribers:
            subs.update(self)

    def state_changer(self, event):
        print('Manager change state')

        if event == 'goal':
            self.state['goals'] += 1

        if event == 'fault':
            self.state['fault'] += 1

        print('manager wanna send notification')
        self.notify()

    def test_a(self):
        pass


class Observer(ABC):

    @abstractmethod
    def update(self, manager):
        pass


class ConcreteObserverA(Observer):

    def __init__(self):
        self.name = 'A'

    def update(self, manager):
        print(f"observer A show goals {manager.state['goals']}")


class ConcreteObserverB(Observer):

    def __init__(self):
        self.name = 'B'

    def update(self, manager):
        print(f"observer B show fault {manager.state['fault']}")


# testing

if __name__ == '__main__':

    manager = ConcreteManager()

    observer_a = ConcreteObserverA()
    manager.subscribe(observer_a)

    observer_b = ConcreteObserverB()
    manager.subscribe(observer_b)

    manager.state_changer('goal')
    manager.state_changer('fault')

    manager.unsubscribe(observer_b)

    manager.state_changer('goal')
