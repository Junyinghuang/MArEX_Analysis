import numpy as np

def select_tof_ptbc(tof, detn, amp):
    return np.concatenate((tof[(detn == 2) & (tof >= 700) & (tof < 20000) & (amp > 8000)],
tof[(detn == 2) & (tof >= 20000) & (amp > 5000)],
tof[(detn == 3) & (tof >= 700) & (tof < 2000) & (amp > 7000)],
tof[(detn == 3) & (tof >= 2000) & (amp > 4500)],
tof[(detn == 4) & (tof >= 700) & (tof < 2000) & (amp > 10000)],
tof[(detn == 4) & (tof >= 2000) & (amp > 5000)],
tof[(detn == 5) & (tof >= 700) & (tof < 2000) & (amp > 10000)],
tof[(detn == 5) & (tof >= 2000) & (tof < 20000) & (amp > 8000)],
tof[(detn == 5) & (tof >= 20000) & (amp > 4500)],
tof[(detn == 6) & (tof >= 700) & (tof < 2000) & (amp > 9000)],
tof[(detn == 6) & (tof >= 2000) & (tof < 20000) & (amp > 6000)],
tof[(detn == 6) & (tof >= 20000) & (amp > 4500)],
tof[(detn == 7) & (tof >= 700) & (tof < 2000) & (amp > 8000)],
tof[(detn == 7) & (tof >= 2000) & (tof < 20000) & (amp > 4000)],
tof[(detn == 7) & (tof >= 20000) & (amp > 3500)]))

def select_tof_fimg(tof, detn, amp):
    return np.concatenate((tof[(detn == 1) & (tof >= 10000) & (tof < 100000) & (amp > -37 / 1800 * tof + 23000 / 9)],
tof[(detn == 1) & (tof >= 100000) & (amp > 500)],
tof[(detn == 2) & (tof >= 10000) & (tof < 100000) & (amp > - 1 / 36 * tof + 29500 / 9)],
tof[(detn == 2) & (tof >= 100000) & (amp > 500)]))