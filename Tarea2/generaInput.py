import json
import numpy as np

#Cambiar para recibir nombres, o seleccionar en mapa
start = input("Origen: ")
end = input("Destino: ") 
data = json.load(open("PathFinder/assets/data.json", 'r'))

coorS = np.array(data[start][:-1])
coorE = np.array(data[end][:-1])

#Output para lisp
f = open("in.txt", 'w')
f.write("({0} nil {1} {2} {3} 0 {3})\n".format(start, coorS[0], coorS[1], np.linalg.norm(coorS-coorE))) 
f.write("({0} nil {1} {2} 0 0 0)\n(".format(end, coorE[0], coorE[1]))

#Guarda el resto de los nodos como (id x y h), hay q completarlos en lisp
for i in data.keys():
    coorN = data[i][:-1]
    f.write("({0} {1} {2} {3})".format(i, coorN[0], coorN[1], np.linalg.norm(coorN-coorE)))
f.write(")")
