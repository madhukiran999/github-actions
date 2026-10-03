import os
import requests
import time

def ping_url(url,delay,max_trails):
   trails=0
   while trails < max_trails:
      try:
         response=requests.get(url)
         if response.status_code==200:
            print(f"website {url} is reachable")
      except requests.ConnectionError:
         print(f"website {url} is unreachable retry in {delay} seconds..")
         time.sleep(delay)
         trails += 1

      except requests.exceptions.MissingSchema:
         print(f"invalid url {url}. make sure it has valid schema ")


   return False




   
def run():
   website_url = os.getenv("INPUT_URL")
   delay=int(os.getenv("INPUT_DELAY"))
   max_trails=int(os.getenv("INPUT_MAX_TRAILS"))

   website_reachable = ping_url(website_url,delay,max_trails)

   if not website_reachable:
      raise Exception(f"website is unreachable after {max_trails} attempts. Please check the url {website_url} and try again")
      
   print(f'{website_url} is reachable')




if __name__ == "__main__":
   run()