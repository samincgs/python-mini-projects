from sys import exit

class IceCreamTruck:
    def __init__(self):
        self.ice_cream_list = {
            'vanilla' : 4,
            'chocolate' : 3.5,
            'mint' : 5,
            'cookie dough' : 5,
            'pistachio' : 6
        }
        
        self.order = {}
        self.display_menu()
        
        
    def display_menu(self):
        print('Welcome to the Ice Cream Truck!\nPlease select an option below (Type the number please)\n')
        print('1. Order some Ice cream')
        print('2. Check your total')
        print('3. Remove an ice cream from an order')
        print('4. Exit\n')
        try:
            self.choice = int(input('Your choice: '))
            self.choose_choice()
        except:
            print('\nPlease input a proper number!')
            self.display_menu()
    
    def display_ice_cream(self):
        while True:
            print('\nHere are our options for today! Please type the flavor you would like to order\n(If you are done type exit)\n')
            for flavor, price in self.ice_cream_list.items():
                print(f'{flavor.capitalize()}: {price}')

            self.ice_cream_choice = input('\nYour choice: ').lower()
            if self.ice_cream_choice in self.ice_cream_list:
                try:
                    self.ice_cream_amount = int(input('\nHow many would you like to order?: '))
                except:
                  print('\nPlease input a proper number!')  
                  self.ice_cream_amount = int(input('\nHow many would you like to order?: '))
                  
                self.order[self.ice_cream_choice] = self.ice_cream_amount * self.ice_cream_list[self.ice_cream_choice]
                  
            elif self.ice_cream_choice == 'exit':
                self.display_menu()
                break
            else:
                print('Not a valid choice try again')
                self.ice_cream_choice = input('\nYour choice: ')
            
    def calculate_total(self):
        total = 0
        for price in self.order.values():
            total += price
    
        print(f'Your total is: ${total}')
    
    def remove_ice_cream(self):
        print('REMOVE')
    
    def choose_choice(self):
        match self.choice:
            case 1:
                self.display_ice_cream()  
            case 2:
                self.calculate_total()
            case 3:
                self.remove_ice_cream()
            case 4:
                exit()
            case _:
                print('Choice is invalid! Please try again')
                self.display_menu()
    
        
if __name__ == '__main__':
    IceCreamTruck()