import sys

def num_duplicates(names, prices, weights):
    product_info_map = {}
    for i in range(len(names)):
        product_info = f"{names[i]}_{prices[i]}_{weights[i]}"
        if product_info in product_info_map:
            product_info_map[product_info] += 1 #존재할 때하나씩 증가
        else:
            product_info_map[product_info] = 0 #최초값 설정

    if product_info_map:
        max_value = max(product_info_map.values())
        return max_value
    else:
        return 0

#예시 입력
names_size = int(input())
names = [sys.stdin.readline().strip() for _ in range(names_size)]
prices_size = int(input())
prices = [int(sys.stdin.readline().strip()) for _ in range(prices_size)]
weights_size = int(input())
weights = [int(sys.stdin.readline().strip()) for _ in range(weights_size)]
print(num_duplicates(names, prices, weights))