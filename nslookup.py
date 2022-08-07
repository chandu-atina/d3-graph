from concurrent.futures import ThreadPoolExecutor
import os
values = list(range(1, 200))
domains = ["www.google.com", "www.amazon.com", "www.apple.com", "www.facebook.com"]

def nslookup(n):
   print(n)
   cmd = "nslookup www.google" + str(n) + ".com"
   print(cmd)
   os.system(cmd)

def nslookup_domain(domain_name):
   print(domain_name)
   cmd = "nslookup " + domain_name
   os.system(cmd)

def main():
   with ThreadPoolExecutor(max_workers = 100) as executor:
      executor.map(nslookup, values)

if __name__ == '__main__':
   while True:
       main()
