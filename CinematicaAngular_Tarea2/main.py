import Files.Functions as func
import matplotlib.pyplot as plt

# Extract data from csv file into arrays
arrays = func.csv_to_arrays(r"C:\Users\mateo\Documents\GitHub\Biomechanics2024-1\CinematicaAngular_Tarea2\Drop_jump.csv")
time = [] # Time in seconds
for i in range(len(arrays[0])):
    time.append(i / 100) # 100 frames per second

## Ankle: Lineal Velocity and Acceleration
# Calculate the absolute angles of the ankle
ThetaAP = []
ThetaAE = []
for i in range(len(arrays[0])):
    ThetaAP.append(func.calculate_absoluteAngles(Prox_X=arrays[7][i], Prox_Y=arrays[8][i], Dist_X=arrays[11][i], Dist_Y=arrays[12][i]))
    ThetaAE.append(func.calculate_absoluteAngles(Prox_X=arrays[13][i], Prox_Y=arrays[14][i], Dist_X=arrays[15][i], Dist_Y=arrays[16][i]))
# Calculate the relative angles of the ankle
ThetaRAnkle = []
for i in range(len(ThetaAP)):
    ThetaRAnkle.append(ThetaAE[i] - ThetaAP[i] - 90)
# Calculate the angular velocity and acceleration of the ankle
AngVelAnkle = func.calculate_angularVelocityAcceleration(ThetaRAnkle, time)
AngAccelAnkle = func.calculate_angularVelocityAcceleration(AngVelAnkle, time)
# Turn the Velocity and Acceleration from mm/s to m/s and mm/s^2 to m/s^2
for i in range(len(AngVelAnkle)):
    AngVelAnkle[i] = AngVelAnkle[i] / 1000
for i in range(len(AngAccelAnkle)):
    AngAccelAnkle[i] = AngAccelAnkle[i] / 1000
# Calculate the lineal velocity and acceleration of the ankle
VTAnkle = []
for i in range(len(AngVelAnkle)):
    VTAnkle.append(AngVelAnkle[i] * func.point_distance(arrays[7][i], arrays[8][i], arrays[11][i], arrays[12][i]))
ATAnkle = []
for i in range(len(AngAccelAnkle)):
    ATAnkle.append(AngAccelAnkle[i] * func.point_distance(arrays[13][i], arrays[14][i], arrays[15][i], arrays[16][i]))
# Graph the lineal velocity and acceleration of the ankle
plt.plot(time[1:-1], VTAnkle, label="Lineal velocity")
plt.title("Velocidad Lineal del Tobillo")
plt.xlabel("Tiempo (s)")
plt.ylabel("Velocidad (m/s)")
plt.show()
plt.plot(time[2:-2], ATAnkle, label="Lineal acceleration")
plt.title("Aceleración Lineal del Tobillo")
plt.xlabel("Tiempo (s)")
plt.ylabel("Aceleración (m/s^2)")
plt.show()
print(f"La velocidad máxima del tobillo es {max(VTAnkle)} m/s y ocurre en el frame {VTAnkle.index(max(VTAnkle)) + 1}.")
print(f"La aceleración máxima del tobillo es {max(ATAnkle)} m/s^2 y ocurre en el frame {ATAnkle.index(max(ATAnkle)) + 1}.")