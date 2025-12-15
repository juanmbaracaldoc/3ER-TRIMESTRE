import csv
with open("datos.csv","w",newline="") as f:
 w=csv.writer(f); w.writerow(["Nombre","Edad"])