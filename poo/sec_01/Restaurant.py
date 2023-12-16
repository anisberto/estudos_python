class Plate:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
            
    def __repr__(self) -> str:
        return f"Nome: {self.nome}, Preço: {self.preco}"
    
    def show_plate(self):
        print(f'Nome: {self.nome}, Preço: {self.preco}')

class Restaurant:
    restaurants = []
    def __init__(self, name, description, dishes):
        self.name = name
        self.description = description
        self.dishes = dishes
        self._active = False
        Restaurant.restaurants.append(self)
    
    @property
    def active(self):
        return 'Aberto' if self._active else 'Fechado'
        
    def show_restaurants(self):
        for restaurant in Restaurant.restaurants:
            print(f'Nome: {restaurant.name.ljust(25)} Descrição: {restaurant.description}, Situação: {restaurant.active.ljust(25)} Pratos: {restaurant.dishes}')
        
    def __str__(self) -> str:
        return f"Restaurant: {self.name}, {self.description}, Active: {self.active}, Dishes: {self.dishes}"
    
    def open_restaurant(self):
        self._active = True
        
    def close_restaurant(self):
        self._active = False

res = Restaurant("Restaurante 1", "Comida boa", [Plate("Prato 1", 10), Plate("Prato 2", 20)])
res1 = Restaurant("Restaurante 2", "Comida boa", [Plate("Prato 1", 10), Plate("Prato 2", 20)])

res.open_restaurant()
res1.open_restaurant()

res.show_restaurants()