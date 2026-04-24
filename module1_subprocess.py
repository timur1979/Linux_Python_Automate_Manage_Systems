import subprocess

# 1. Hostname
hostname = subprocess.run(
    ["hostname"],
    capture_output=True,
    text=True
).stdout.strip()

# 2. OS release info
os_release = subprocess.run(
    ["cat", "/etc/os-release"],
    capture_output=True,
    text=True
).stdout

# 3. Kernel version
kernel = subprocess.run(
    ["uname", "-r"],
    capture_output=True,
    text=True
).stdout.strip()

print("Hostname:\n", hostname)
print("OS Release:\n", os_release)
print("Kernel:", kernel)
