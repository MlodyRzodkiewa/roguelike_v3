def statistics():
    stat = {'hp': 0, 'def': 0, 'atc': 0, 'exp': 0, 'lvl': 0}
    return stat


def print_character_statistics(char_stats):
    string = "hp:{:}\tdef:{:}\tatc:{:}\texp:{:}\tlvl:{:}"
    print(string.format(*char_stats.values()))


def create_character(stat):
    #stat = statistics()
    points = 5

    while points > 0:
        stat_to_add = input("Enter, 'h', 'd' or, 'a' to add statistic: ").capitalize()
        if "H" in stat_to_add:
            stat["hp"] += 2
            print_character_statistics(stat)
        elif stat_to_add in ["D"]:
            stat["def"] += 1
            print_character_statistics(stat)
        elif stat_to_add in ["A"]:
            stat["atc"] += 1
            print_character_statistics(stat)
        points -= 1        

    return stat


def main():
    stat = statistics()
    stat = create_character(stat)
    #print_character_statistics(stat)

main()













































#
#    def create_character(points, chatacter_stats, creation=False):
#    if creation:
#        statistics = {"HP": 75, "DEF": 0, "ATC": 1, "EXP": 0, "LVL": 1}
#    else:
#        statistics = chatacter_stats
#    ui.show_character_creation_screen(statistics, points)
#
#    while points > 0:
#        is_answer_correct = False
#        while not is_answer_correct:
#            stat_to_add = ui.get_string_input("Enter 'H', 'h', 'D', 'd' or 'A', 'a' to add statistic: ")
#            is_answer_correct = common.validate_string_input(stat_to_add, ["H", "D", "A", "h", "d", "a"])
#        if stat_to_add in ["h", "H"]:
#            statistics["HP"] += 5
#        elif stat_to_add in ["D", "d"]:
#            statistics["DEF"] += 1
#        elif stat_to_add in ["A", "a"]:
#            statistics["ATC"] += 1
#        points -= 1
#        ui.show_character_creation_screen(statistics, points)
#
#    return statistics