import random
import os

num_firmware = 5
name = "ATMega2560_firmware_v1"

def gen_firmware_name(start):
    major_version = str(random.randint(5, 8))
    minor_version = str(random.randint(1,99))
    file_extension = "bin"
    return ".".join([start, major_version, minor_version, file_extension])

def make_garbage_file(name):
    kb = 1024
    mb = kb*kb
    size = 5*mb + random.randint(-50*kb, 50*kb)
    with open(name, "wb") as f:
        f.write(bytearray(os.urandom(size)))

firmware_names = [gen_firmware_name(name) for _ in range(num_firmware)]
for fw_name in firmware_names:
    make_garbage_file(fw_name)

