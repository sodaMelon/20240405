def count_ways_to_color_house(n):
  return 2 * 3 ** (n//2)
#pattern idea : https://stackoverflow.com/questions/77124539/

n = int(input())
print(count_ways_to_color_house(n))