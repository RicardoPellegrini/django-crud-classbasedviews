def horario(segundos):
  horas = segundos//3600
  minutos = (segundos/3600 - horas)*60
  segundos = segundos - horas*3600 - minutos*60
  print(f'{horas}h {minutos}m {segundos}s')
