import numpy as np
import matplotlib.pyplot as plt

# Inisialisasi variabel awal
x = 0                                 		# posisi awal x
y = 0                                 		# posisi awal y
v0 = 20                               		# kecepatan awal
angle = 90                         		    # sudut awal
angle_rad = (angle/360)*(2 * np.pi)   	    # konversi sudut dari derajat ke radian
g = -9.8                              		# percepatan gravitasi
t = 0                                 		# waktu
dt = 0.01                             		# langkah waktu

# Inisialisasi array untuk menyimpan nilai posisi dan waktu
x_arr = [x]
y_arr = [y]
t_arr = [t]

# Menghitung kecepatan awal pada sumbu x dan y
vx = v0 * np.cos(angle_rad)
vy = v0 * np.sin(angle_rad)

# Perbarui posisi dan waktu menggunakan metode Euler
while y >= 0:
    vy += g*dt
    y += vy*dt
    x += vx*dt
    t += dt
    if y < 0:
        break
    # Simpan nilai posisi dan waktu
    x_arr.append(x)
    y_arr.append(y)
    t_arr.append(t)

# Solusi numerik
t_tot_num = t_arr[-1]
range_num = x_arr[-1]
h_max_num = np.max(y_arr)

# Solusi eksak (analitik)
x_ex_arr = [0]
y_ex_arr = [0]
for t in t_arr:
    x_ex = v0 * np.cos(angle_rad) * t
    y_ex = (0.5 * g * t**2) + (v0 * np.sin(angle_rad) * t)
    x_ex_arr.append(x_ex)
    y_ex_arr.append(y_ex)

t_tot_ex = (2 * v0 * np.sin(angle_rad))/-g
range_ex = v0 * np.cos(angle_rad) * t_tot_ex
h_max_ex = (v0*2 * np.sin(angle_rad)*2) / (-2 * g)

# Plot hasil simulasi numerik dan analitik
plt.figure()
plt.plot(x_arr, y_arr, c='b', label='numerical')
plt.plot(x_ex_arr, y_ex_arr, c='r', label='analytical')
plt.axhline(c='black')
plt.axvline(c='black')
plt.legend()
plt.show()

# Bandingkan hasil numerik dan analitik
print('Perbandingan hasil numerik dan analitik')
print('Total waktu (s): {:.2f} vs {:.2f}'.format(t_tot_num, t_tot_ex))
print('Jarak tempuh (m): {:.2f} vs {:.2f}'.format(range_num, range_ex))
print('Ketinggian maksimum (m): {:.2f} vs {:.2f}'.format(h_max_num, h_max_ex))

# Mencari indeks ketinggian maksimal untuk melakukan perbandingan
max_height = max(y_arr)
max_index_height = y_arr.index(max_height)
print("Index Ketinggian Maksimum : ", max_index_height)
print(len(y_arr))
print(t_arr[max_index_height])
print(t_arr[len(t_arr) - 1] - t_arr[max_index_height])

# Membuat foto yang akan dijadikan simulasi dari awal ke titik tertinggi
plt.rcParams.update({'figure.max_open_warning': 0})
for i in range(max_index_height):
    plt.figure()
    plt.scatter(x_arr[i], y_arr[i], marker='o', c='b')
    plt.text(32, 14, '{:.2f} s'.format(t_arr[i]))
    plt.ylim(-1,16)
    plt.xlim(-1,36)
    plt.axhline(c='black')
    plt.axvline(c='black')
    plt.savefig('...PATH.../foto/fig_{:04d}.png'.format(i+1), 
                format='png', dpi=1000, bbox_inches="tight")

# Membuat foto yang akan dijadikan simulasi dari titik tertinggi ke titik akhir
plt.rcParams.update({'figure.max_open_warning': 0})
for i in range(max_index_height, len(y_arr)):
    plt.figure()
    plt.scatter(x_arr[i], y_arr[i], marker='o', c='b')
    plt.text(32, 14, '{:.2f} s'.format(t_arr[i]))
    plt.ylim(-1,16)
    plt.xlim(-1,36)
    plt.axhline(c='black')
    plt.axvline(c='black')
    plt.savefig('...PATH.../foto/fig_{:04d}.png'.format(i+1), 
                format='png', dpi=1000, bbox_inches="tight")