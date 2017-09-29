# Xiaofan Wu 903152422
class Cat:
    """An object of class Cat will have a minimum of 7 methods: __init__, __eq__, __str__, __repr__, feed, and at least three methods of your choice.
    
    The Cat class has to keep track of the total number of cats owned as num_cats.
    Each cat must have a name, a color, and optionally a favorite food that defaults to “Meow Mix.” Each cat also has a boolean attribute variable called is_hungry which is initially True and an attribute happiness: an int that represents the cat’s level of happiness (higher = happier) and starts at 1. Cats may also have as many optional parameters and variables as you would like.
    """
    def __init__(self, name, color, fout, fav_food="Meow Mix"):

        """
        Initialize a Cat object, saving as instance attributes its name, color, favorite food (defaults to “Meow Mix”), and any other attributes you would like.
        Prints a message saying that a new cat has been acquired and what its name is.
    
        Parameters: 
        self
        name: String
        color: String
        fav_food: String -- is “Meow Mix” if not given
        fout: the txt file to write the printed statament to
        """
        self.name = name
        self.color = color
        self.fav_food = fav_food
        self.is_hungry = True
        self.happiness = 1
        self.feedcount = 0
        self.weight = 10
        self.jump_height = 20
        self.emoji = '=^.^='
        print('A new cat has been acquired and its name is {}'.format(self.name))
        fout.write('A new cat has been acquired and its name is {}'.format(self.name)+'\n')

    def __eq__(self, other):
        """Compares two Cats to test equality. Cats should be equal if their names and colors are the same.
        Parameters:
        self
        other: Cat -- the second Cat you want to use

        Return: Boolean -- True if the Cats were equal, False otherwise
    
        Usage Examples:
        >>> cat = Cat("Sprinkles", "white")
        >>> other_cat = Cat("Princess Lady", "white", "Fancy Feast")
        >>> cat == other_cat
        False
        """
        if self.name == other.name and self.color == other.color:
            return True
        else:
            return False
            
    def __repr__(self):
        """Describe the Cat. Return a string that lists the pairs of attribute/values for that Cat. Including: name, color, is_hungry, fav_food, age, happiness, etc. (attributes you add for creativity’s sake or to make your additional methods work)
    
        Parameters: self
    
        Return:
        info_list: String -- Start with a list of tuples where each tuple has 2 items, an attribute followed by its value. Then convert to a string and return it.
    
        Usage Examples:
        >>> cat = Cat("Garbage", "grey")    ### It is OK if this fails after you add additional attributes to your cats.
        >>> cat                             ### Just maintain the same format for additional attributes as well
        [('name', 'Garbage'), ('color', 'grey'), ('fav_food', 'Meow Mix'), ('is_hungry', True), ('happiness', 1)]
        """
        return str([('name',self.name),('color',self.color),('fav_food',self.fav_food),('is_hungry',self.is_hungry),('happiness',self.happiness),('feedcount',self.feedcount),('weight',self.weight),('jump_height',self.jump_height),('emoji',self.emoji)])

    def __str__(self):
        """Gives an aesthetically pleasing representation of the referenced cat 
        object. All cats will have the same representation.
    
        Parameters: 
            self
    
        Return: A String containing a cat emoji (of your choosing) and a newline 
            character and the cat's name

        Usage Examples:
        >>> cat = Cat("Sprinkles", "white")
        >>> print(cat)
        =^.^=
        Sprinkles
        """
        return self.emoji +'\n'+self.name

    def feed(self, food, fout):
        """Give food to a Cat, changing its is_hungry value to False, and when given 
        its favorite food, a cat’s happiness will increase by 1.
        This method should print that the cat has been fed and if the cat is fed its 
        favorite food, an additional message will say that the cat is noticeably 
        happier.

        Parameters:
            self
            food: String -- the food being given to the cat
            fout: the txt file to write the printed statament to
        
        Return: None
    
        Usage Examples:
        >>> new_cat = Cat("Princess Lady", "white", "Fancy Feast")
        >>> new_cat.feed("Fancy Feast")
        Princess Lady ate Fancy Feast and is no longer hungry.
        Princess Lady seems happier!
        """
        self.is_hungry = False
        self.feedcount += 1
        print('{} ate {} and is no longer hungry.'.format(self.name, food))
        fout.write('{} ate {} and is no longer hungry.'.format(self.name, food)+'\n')
        if food == self.fav_food:
            self.happiness += 1
            print('{} seems happier!'.format(self.name))
            fout.write('{} seems happier!'.format(self.name)+'\n')

    def digest(self, fout):
        """Provide the cat with a special medicine and let it fully digest the given food given. Each time of feed will lead to 1 pound weight growth.
        If no food has been given, this method will print feed the cat first, or this method will update the cat's weight according to the times it got fed and print the updated weight.
        
        Parameters:
            self
            fout: the txt file to write the printed statament to

        Return:
            None

        Usage Examples:
        >>> new_cat = Cat("Princess Lady", "white", "Fancy Feast")
        >>> new_cat.feed("Fancy Feast")
        Princess Lady ate Fancy Feast and is no longer hungry.
        Princess Lady seems happier!
        >>> new_cat.digest()
        Princess Lady digested the food and grew up to 11 pounds.

        """
        if self.feedcount == 0:
            print("Please feed {} first!".format(self.name))
            fout.write("Please feed {} first!".format(self.name)+'\n')
        else:
            self.weight += self.feedcount
            print('{} digested the food and grew up to {} pounds.'.format(self.name, self.weight))
            fout.write('{} digested the food and grew up to {} pounds.'.format(self.name, self.weight)+'\n')

    def jump(self,times,fout):
        """Train the cat to jump for certain times. The more the cat is trained, the lighter its
        weight will be, and the higher it will reach.  The method will first update the cat's weight with 0.05 pound loss each time trained. 
        And the new height after certain times training will be 10/weight + 1*times feet. This method will then print the fact that the cat has been trained
        for certain times and print the height it could reach this time (round to 2 decimals).

        Parameters:
            self
            times: Integer -- the times that the cat is trained to jump
            fout: the txt file to write the printed statament to

        Return:
            None 

        Usage Examples:
        >>> new_cat = Cat("Princess Lady", "white", "Fancy Feast")
        >>> new_cat.feed("Fancy Feast")
        Princess Lady ate Fancy Feast and is no longer hungry.
        Princess Lady seems happier!
        >>> new_cat.digest()
        Princess Lady digested the food and grew up to 11 pounds.
        >>> new_cat.jump(10)
        Princess Lady has been trained to jump 10 times and can reach 10.95 feet.
        """

        for i in range(times):
            self.weight -= 0.05
        self.jump_height = round(10/self.weight + times, 2)
        print('{} has been trained to jump {} times and can reach {} feet.'.format(self.name, times, self.jump_height))
        fout.write('{} has been trained to jump {} times and can reach {} feet.'.format(self.name, times, self.jump_height)+'\n')
  
    def pat(self, fout, part = 'head'):
        """Changes the cat's emoji from '=^.^=' to '^0_0^' when patting its head.
        Changes the emoji to '(=O=)?' when patting other parts.
        Prints please enter a valid body part if user enters a string that is not a part of the body.
        Parameters:
            self
            part: String -- the part on which the cat is patted, head by default.
            fout: the txt file to write the printed statament to

        Return:
            None

        Usage Examples:
        >>> cat = Cat("Sprinkles", "white")
        >>> print(cat)
        =^.^=
        Sprinkles
        >>> cat.pat()
        ^0_0^
        >>> print(cat)
        ^0_0^
        Sprinkles
        """
        if part in ['head', 'waist', 'leg', 'claw', 'neck','shoulder','tail']:
            self.emoji = '^0_0^' if part == 'head' else '(=O=)?'
            print(self.emoji)
            fout.write(self.emoji+'\n')
        else:
            print("Please enter a valid body part.")
            fout.write("Please enter a valid body part."+'\n')


