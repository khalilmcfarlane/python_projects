class FavoriteCity:
    favorite_city_list = []
    valid_answers = False
    num_participants = 0
    while valid_answers:
        try:
            num_participants = int(input("How many people do we have here?"))
            valid_answers = True
        except ValueError:
            print("That was not number!")
    for i in range(num_participants):
        name = input("Welcome. What's your name?")
        # call fav city but this will be below the function

    def favorite_city(self, name, favorite_city_list=[]):
        print("Yo, {}.".format(name))
        favorite_city_name = input("So, what's your favorite city in the world?")
        favorite_city_list.append(favorite_city_name)
