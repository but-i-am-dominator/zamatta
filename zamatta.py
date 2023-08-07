import nmap3

# Create nmap object
nmap = nmap3.Nmap()

# Placeholder
results = nmap.scan_top_ports("192.168.1.1")

# Results
results['192.168.1.1']['ports'][0]