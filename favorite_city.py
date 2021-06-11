class FavoriteCity:
    favorite_city_list = []
    num_players = int(input("How many people do we have here?"))
    name = input("Welcome. What's your name?")

    def favorite_city(self, name, favorite_city_list=[]):
        print("Yo, {} .".format(name))
        favorite_city_name = input("So, what's your favorite city in the world?")
        favorite_city_list.append(favorite_city_name)
