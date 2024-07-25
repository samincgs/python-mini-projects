class IceCreamShop:
    def __init__(self):
        self.menu = {
            "Vanilla": 1.50,
            "Chocolate" : 1.75,
            "Strawberry": 1.60,
            "Mint": 1.70,
            "Cookie Dough": 2.0
        }
        
        self.order = {}
        
    def display_menu(self):
        print("\nIce Cream Menu: ")
        
        for flavor, price in self.menu.items():
            print(f'{flavor}: {price: .2f}')
            
    def take_order(self):
        while True:
            
            self.display_menu()
            
            flavor = input('\nEnter the flavour you want to order (or type "done" to finish)').title()
            
            if flavor.lower() == 'done':
                break;
            if flavor in self.menu:
                quantity = int(input(f'How many scoops of {flavor} do you want?'))
                
                if flavor in self.order:
                    self.order[flavor] += quantity
                else:
                    self.order[flavor] = quantity
                    
            else:
                print('Sorry we do not have that flavor. Please choose a different flavor')
                
    def remove_order(self):
        while True:
            
            print('\nYour current order: ')
            
            for flavor, quantity in self.order.items():
                print(f'{flavor} - {quantity} scoops')
                
                
            flavor = input('\nEnter the flavor you want to remove (or "done" to finish):').title()
            
            if flavor.lower() == 'done':
                break
            
            if flavor in self.order:
                quantity = int(input(f'How many scoops of {flavor} would you like to remove?'))
                
                if quantity >= self.order[flavor]:
                    del self.order[flavor]
                
                else:
                    
                    self.order[flavor] -= quantity
                    
            else:
                print("That flavor is not in your order. Please choose from an existing ice cream order.")
                
    def calculate_total(self):
        total = 0
        
        print("\nYour order: ")
        
        for flavor, quantity in self.order.items():
            price = self.menu[flavor] * quantity
            
            total += price
            
            print(f'{flavor} - {quantity} scoops: ${price: .2f}')
        
        print(f'\nTotal Cost: ${total: .2f}')
        
def main():
    
    shop = IceCreamShop()
    
    while True:
        
        print("\nWelcome to the Ice Cream Shop")
        print("1. View Menu")
        print("2. Place Order")
        print("3. Remove Item from order")
        print("4. View Total")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            shop.display_menu()
        elif choice == '2':
            shop.take_order()
        elif choice == '3':
            shop.remove_order()
        elif choice == '4':
            shop.calculate_total()
        elif choice == '5':
            print("Thank you for visiting the Ice cream shop")
            break
        else:
            print("Invalid choice. Please try again")
            
if __name__ == '__main__':
    main()
            
            
        