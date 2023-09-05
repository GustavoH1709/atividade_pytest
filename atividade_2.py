def ordenar_lista(x):
  n = len(x)

  for i in range(n):
    for j in range(0, n-i-1):
    
        # Swap if current element is greater than next
        if x[j] > x[j+1]:
            x[j], x[j+1] = x[j+1], x[j]
  return x