def main(args):
    """Main asks for a username using user input.
    Asks <username> to begin the game and uses a while loop to continuously 
    accept user input until user quits the sim with 'quit'.

    'quit' and 'census' are user input calls that will end the sim and call 
    the __repr__ method for ALL cats, respectively.

    Every output printed to the console and everything typed by the user should 
    be saved to a text file named log.txt while the main loop is running.
    """
    f = open("log.txt",'w')
    user_name = input("Welcome to Cat Sim v1.0. What is your name?")
    f.write("Welcome to Cat Sim v1.0. What is your name?"+'\n')
    f.write(user_name+'\n')
    print("Hello {}.".format(user_name))
    f.write("Hello {}.".format(user_name)+'\n')
    cat_dict= {}
    a = True
    while a:
        do_next = input("What would you like to do next?")
        f.write("What would you like to do next?"+'\n')
        f.write(do_next+'\n')
        do_next = do_next.lower()
        if do_next == "adopt":
            name = input("Congrats! What's your new cat's name?")
            f.write("Congrats! What's your new cat's name?"+'\n')
            f.write(name+'\n')
            color = input("What color?")
            f.write("What color?"+'\n')
            f.write(color+'\n')
            color = color.lower()
            fav_food = input("What's its favorite food?")
            f.write("What's its favorite food?"+'\n')
            f.write(fav_food+'\n')
            fav_food = fav_food.lower()
            cat_dict[name.lower()] = Cat(name,color,f,fav_food)
        elif do_next == "feed":
            name = input("What is the name of the cat you wanna select?")
            f.write("What is the name of the cat you wanna select?"+'\n')
            f.write(name+'\n')
            name = name.lower()
            food = input("Feed what food?")
            f.write("Feed what food?"+'\n')
            f.write(food+'\n')
            food = food.lower()
            cat_dict[name].feed(food,f)
        elif do_next == "digest":
            name = input("What is the name of the cat you wanna select?")
            f.write("What is the name of the cat you wanna select?"+'\n')
            f.write(name+'\n')
            name = name.lower()
            cat_dict[name].digest(f)
        elif do_next == "jump":
            name = input("What is the name of the cat you wanna select?")
            f.write("What is the name of the cat you wanna select?"+'\n')
            f.write(name+'\n')
            name = name.lower()
            times = int(input("How many time do you want {} to jump?".format(name)))
            f.write("How many time do you want {} to jump?".format(name)+'\n')
            f.write(str(times)+'\n')
            cat_dict[name].jump(times,f)
        elif do_next == "pat":
            name = input("What is the name of the cat you wanna select?")
            f.write("What is the name of the cat you wanna select?"+'\n')
            f.write(name+'\n')
            name = name.lower()
            part = input("Which body part do you want to pat?")
            f.write("Which body part do you want to pat?"+'\n')
            f.write(part+'\n')
            part = part.lower()
            cat_dict[name].pat(f, part)
        elif do_next == "quit" or do_next == "census":
            a = False
    for cat in cat_dict.values():
        print(cat.__repr__())
        f.write(cat.__repr__()+'\n')

if __name__ == "__main__":
    import sys
    main(sys.argv)

            


