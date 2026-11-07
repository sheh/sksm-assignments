```
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)
```

Формальная запись:

`{P: arr.length > 0} r := quick_sort(arr) {Q: arr[0] <= arr[1] <= ... <= arr[arr.length - 1] AND set(arr) == set(r)}`

Для `len(arr) <= 1`:

- пустой массив выполняет постусловие `[] == []`, отсортирован и содержет все изначальные элементы
- массив длинно 1, `[arr[0]] == [arr[0]]`, так же отсортирован и полон


Для `len(arr) >= 2`:

Если `L = quick_sort(left)`, `R = quick_sort(right)`, `M = middle` и принимаем, что L, R, M отсортированы (M -- все равны), то L + M + R тоже отсортированы. 

Каждый элемет попадает строго один раз в одно из множеств так ка он либо больше, либо меньше, либо равен pivot. Отсюда `set(L) == set(left)`, `set(R) == set(right)`, `set(M) == set(middle)`, то `set(L+M+R) == set(left + middle + right)`. 

При том, что рекурсия конечна (каждый рекурсивный вызов `quick_sort` как минимум на 1 элемент короче из-за pivot), по правилу индукции выполняются все пост условния: неубывающий порядок и полнота.