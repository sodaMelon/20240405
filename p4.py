def compare_all_values_bigger(dict1, original):
  for key in dict1:
      if key in original and dict1[key] >= original[key]:
        continue
      else:
        return False
  return True

def programmer_string(word):
    answer_map = {
        'p': 1,
        'r': 3,
        'o': 1,
        'g': 1,
        'a': 1,
        'm': 2,
        'e': 1
    }
    answer_scan_map1 = {
        'p': 0,
        'r': 0,
        'o': 0,
        'g': 0,
        'a': 0,
        'm': 0,
        'e': 0
    }
    answer_scan_map2 = answer_scan_map1.copy(); # reverse scan기록용
    answer_index1 = 0 #left-search
    answer_index2 = 0 #right-search
    keys = answer_map.keys()
    
    for index, char in enumerate(word): #인덱스 찾기1:순차 순회
        if char in keys:
            answer_scan_map1[char] += 1
            if (answer_scan_map1['r'] >= 3) and (compare_all_values_bigger(answer_scan_map1,answer_map)):
                answer_index1 = index
                break
  
    word_length = len(word)
    for index in range(word_length - 1, -1, -1): # 문자열 길이부터 0까지 거꾸로 순회
        char = word[index] # 해당 인덱스의 문자
        if char in keys:
            answer_scan_map2[char] += 1
            if (answer_scan_map2['r'] >= 3) and (compare_all_values_bigger(answer_scan_map2,answer_map)):
                answer_index2 = index
                break
    if (answer_index1==answer_index2):
      return 0
    return (answer_index2-answer_index1)-1


  # 예시 문자열
text = input()# "wwwpros2grammerlovepros2grammer"

  # programmer가 처음 나타나는 인덱스 찾기
index = programmer_string(text)
print(index)