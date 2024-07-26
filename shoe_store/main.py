class Shoe:
    def __init__(self, brand, size, color, price):
        
        self.brand = brand
        self.size = size
        self.color = color
        self.price = price
        
    def __str__(self):
        return f'Brand: {self.brand}, Size: {self.size}, Color: {self.color}, Price: ${self.price}'
    
class ShoeInventory:
    def __init__(self):
    
        self.shoes = []
        
    def add_shoe(self, shoe):
        self.shoes.append(shoe)
        print(f'{shoe.brand} added to inventory.')
        
    def view_inventory(self):
        
        if not self.shoes:
            print("No shoes in inventory")
        
        else:
            
            for i, shoe in enumerate(self.shoes, 1):
                print(f'{i}. {shoe}')
                
    def remove_shoe(self, index):
        
        if 0 <= index < len(self.shoes):
            
            removed_shoe = self.shoes.pop(index)
            
            print(f'Removed {removed_shoe.brand} from inventory.')
            
        else:
            
            print("invalid index. No shoe removed.")
            
    def search_shoes(self, brand):
        
        found_shoes = [shoe for shoe in self.shoes if shoe.brand.lower() == brand.lower()]
        
        if found_shoes:
            for shoe in found_shoes:
                print(shoe)
                
        else:
            print('No shoes found for the given brand.')
            
def main():
    inventory = ShoeInventory()
    
    while True:
        print('\nShoe Management System')
        print('1. Add Shoe')
        print('2. View inventory')
        print('3. Remove a Shoe')
        print('4. Search for Shoes by Brand')
        print('5. Exit')
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            
            brand = input('Enter the brand: ')
            size = input('Enter the shoe size: ')
            color = input('Enter the color of the shoe: ')
            price = input('Enter the price of the shoe: ')
            
            shoe = Shoe(brand, size, color, price)
            
            inventory.add_shoe(shoe)
        
        elif choice == '2':
            inventory.view_inventory()
        elif choice == '3':
            inventory.view_inventory()
            
            index = int(input("Enter the index of the shoe you want to remove: ")) - 1
            inventory.remove_shoe(index)
        elif choice == '4':
            brand = input('Enter the brand you want to search for: ')
            
            inventory.search_shoes(brand)
        elif choice == '5':
            print('Thank you for using the Shoe Management System')
            break
        
        else:
            print('Invalid choice. Please try again.')
            
if __name__ == '__main__':
    main()