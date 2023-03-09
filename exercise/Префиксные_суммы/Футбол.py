"""
Характеристика футболиста - профессионализм(p).
Сплоченная когда p1 + p2 <= p3
N - произвольное число игроков в команде

Найти максимальный суммарный профессионализм сплоченной команды

p_max <= p_min + p_min_next
p_max - R с конца, p_min - L с начала
"""


def best_sum(players):
    best_count = 0
    count = 0
    right = 0
    for left in range(len(players)):
        while right < len(players) and (left == right or players[left] + players[left + 1] >= players[right]):
            count += players[right]
            right += 1
        best_count = max(best_count, count)
        count -= players[left] # вычитаем игрока слева
    return best_count


if __name__ == '__main__':
    players = [1, 1, 3, 3, 4, 6, 11]
    print(best_sum(players))
