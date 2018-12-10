import math

def sfera(raggio):
	volume = (4.0/3.0*math.pi)*raggio**3
	return volume


raggio = input ("Inserire il raggio della sfera: ")
raggio = int(raggio)
ris = sfera(raggio)
print (ris)