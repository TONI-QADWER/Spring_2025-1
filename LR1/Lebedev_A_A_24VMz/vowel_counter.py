def count_vowels(text):
  """
  Подсчитывает количество гласных букв в строке на латинице.

  Args:
    text: Входная строка.

  Returns:
    Количество гласных букв (int).
  """
  vowels = "aeiouyAEIOUY"
  count = 0
  for char in text:
    if char in vowels:
      count += 1
  return count

# Пример использования:
text = "My life, my rules."
vowel_count = count_vowels(text)
print(f"Количество гласных букв: {vowel_count}")

text2 = "Hello World!"
vowel_count2 = count_vowels(text2)
print(f"Количество гласных букв: {vowel_count2}")

text3 = "ilAtruY VOngerat"
vowel_count3 = count_vowels(text3)
print(f"Количество гласных букв: {vowel_count3}")