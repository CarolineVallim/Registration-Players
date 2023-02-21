def add_player():
    while True:
        player = {}
        match = []
        player['name'] = str(input('Type the player name:  '))
        total_player = int(input('How many match {} played?  '.format(player['name'])))
        for x in range(0, total_player):
            match.append(int(input('How many goals in the match {}:  '.format(x))))
        
        player['goal'] = match[:]
        player['total'] = sum(match)

        team_benfica.append(player)
        
        while True:
            answer = str(input('Do you want to continue? [Y/N]  ')).upper()
            if answer in 'YN':
                break
            print('Error: You need to type only Y or N.')
        if answer == 'N':
            break


team_benfica = []
add_player()
for item in team_benfica:
    print(item)