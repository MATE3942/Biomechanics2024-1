import Files.Functions as func
import matplotlib.pyplot as plt

# Extract data from csv file into arrays
arrays = func.csv_to_arrays(r"C:\Users\mateo\Documents\GitHub\Biomechanics2024-1\CinematicaAngular_Tarea2\Drop_jump.csv")
time = [] # Time in seconds
for i in range(len(arrays[0])):
    time.append(i / 100) # 100 frames per second

## Ankle: Lineal Velocity and Acceleration
# Calculate the Lineal Velocity for each coordinate
LVAnkle_x = func.calculate_difMethod(arrays[11], time)
LVAnkle_z = func.calculate_difMethod(arrays[12], time)
# Calculate the Magnitude and Angle of the Lineal Velocity
MagVelAnkle = []
VelDirectionAnkle = []
for i in range(len(LVAnkle_x)):
    MagVelAnkle.append(func.math.sqrt((LVAnkle_x[i])**2 + (LVAnkle_z[i])**2))
    VelDirectionAnkle.append(func.math.degrees(func.math.atan(LVAnkle_z[i]/LVAnkle_x[i])))
# Calculate the Lineal Acceleration for each coordinate
LAAnkle_x = func.calculate_difMethod(LVAnkle_x, time)
LAAnkle_z = func.calculate_difMethod(LVAnkle_z, time)
# Calculate the Magnitude and Angle of the Lineal Acceleration
MagAccelAnkle = []
AccelDirectionAnkle = []
for i in range(len(LAAnkle_x)):
    MagAccelAnkle.append(func.math.sqrt(LAAnkle_x[i]**2 + LAAnkle_z[i]**2))
    AccelDirectionAnkle.append(func.math.degrees(func.math.atan(LAAnkle_z[i]/LAAnkle_x[i])))
# Turn the Velocity and Acceleration from mm/s to m/s and mm/s^2 to m/s^2
for i in range(len(MagVelAnkle)):
    MagVelAnkle[i] = MagVelAnkle[i] / 1000
for i in range(len(MagAccelAnkle)):
    MagAccelAnkle[i] = MagAccelAnkle[i] / 1000
# Graph the lineal velocity and acceleration of the ankle
print(f"La magnitud máxima de la velocidad lineal del tobillo es {max(MagVelAnkle, key=abs)} m/s y ocurre en el frame {MagVelAnkle.index(max(MagVelAnkle, key=abs)) + 1}. El ángulo en ese momento es {VelDirectionAnkle[MagVelAnkle.index(max(MagVelAnkle, key=abs)) + 1]} °")
plt.plot(time[1:-1], MagVelAnkle, label="Lineal velocity magnitude")
plt.title("Magnitud de la Velocidad Lineal del Tobillo")
plt.xlabel("Tiempo (s)")
plt.ylabel("Velocidad (m/s)")
plt.show()
plt.plot(time[1:-1], VelDirectionAnkle, label="Lineal velocity direction")
plt.title("Dirección de la Velocidad Lineal del Tobillo")
plt.xlabel("Tiempo (s)")
plt.ylabel("Ángulo (°)")
plt.show()

print(f"La aceleración máxima del tobillo es {max(MagAccelAnkle, key=abs)} m/s^2 y ocurre en el frame {MagAccelAnkle.index(max(MagAccelAnkle, key=abs)) + 2}. El ángulo absoluto en ese momento es {AccelDirectionAnkle[MagAccelAnkle.index(max(MagAccelAnkle, key=abs)) + 2]} °")
plt.plot(time[2:-2], MagAccelAnkle, label="Lineal acceleration magnitude")
plt.title("Magnitud de la Aceleración Lineal del Tobillo")
plt.xlabel("Tiempo (s)")
plt.ylabel("Aceleración (m/s^2)")
plt.show()
plt.plot(time[2:-2], AccelDirectionAnkle, label="Lineal acceleration direction")
plt.title("Dirección de la Aceleración Lineal del Tobillo")
plt.xlabel("Tiempo (s)")
plt.ylabel("Ángulo (°)")
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
AngVelAnkle = func.calculate_difMethod(ThetaAE, time)
AngAccelAnkle = func.calculate_difMethod(AngVelAnkle, time)
# Turn the Velocity and Acceleration from mm/s to m/s and mm/s^2 to m/s^2
for i in range(len(AngVelAnkle)):
    AngVelAnkle[i] = AngVelAnkle[i] / 1000
for i in range(len(AngAccelAnkle)):
    AngAccelAnkle[i] = AngAccelAnkle[i] / 1000
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

## Toe: Highest Point after landing
# Start searching for the highest value in the second half of the array (highest point after jumping)
highest_after_lowest = max(arrays[16][(len(arrays[16]) // 2):])
print(f"\nEl valor más alto alcanzado luego de aterrizar es: {highest_after_lowest / 1000} m y sucede en el frame {arrays[16].index(highest_after_lowest)}.")