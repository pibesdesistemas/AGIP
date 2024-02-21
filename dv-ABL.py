def dv(partida):
  
  multipliers = [7, 2, 3, 4, 5, 6, 7]

  partida = partida.upper().replace(" ", "").replace("-", "")
  if len(partida) == 6:
    partida = "0" + partida
  if len(partida) != 7:
    return None

  sum = 0
  for i in range(7):
    sum += int(partida[i]) * multipliers[i]

  dv = sum % 11

  if dv == 10:
    dv_str = "01"
  elif dv < 10:
    dv_str = "0" + str(dv)
  else:
    dv_str = str(dv)

  return dv_str

# EJEMPLO
partida = "123456"
digito = dv(partida)
print(f"Partida: {partida} DV: {digito}")
