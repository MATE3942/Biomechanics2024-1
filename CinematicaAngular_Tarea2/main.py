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
print(f"La velocidad máxima del tobillo es {max(VTAnkle, key=abs)} m/s y ocurre en el frame {VTAnkle.index(max(VTAnkle, key=abs)) + 1}. El ángulo absoluto en ese momento es {ThetaAE[VTAnkle.index(max(VTAnkle, key=abs)) + 1]} °")
plt.plot(time[1:-1], VTAnkle, label="Lineal velocity")
plt.title("Velocidad Lineal del Tobillo")
plt.xlabel("Tiempo (s)")
plt.ylabel("Velocidad (m/s)")
plt.show()
print(f"La aceleración máxima del tobillo es {max(ATAnkle, key=abs)} m/s^2 y ocurre en el frame {ATAnkle.index(max(ATAnkle, key=abs)) + 2}. El ángulo absoluto en ese momento es {ThetaAE[ATAnkle.index(max(ATAnkle, key=abs)) + 2]} °")
plt.plot(time[2:-2], ATAnkle, label="Lineal acceleration")
plt.title("Aceleración Lineal del Tobillo")
plt.xlabel("Tiempo (s)")
plt.ylabel("Aceleración (m/s^2)")
plt.show()

## Knee: Relative Angles
# Calculate the absolute angles of the knee
ThetaAM = []
ThetaAP = []
for i in range(len(arrays[0])):
    ThetaAM.append(func.calculate_absoluteAngles(Prox_X=arrays[5][i], Prox_Y=arrays[6][i], Dist_X=arrays[7][i], Dist_Y=arrays[8][i]))
    ThetaAP.append(func.calculate_absoluteAngles(Prox_X=arrays[7][i], Prox_Y=arrays[8][i], Dist_X=arrays[9][i], Dist_Y=arrays[10][i]))
# Calculate the relative angles of the knee
ThetaRKnee = []
for i in range(len(ThetaAM)):
    ThetaRKnee.append(ThetaAM[i] - ThetaAP[i])
# Graph the relative angles of the knee
print(f"\nEl ángulo máximo de la rodilla es {max(ThetaRKnee, key=abs)} ° y ocurre en el frame {ThetaRKnee.index(max(ThetaRKnee, key=abs))}.")
plt.plot(time, ThetaRKnee, label="Relative angle")
plt.title("Ángulo Relativo de la Rodilla")
plt.xlabel("Tiempo (s)")
plt.ylabel("Ángulo (°)")
plt.show()

## Feet: Angular Velocity and Acceleration
print(f"\nLa velocidad angular máxima del tobillo es {max(AngVelAnkle, key=abs)} °/s y ocurre en el frame {AngVelAnkle.index(max(AngVelAnkle, key=abs)) + 1}.")
plt.plot(time[1:-1], AngVelAnkle, label="Angular velocity")
plt.title("Velocidad Angular del Tobillo")
plt.xlabel("Tiempo (s)")
plt.ylabel("Velocidad (°/s)")
plt.show()
print(f"La aceleración angular máxima del tobillo es {max(AngAccelAnkle, key=abs)} °/s^2 y ocurre en el frame {AngAccelAnkle.index(max(AngAccelAnkle, key=abs)) + 2}.")
plt.plot(time[2:-2], AngAccelAnkle, label="Angular acceleration")
plt.title("Aceleración Angular del Tobillo")
plt.xlabel("Tiempo (s)")
plt.ylabel("Aceleración (°/s^2)")
plt.show()