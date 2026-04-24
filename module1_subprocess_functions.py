import subprocess

def get_system_info():
    # Get hostname
    hostname = subprocess.run(
        ["hostname"], capture_output=True, text=True
    ).stdout.strip()

    # Get OS release info
    os_release = subprocess.run(
        ["cat", "/etc/os-release"], capture_output=True, text=True
    ).stdout

    # Get kernel version
    kernel = subprocess.run(
        ["uname", "-r"], capture_output=True, text=True
    ).stdout.strip()

    # Return all values as a dictionary
    return {
        "hostname": hostname,
        "os_release": os_release,
        "kernel": kernel
    }

info = get_system_info()

print("Hostname:", info["hostname"])
print("Kernel:", info["kernel"])
print("OS Release:\n", info["os_release"])