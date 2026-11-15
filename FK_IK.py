import numpy as np
import matplotlib.pyplot as plt

FEMUR_LEN = 44; TIBIA_LEN = 48
def save_visual(x1,y1,x2,y2):
    plt.plot([0, x1], [0, y1], 'r-', lw=6, label='Femur')
    plt.plot([x1, x2], [y1, y2], 'g-', lw=6, label='Tibia')
    plt.plot([0, x1, x2], [0, y1, y2], 'ko')   # titik sendi
    plt.axis('equal')
    plt.grid()
    plt.legend()
    plt.title(f'Posisi akhir: ({x2:.2f}, {y2:.2f}) cm')
    plt.savefig('visualisasi.png')
    plt.show()


def extract_x_y():
    # Mengubah ke radians agar bisa diterima numpy untuk sine dan cosine
    print("--- Forward Kinematics ---")
    rot_1 = np.deg2rad(float(input("Masukkan derajat Servo 1 (dalam derajat): ")))
    rot_2 = np.deg2rad(float(input("Masukkan derajat Servo 2 (dalam derajat): ")))

    # Menghitung (x_1, y_1) dari femur
    x_1 = np.cos(rot_1)*FEMUR_LEN
    y_1 = np.sin(rot_1)*FEMUR_LEN

    # Menghitung (x_2, y_2) dari tibia
    x_2 = x_1 + np.cos(rot_1+rot_2)*TIBIA_LEN
    y_2 = y_1 + np.sin(rot_1+rot_2)*TIBIA_LEN
    

    print(f"Didapatkan posisi (x,y) dari titik hasil pergerakan: ({x_2}, {y_2})")
    save_visual(x_1,y_1,x_2,y_2)
    return (x_2, y_2)

def extract_degree(x:float, y:float):
    # Jika diketahui (x,y), lalu dicari kedua sudutnya
    slope = np.sqrt(x**2 + y**2)
    
    # -- Mencari sudut servo 2
    cos_inner = (FEMUR_LEN**2 + TIBIA_LEN**2- slope**2) / (2*FEMUR_LEN*TIBIA_LEN)
    cos_inner = np.clip(cos_inner, -1.0, 1.0)
    rot_2 = np.pi - np.arccos(cos_inner)
    
    # -- Mencari sudut servo 1 
    alpha = np.arctan(y/x)
    cos_beta = (slope**2 + FEMUR_LEN**2 - TIBIA_LEN**2) / (2*slope*FEMUR_LEN)
    cos_beta = np.clip(cos_beta, -1.0, 1.0)
    rot_1 = alpha - np.arccos(cos_beta)
    
    print('--- Inverse Kinematics (Jika diketahui (x,y) serta panjang tibia dan femur) ---')
    print(f'Didapatkan sudut Servo 1: {np.degrees(rot_1)}')
    print(f'Didapatkan sudut Servo 2: {np.degrees(rot_2)}')
    return rot_1,rot_2

def main():
    x, y = extract_x_y()
    rot_1, rot_2 = extract_degree(x,y)
    
if __name__ == '__main__':
    main()


