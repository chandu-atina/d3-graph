from multiprocessing import Pool

import os
values = list(range(1, 200))
domains = ["www.google.com", "www.amazon.com", "www.apple.com", "www.facebook.com"]

def nslookup(n):
   print(n)
   cmd = "nslookup www.google" + str(n) + ".com"
   print(cmd)
   os.system(cmd)

def main():
   with Pool(12) as executor:
      executor.map(nslookup, values)

if __name__ == '__main__':
   print(os.cpu_count())
   while True:
      main()
