"""
SW Expert Academy 5201. 컨테이너 운반(D3)
blog : https://daimhada.tistory.com/31
"""

def greedy(container, truck):
    total_weight = 0
    for t in truck:
        for index, c in enumerate(container):
            if t >= c:
                total_weight += c
                container.pop(index)
                break
    return total_weight


def gens(t):
    for i in range(t):
        n , m = map(int, input().split(' ')) # container, truck
        container = list(map(int, input().strip().split()))
        container.sort(reverse=True)
        truck = list(map(int, input().strip().split()))
        truck.sort(reverse=True)
        yield container, truck

if __name__ == "__main__":
    num = 0
    t = int(input())
    for container, truck in gens(t):
        num += 1
        print('#{0} {1}'.format(num, greedy(container, truck)))

