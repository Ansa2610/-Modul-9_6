# Напишите функцию-генератор all_variants(text),
# которая принимает строку text и возвращает
# объект-генератор, при каждой итерации которого
# будет возвращаться подпоследовательности переданной строки.

def all_variants(text):
    n = len(text)
    for x in range(1, n + 1):
        for k in range(n - x + 1):
            yield text[k:k + x]


a = all_variants('abc')
for i in a:
    print(i)
