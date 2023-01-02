import ipaddress

def get_ip_range(ip, mask):
  network = ipaddress.IPv4Network((ip, mask), strict=False)

  first_ip = network[0]
  last_ip = network[-1]

  return (first_ip, last_ip)

ip = "124.110.161.39"
mask = "255.255.192.0"
first_ip, last_ip = get_ip_range(ip, mask)
print(f"IP range: {first_ip} - {last_ip}")
