icecream_names = {
    "name_1":"vanilla",
    "name_2":"chocolate"


}
if "name_1" in icecream_names:
    print(f"your icecream_name is {icecream_names['name_1']}")


    tuples_list = ( "luka","guga","kesane","luka","giorgi","daviti","daviti","jumbera","jemala","andria")
    print(tuples_list.count(2))

    name_1 , name_2, *rest = tuples_list
    print(name_1)
    print(name_2)
    print(rest)
