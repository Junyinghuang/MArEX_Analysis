import numpy as np
import h5py

def search_asc(arr, target):
    left = 0
    right = len(arr) - 1
    while left < right - 1:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid
        else:
            right = mid
    return left

def search_desc(arr, target):
    left = 0
    right = len(arr) - 1
    while left < right - 1:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            left = mid
        else:
            right = mid
    return left

def xsec_to_ts(xsec, rho, d, m):
    return np.exp(-rho * d * xsec / m)
def tof_to_energy(tof, x, m, c):
    return m * (1 / np.sqrt(1 - x * x / c / c / tof / tof) - 1)
def tof_to_energy_dl(tof, x, m, c):
    e = tof_to_energy(tof, x, m, c) * 1e6
    f = h5py.File("data/rf_avg.h5py", "r")
    dl_avg = f['dl_avg'][:]
    dl_sig = f['dl_sig'][:]
    idx = ((np.log10(e) + 3) * 100).astype(int)
    dl = dl_avg[idx]
    sig = dl_sig[idx]
    dl250 = dl_avg[int((np.log10(250) + 3) * 100)]
    e_mid = tof_to_energy(tof, x + dl - dl250, m, c)
    e_long = tof_to_energy(tof, x + dl - dl250 + sig, m, c)
    e_short = tof_to_energy(tof, x + dl - dl250 - sig, m, c)
    return e_mid, e_long, e_short

def energy_to_tof(energy, x, m, c):
    return x * (energy + m) / c / np.sqrt(energy ** 2 + 2 * energy * m)

'''
tof = energy_to_tof(energy, 182.24, 939.56542, 299792458) * 1e9
ts = xsec_to_ts(crs * 1e-28, 9747, 0.01, 3.47e-25)
'''

def chi_sq(tr, tr_error, L, t, x_tof, crs, energy):
    ts = xsec_to_ts(np.array(crs) * 1e-28, 9747, t, 3.47e-25)[::-1]
    tof = energy_to_tof(energy, L, 939.56542, 299792458)[::-1] * 1e9
    y_ts = []
    for x in x_tof:
        y_ts.append(np.interp(x, tof, ts))
    y_ts = np.array(y_ts)
    r = y_ts - tr
    chi_sq = np.sum((r / tr_error) ** 2)
    return chi_sq