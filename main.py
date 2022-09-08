
from asyncio import as_completed
import logging
import multiprocessing
from multiprocessing.pool import ThreadPool
from operator import itemgetter
import re
import threading
import time
import trio
import httpx
from ignorant.modules.shopping.amazon import amazon
from bs4 import BeautifulSoup as bs
from termcolor import colored
import time
from threading import Lock
import concurrent.futures

async def main():
    start = time.perf_counter()
    lines = open("numlist.txt", "r+")
    numbers = lines.readlines()
    x = (len(numbers))
    print(x)
    print('phone numbers in list.')
    lines.seek(0)
    for line in range(len(numbers)):
        
        for line in numbers:
            phone=(line)
            country_code="1"
            client= httpx.AsyncClient()
            out = []
            await amazon(phone, country_code, client, out)
            for results in out:
                if results["exists"] == False:
                    lines.write("  --")
                    shortout = colored(text= phone + " [-] Exists: False", color="red")
                    print(shortout)
                elif results["exists"] == True:
                    shortout = colored(text= phone + " [+] Exists: True", color="green")
                    print(shortout)
                    f = open("valid.txt", "a")
                    f.write(phone)
                    f.close()
                    print("---")
                finish = time.perf_counter()
        print(f"Finished in {round(finish-start, 2)} second(s)")
a = input("paste your phone numbers in 'numberlist.txt', save then press ENTER key to continue.")
    
    


def task(id):
    import numbers
    
    trio.run(main)
    return "processed"


with concurrent.futures.ProcessPoolExecutor() as executor:
   results = [executor.submit(task(id), 1) for _ in range(30)]
       
for f in concurrent.futures.as_completed(results):
    print(f.result())
processes = []
#
for _ in range(30):
    
    p = multiprocessing.Process(target=task(id))
    id = multiprocessing.get_ident()
    p.start()
    multiprocessing.append(p)
    
#       
for process in processes:
    processes.join()
    
for process in processes:
    
    p.close()
    