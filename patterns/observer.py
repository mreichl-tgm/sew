"""
==============
:: Observer ::
==============
Behavioral pattern using the loose coupling principle to interact with other components
with little or no knowledge about their definition.

Positive:
    + loosely coupled and therefore independent and interchangeable
    + multi-casting
    + allows both active and passive observation
Negative:
    - notifications contain no information
    - components have little of no knowledge about their observers
    - observers and concrete subjects share no common interface
"""

import abc


class Observer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def update(self): pass


class Subject(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def register(self, observer: Observer): pass

    @abc.abstractmethod
    def remove(self, observer: Observer): pass

    @abc.abstractmethod
    def notify(self, observer: Observer): pass

    @abc.abstractmethod
    def notify_all(self): pass


class ConcreteSubject(Subject):
    observers = []

    def register(self, observer: Observer): self.observers.append(observer)

    def remove(self, observer: Observer): self.observers.remove(observer)

    def notify(self, observer: Observer): observer.update()

    def notify_all(self):
        for observer in self.observers:
            observer.update()

    @staticmethod
    def pull() -> object: return


class ConcreteObserver(Observer):
    def __init__(self, subject: ConcreteSubject): self.subject = subject

    def update(self): print(self.subject.pull())


if __name__ == "__main__":
    subject1 = ConcreteSubject()

    subject1.register(ConcreteObserver(subject1))
    subject1.notify_all()
