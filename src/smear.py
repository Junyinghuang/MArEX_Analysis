import numpy as np
import sys
sys.path.append("..")
from utils import search_asc, search_desc, xsec_to_ts, tof_to_energy, energy_to_tof, chi_sq

def gaus(x, mu, sig):
    return np.exp(-((x - mu) ** 2) / 2 / sig ** 2) / np.sqrt(2 * np.pi * sig ** 2)

def single(energy, crs, mean_dL, sig_dL, en):
    tot = 0
    norm = 0
    tof = energy_to_tof(en / 1e6, 182.24, 939.56542, 299792458)
    energy_mean = tof_to_energy(tof, 182.24 + mean_dL, 939.56542, 299792458) * 1e6
    energy_low = tof_to_energy(tof, 182.24 + mean_dL - sig_dL, 939.56542, 299792458) * 1e6
    energy_high = tof_to_energy(tof, 182.24 + mean_dL + sig_dL, 939.56542, 299792458) * 1e6
    diff = (energy_high - energy_low) / 100
    cur = energy_low + diff / 2
    for i in range(100):
        tot += np.interp(cur, energy, crs) * gaus(cur, energy_mean, (energy_high - energy_low) / 2)
        norm += gaus(cur, energy_mean, (energy_high - energy_low) / 2)
        cur += diff
    return tot / norm
def smear(energy, crs, mean_dL, sig_dL, en_low, en_high, num):
    ret_energy = []
    ret_crs = []
    diff = (en_high - en_low) / num
    cur = en_low
    for i in range(num):
        ret_crs.append(single(energy, crs, mean_dL, sig_dL, cur))
        ret_energy.append(cur)
        cur += diff
    return np.array(ret_energy), np.array(ret_crs)