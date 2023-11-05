import numpy as np
import uproot
import h5py


def compress(run_number):
    run_number = str(run_number)
    file = uproot.open("run" + run_number + ".root")
    PTBC = file["PTBC;1"]
    PKUP = file["PKUP;1"]
    C6D6 = file["C6D6;1"]

    f = h5py.File("h5_" + run_number + ".hdf5", "w")

    h5_PTBC = f.create_group("PTBC")
    data = PTBC
    save = h5_PTBC
    # tflash = data['tflash'].array(library="np")
    tof = data['tof'].array(library="np")
    detn = data['detn'].array(library="np")
    BN = data['BunchNumber'].array(library="np")
    PI = data['PulseIntensity'].array(library="np")
    amp = data['amp'].array(library="np")
    # area = data['area'].array(library="np")
    # save.create_dataset("tflash", data=tflash)
    save.create_dataset("tof", data=tof)
    save.create_dataset("detn", data=detn)
    save.create_dataset("BunchNumber", data=BN)
    save.create_dataset("PulseIntensity", data=PI)
    save.create_dataset("amp", data=amp)
    # save.create_dataset("area", data=area)

    h5_PKUP = f.create_group("PKUP")
    data = PKUP
    save = h5_PKUP
    tflash = data['tflash'].array(library="np")
    # tof = data['tof'].array(library="np")
    # detn = data['detn'].array(library="np")
    # BN = data['BunchNumber'].array(library="np")
    # PI = data['PulseIntensity'].array(library="np")
    # amp = data['amp'].array(library="np")
    # area = data['area'].array(library="np")
    save.create_dataset("tflash", data=tflash)
    # save.create_dataset("tof", data=tof)
    # save.create_dataset("detn", data=detn)
    # save.create_dataset("BunchNumber", data=BN)
    # save.create_dataset("PulseIntensity", data=PI)
    # save.create_dataset("amp", data=amp)
    # save.create_dataset("area", data=area)

    h5_C6D6 = f.create_group("C6D6")
    data = C6D6
    save = h5_C6D6
    tflash = data['tflash'].array(library="np")
    tof = data['tof'].array(library="np")
    # detn = data['detn'].array(library="np")
    # BN = data['BunchNumber'].array(library="np")
    # PI = data['PulseIntensity'].array(library="np")
    # amp = data['amp'].array(library="np")
    # area = data['area'].array(library="np")
    save.create_dataset("tflash", data=tflash)
    save.create_dataset("tof", data=tof)
    # save.create_dataset("detn", data=detn)
    # save.create_dataset("BunchNumber", data=BN)
    # save.create_dataset("PulseIntensity", data=PI)
    # save.create_dataset("amp", data=amp)
    # save.create_dataset("area", data=area)

    f.close()


def compress_PTBC(run_number):
    run_number = str(run_number)
    file = uproot.open("run" + run_number + ".root")
    PTBC = file["PTBC;1"]
    PKUP = file["PKUP;1"]

    f = h5py.File("h5" + run_number + ".hdf5", "w")

    h5_PTBC = f.create_group("PTBC")
    data = PTBC
    save = h5_PTBC
    tflash = data['tflash'].array(library="np")
    tof = data['tof'].array(library="np")
    detn = data['detn'].array(library="np")
    BN = data['BunchNumber'].array(library="np")
    PI = data['PulseIntensity'].array(library="np")
    amp = data['amp'].array(library="np")
    area = data['area'].array(library="np")
    save.create_dataset("tflash", data=tflash)
    save.create_dataset("tof", data=tof)
    save.create_dataset("detn", data=detn)
    save.create_dataset("BunchNumber", data=BN)
    save.create_dataset("PulseIntensity", data=PI)
    save.create_dataset("amp", data=amp)
    save.create_dataset("area", data=area)

    h5_PKUP = f.create_group("PKUP")
    data = PKUP
    save = h5_PKUP
    tflash = data['tflash'].array(library="np")
    save.create_dataset("tflash", data=tflash)

    f.close()

def compress_MGAS(run_number):
    run_number = str(run_number)
    file = uproot.open("run" + run_number + ".root")
    PTBC = file["PTBC;1"]
    PKUP = file["PKUP;1"]
    FIMG = file["FIMG;1"]

    f = h5py.File("h5" + run_number + ".hdf5", "w")

    h5_PTBC = f.create_group("PTBC")
    data = PTBC
    save = h5_PTBC
    tflash = data['tflash'].array(library="np")
    tof = data['tof'].array(library="np")
    detn = data['detn'].array(library="np")
    BN = data['BunchNumber'].array(library="np")
    PI = data['PulseIntensity'].array(library="np")
    amp = data['amp'].array(library="np")
    area = data['area'].array(library="np")
    save.create_dataset("tflash", data=tflash)
    save.create_dataset("tof", data=tof)
    save.create_dataset("detn", data=detn)
    save.create_dataset("BunchNumber", data=BN)
    save.create_dataset("PulseIntensity", data=PI)
    save.create_dataset("amp", data=amp)
    save.create_dataset("area", data=area)

    h5_FIMG = f.create_group("FIMG")
    data = FIMG
    save = h5_FIMG
    tflash = data['tflash'].array(library="np")
    tof = data['tof'].array(library="np")
    detn = data['detn'].array(library="np")
    BN = data['BunchNumber'].array(library="np")
    PI = data['PulseIntensity'].array(library="np")
    amp = data['amp'].array(library="np")
    area = data['area'].array(library="np")
    save.create_dataset("tflash", data=tflash)
    save.create_dataset("tof", data=tof)
    save.create_dataset("detn", data=detn)
    save.create_dataset("BunchNumber", data=BN)
    save.create_dataset("PulseIntensity", data=PI)
    save.create_dataset("amp", data=amp)
    save.create_dataset("area", data=area)

    h5_PKUP = f.create_group("PKUP")
    data = PKUP
    save = h5_PKUP
    tflash = data['tflash'].array(library="np")
    save.create_dataset("tflash", data=tflash)

    f.close()