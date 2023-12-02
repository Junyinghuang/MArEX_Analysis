import numpy as np
import uproot
import h5py


def energy(tof, x, m, c):
    return m * (1 / np.sqrt(1 - x * x / c / c / tof / tof) - 1)


def get_data(run_number, detector, L):
    run_number = str(run_number)
    data = uproot.open("data/run" + run_number + ".root")[detector + ";1"]
    PKUP = uproot.open("data/run" + run_number + ".root")["PKUP;1"]
    PKUP_tflash = PKUP['tflash'].array(library="np")
    # tflash = data['tflash'].array(library="np")
    tof = data['tof'].array(library="np")
    # detn = data['detn'].array(library="np")
    BN = data['BunchNumber'].array(library="np")
    PI = data['PulseIntensity'].array(library="np")
    amp = data['amp'].array(library="np")
    norm = PI[0]
    for i in range(1, len(PI)):
        if BN[i] != BN[i - 1]:
            norm += PI[i]
    real_tof = np.zeros(len(tof))
    for i in range(len(tof)):
        real_tof[i] = tof[i] - (PKUP_tflash[BN[i] - 1] - 660 - L * 1e9 / 299792458)
    return real_tof, amp, norm


def process_data(run_numbers, detector, output):
    tof = np.array([])
    amp = np.array([])
    norm = 0
    # L = 184.5
    L = 182.24
    if detector == "C6D6":
        L += 6.89
    for i in run_numbers:
        tof_i, amp_i, norm_i = get_data(i, detector, L)
        tof = np.append(tof, tof_i)
        amp = np.append(amp, amp_i)
        norm += norm_i
    en = energy(tof / 1e9, L, 939.56542, 299792458) * 1e6  # eV
    f = h5py.File(output, "w")
    f.create_dataset("energy", data=en)
    f.create_dataset("amp", data=amp)
    f.create_dataset("norm", data=[norm])
    f.create_dataset("tof", data=tof)
    f.close()
