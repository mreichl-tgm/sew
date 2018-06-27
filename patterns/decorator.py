"""
===============
:: Decorator ::
===============
Decoupling pattern using the open/closed principle making it
open for extension for but closed for modification.

Positive:
    + allows nesting
    + component swap at runtime
Negative:
    - increased complexity
    - possibly bad communication between component and decorator
"""


import abc


class Interface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def operation(self): pass


class Component(Interface):
    def operation(self): pass


class Decorator(Interface, metaclass=abc.ABCMeta):
    def __init__(self, component: Interface): self.component = component


class ConcreteDecorator(Decorator):
    def operation(self): self.component.operation()


if __name__ == "__main__":
    component1 = ConcreteDecorator(Component())
    component1.operation()
