import subprocess

def get_ip_address():
    try:
        
        output = subprocess.check_output("ipconfig | findstr /C:\"IPv4 Address\" /C:\"Wireless LAN adapter Wi-Fi\"", shell=True)
        ip_address = output.decode().split(":")[1].strip()        
        if not ip_address:
            output = subprocess.check_output("hostname -I", shell=True)
            ip_address = output.decode().strip()
        return ip_address
    except Exception as e:
        print(f"Error occurred: {e}")
        return None





# # Example usage
# if __name__ == "__main__":
#     ip_address = get_ip_address()
#     if ip_address:
#         print(f"My IP address is: {ip_address}")
#     else:
#         print("Unable to determine my IP address.")
