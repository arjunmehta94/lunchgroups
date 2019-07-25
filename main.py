import random

"""
function that takes list of people and figures out groupings
returns list of list of people in their corresponding groups
"""
def create_random_groups(list_of_people, team_people):
    num_people = len(list_of_people)
    if num_people <= 5:
        return [list_of_people]
    index_to_name = {}
    people_chosen = set()
    group_size = 3
    result = [] # list of lists of people
    # create our internal structures to map index -> name
    for idx, name in enumerate(list_of_people):
        index_to_name[idx] = name
    i = num_people
    while i >= group_size:
        people = []
        j = 0
        team_pos = 0
        teams = team_people.keys()
        while j < group_size:
            val = _pick_random_person(len(team_people[teams[team_pos]]))
            person = team_people[teams[team_pos]][val]
            if person not in people_chosen:
                people_chosen.add(person)
                j += 1
                people.append(person)
            team_pos = (team_pos + 1) % len(teams)
        result.append(people)
        i -= group_size

    # may have some people left over
    while i > 0:
        val = _pick_random_person(num_people)
        if val not in people_chosen:
            people_chosen.add(val)
            group = 0
            result[group].append(index_to_name[val])
            while group < len(result) and len(result[group]) < 5:
                group += 1
            i -= 1
    return result


def _pick_random_person(number):
    return random.randint(0, number - 1)



if __name__ == '__main__':

    # list_of_people_9 = [1,2,3,4,5,6,7,8,9]
    # result = create_random_groups(list_of_people_9)
    # assert len(result) >= 3

    # list_of_people_16 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
    # result = create_random_groups(list_of_people_16)
    # assert len(result) >= 5


    # list_of_people_23 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
    # result = create_random_groups(list_of_people_23)
    # assert len(result) >= 7

    # list_of_people_25 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
    # result = create_random_groups(list_of_people_25)
    # assert len(result) >= 8

    # list_of_people_2 = [1,2]
    # result = create_random_groups(list_of_people_2)
    # assert len(result) == 1



    # list_of_people_0 = []
    # result = create_random_groups(list_of_people_2)
    # assert len(result) == 1

    list_of_people_9 = [1,2,3,4,5,6,7,8,9]
    people_team = {
        1: [1, 2, 3],
        2: [4, 5, 6],
        3: [7, 8, 9],
        4: [10]
    }
    for key, value in people_team.items():
        print "person: " + str(key) + "in team: " + str(value)
    print create_random_groups(list_of_people_9, people_team)
