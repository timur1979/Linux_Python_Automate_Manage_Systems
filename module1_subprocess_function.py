def get_kernel_version():
    import subprocess
    result = subprocess.run(["uname", "-r"], capture_output=True, text=True)
    return result.stdout.strip()

kernel = get_kernel_version()
print("Kernel:", kernel)