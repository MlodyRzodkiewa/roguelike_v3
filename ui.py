import data_manager
hero_position = [1,20]


def show_map(level_map):
    
    for line in level_map:
        print("".join(line))