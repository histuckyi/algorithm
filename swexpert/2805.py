"""
SW Expert Academy 2805. 농작물 수확하기
blog :https://daimhada.tistory.com/79
"""

def solve(n, lines, capicity_list):
    middle_index = (n - 1) // 2
    r = 0
    revenue = 0
    for length in capicity_list:
        side = (length - 1) // 2
        start_index = middle_index - side
        end_index = middle_index + side + 1
        revenue += sum(lines[r][start_index:end_index])
        r += 1
    
    for length in reversed(capicity_list[:-1]):
        side = (length - 1) // 2
        start_index = middle_index - side
        end_index = middle_index + side + 1
        revenue += sum(lines[r][start_index:end_index])
        r += 1
    return revenue

if __name__ == "__main__":
    
    n = 1
    odd = []
    while n < 50:
        odd.append(n)
        n += 2

    t = int(input())
    for c in range(t):
        n = int(input())
        odd_index = odd.index(n)
        lines = []
        for i in range(n):
            lines.append(list(map(int, list(input().strip()))))
        print("#{0} {1}".format(c+1, solve(n, lines, odd[:odd_index+1])))