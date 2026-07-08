from Chef import Chef

class ChineseChef(Chef): #<-- inheritance from base Chef recipe

    def make_fried_rice(self):
        print("The chef makes fried rice")

    def make_special_dish(self):
        print("The chef makes orange chicken")