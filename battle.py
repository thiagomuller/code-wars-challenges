def find_smallest_and_biggest_lists(first_list,second_list):
    biggest_list = []
    smallest_list = []
    if len(first_list) > len(second_list) or len(first_list) == len(second_list):
        return first_list, second_list
    return second_list, first_list

def damage(first_list, second_list, smallest_list):
    result = {'player1': [], 'player2': []}
    for creature in range(len(smallest_list)):
        if second_list[creature][1] > first_list[creature][0]:
            result['player2'].append(second_list[creature])
        if first_list[creature][1] > second_list[creature][0]:
            result['player1'].append(first_list[creature])
    return result

def battle(player1, player2):
    biggest_list,smallest_list = find_smallest_and_biggest_lists(player1,player2)
    remaining = biggest_list[len(smallest_list):]
    result = damage(player1, player2, smallest_list)
    if len(remaining) == 0:
        return result
    if biggest_list is player1:
        for rem in remaining:
            result['player1'].append(rem)
        return result
    if biggest_list is player2:
        for rem in remaining:
            result['player2'].append(rem)
        return result


if __name__ == '__main__':
    #player1 = [[1,3],[1,1],[3,3],[6,6]]
    #player2 = [[1,1],[1,2],[1,1]]
    player1 = []
    player2 = [[3, 3], [4, 1]]
    print(battle(player1, player2))
