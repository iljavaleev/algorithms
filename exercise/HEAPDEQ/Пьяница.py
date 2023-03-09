from collections import deque

def play(q1, q2):
    count = 0
    while count < 10**6 + 1:
        card1 = q1.popleft()
        card2 = q2.popleft()
        if card1 == 0 and card2 == 9:
            q1.append(card1)
            q1.append(card2)
        elif card1 == 9 and card2 == 0:
            q2.append(card1)
            q2.append(card2)
        elif card1 > card2:
            q1.append(card1)
            q1.append(card2)
        elif card1 < card2:
            q2.append(card1)
            q2.append(card2)
        count += 1

        if not q1:
            print('second', count)
            break
        if not q2:
            print('first', count)
            break

    else:
        print('botva')


if __name__ == '__main__':
    q1 = deque(int(i) for i in input().split())
    q2 = deque(int(i) for i in input().split())
    play(q1, q2)
