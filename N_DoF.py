import numpy as np
import matplotlib.pyplot as plt


def save_visual(x, y):
    plt.plot([0, x[0]], [0,y[0]], 'r-', lw=6)
    for i in range(1, len(x)):
        plt.plot([x[i-1], x[i]], [y[i-1], y[i]], 'r-', lw=6)
    plt.grid()
    plt.title(f'Posisi akhir: ({x[-1]:.2f}, {y[-1]:.2f}) cm')
    plt.savefig('visualisasi_n_dof.png')
    plt.show()

def _get_input():
    n = int(input("Jumlah N (Banyaknya Servo): "))
    servo_len = []; degree = [];
    for i in range(n):
        servo_len.append(float(input(f"\nMasukkan panjang servo {i}: ")))
        degree.append(float(input(f"Masukkan sudut servo {i} (dalam derajat): ")))
    degree = np.deg2rad(degree)
    return n, servo_len, degree

def extract_x_y():
    print("--- Forward Kinematics ---")
    n, servo_len, degree = _get_input()
    
    cum_angles = np.cumsum(degree)
    x = np.cumsum(servo_len*np.cos(cum_angles))
    y = np.cumsum(servo_len*np.sin(cum_angles))
    print(f"Didapatkan posisi (x,y) dari titik hasil pergerakan: ({x[-1]}, {y[-1]})")
    save_visual(x,y)
    return x,y

def main():
    x, y = extract_x_y()

    
if __name__ == '__main__':
    main()

