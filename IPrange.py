import ipaddress
import sys

def get_ip_range(ip, mask):
  network = ipaddress.IPv4Network((ip, mask), strict=False)

  first_ip = network[0]
  last_ip = network[-1]

  return (first_ip, last_ip)

ip = sys.argv[1]
mask = sys.argv[2]

first_ip, last_ip = get_ip_range(ip, mask)
print(f"IP range: {first_ip} - {last_ip}")
