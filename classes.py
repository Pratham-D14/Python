class Microwave:
    def __init__(self, brand: str, rating: str, timing: str) -> None:
        self.brand = brand
        self.rating = rating
        self.turned_on: bool = False
        self.timing = timing

    def turn_on(self) -> None:
        if self.turned_on:
            print(f'Microwave ({self.brand}) is already turned on.')
        else:
            self.turned_on = True
            print(f'Microwave ({self.brand}) is now turned on.')

    def set_timing(self):
        print(f'The timing for microwave is set to {self.timing}seconds.')

    def __str__(self):
        return f'Microwave(brand={self.brand}, rating={self.rating}, timing={self.timing})'

    def __repr__(self):
        return f'Microwave(brand={self.brand}, rating={self.rating}, timing={self.timing}) from __repr__ method'


smeg: Microwave = Microwave(brand='Smeg', rating='3.4', timing='30')
print(smeg)
# smeg.turn_on()
# smeg.set_timing()


def something():
    ...

def somethingNew():
    ...