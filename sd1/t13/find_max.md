```
def find_max(arr):
    m = arr[0]
    for i in range(1, len(arr)-1):
        if a[i] > m:
            m = a[i]
    return m
```

Формальная запись:

`{P: arr.length > 0} find_max(arr) {Q: result = max(arr)}`

Инвариант цикла:

`0 < i < arr.length AND m = max(arr[0:i])`

Для инициализации:

```
i = 1
m = a[0]
0 < i < arr.length AND m = max(arr[0:1])
```

При итерациях:

Пусть на шаге n выполняется инвариант цикла. Тогда для шага n+1, 

если `a[n+1] > m`, с учетом, что `m = max(ar[:n])`, то `m = arr[n+1]` становится больше всех предидущих значений тоесть `m = max(ar[:n+1]))`

если `a[n+1] <= m`, то `m` остается `m = max(ar[:n])`, что является `m = max(ar[:n+1]))`

В конце цикла:

```
i = arr.length-1
m = max(a[0:arr.length-1])
0 < i < arr.length AND m = max(arr[0:arr.length-1])
```
