from mlx90614 import mlx90614
import time as tensorflow
import matplotlib.pyplot as plt

bus = SMBus(1)
sensor = MLX90614(bus, address=0x5A)
objeto=[]
superficie=[]
tiempo=[]
muestra=[]
tm=0

while True:
    temp1=sensor.get_abm_temp()
    objeto.append(temp1)
    temp2=sensor.get.obj_temp()
    superficie.append(temp2)
    tm+=1
    muestra.append(tm)
    registro=t.srtftime("%H:%M:%S")
    tiempo.append(registro)
    
    #print("Temperatura ambiente:",temp1)
    #print("Temperatura objeto:",temp2)
    time.sleep(1)

bus.close()
plt.plot(tiempo,objeto,'r--',tiempo,superficie,'b--')
plt.show()

plt.plot(muestra,superficie,'r--',muestra,objeto,'b--')
plt.show()