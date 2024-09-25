import random


def generate_simple_events(probability: float, N: int = 1):
    return [random.random() < probability for _ in range(N)]


class Team:
    def __init__(self, name, rating):
        self.name = name
        self.rating = rating

    def __repr__(self):
        return f'{self.name} (рейтинг: {self.rating})'


def simulate_match(team1, team2):
    total_rating = team1.rating + team2.rating
    win_probability_team1 = team1.rating / total_rating

    return team1 if generate_simple_events(win_probability_team1, 1) else team2


def simulate_round(teams):
    winners = []
    losers = []

    random.shuffle(teams)

    for i in range(0, len(teams), 2):
        team1, team2 = teams[i], teams[i + 1]
        winner = simulate_match(team1, team2)
        loser = team1 if winner == team2 else team2
        winners.append(winner)
        losers.append(loser)

    return winners, losers


def simulate_tournament(teams):
    round_num = 1
    all_losers = []

    while len(teams) > 1:
        print(f'\n---Раунд {round_num} ---')
        winners, losers = simulate_round(teams)

        print('Пары участников:')
        for i in range(len(losers)):
            print(f'{teams[2*i]} vs {teams[2*i + 1]} - Победитель: {winners[i]}')

        print('Выбывшие команды:')
        for loser in losers:
            print(loser)

        teams = winners
        all_losers.extend(losers)
        round_num += 1

    print('\n--- Финал ---')
    print(f'Победитель турнира: {teams[0]}')
    print('Все выбывшие команды:')

    for loser in all_losers:
        print(loser)


def main():
    while True:
        k = int(input('Введите значение k: '))
        if k >= 6:
            print('Введите корректное значение! (k <= 6)')
        else:
            break

    num_teams = 2 ** k

    teams = []
    for i in range(num_teams):
        name = f'Команда {i + 1}'
        rating = random.randint(0, 100)
        teams.append(Team(name, rating))

    print('Список команд: ')
    for team in teams:
        print(team)

    simulate_tournament(teams)


if __name__ == '__main__':
    main()
