"""
 Universidad Adolfo Ibañez
 Facultad de Ingeniería y Ciencias
 Miguel Carrasco (miguel.carrasco@uai.cl)
 version 1.0 (07/06/2021)

 Objetivo:
 1) Emplear un test ANOVA de una vía y calcular los valores estadísticos F y p-value

"""

from scipy.stats import f_oneway

tillamook = [0.0571, 0.0813, 0.0831, 0.0976, 0.0817, 0.0859, 0.0735,
             0.0659, 0.0923, 0.0836]
newport = [0.0873, 0.0662, 0.0672, 0.0819, 0.0749, 0.0649, 0.0835,
           0.0725]
petersburg = [0.0974, 0.1352, 0.0817, 0.1016, 0.0968, 0.1064, 0.105]
magadan = [0.1033, 0.0915, 0.0781, 0.0685, 0.0677, 0.0697, 0.0764,
           0.0689]
tvarminne = [0.0703, 0.1026, 0.0956, 0.0973, 0.1039, 0.1045]

F, p = f_oneway(tillamook, newport, petersburg, magadan, tvarminne)

print('F:{:2.4}'.format(F))
print('p:{:2.4}'.format(p))

#////////////////////////////////
# Interpretacion a través de  p-value

# nivel de significancia
alpha = 0.05

print('significancia={:.2}, p={:.4}'.format(alpha, p))
if p <= alpha:
	print('Las longitudes medias no son todas iguales (rechazar H0)')
else:
	print('Las longitudes medias son todas iguales indendiente de la ubicación  (fallamos en rechazar H0)')