import colorama
from colorama import init, Fore, Back, Style
import time
import secrets
from random import randint

continuing = True

btcval = 30000
print("""\n\033[36m                                                                                                                                                 


                        ░░░░  ░░            
                        ░░░░░░              
                                           
                            ▒▒▒▒░░          
                  ░░                  ░░░░  
              ▒▒░░                          
                    ▒▒██░░    ▓▓▓▓        ░░
            ░░      ██████    ████          
                      ░░                    
          ▒▒                                
            ▒▒                              
                                        ░░  
                ░░░░          ░░    ░░▒▒    

             ╔════════════════════════════╗
             ║     Clouds Wallet Gen      ║
             ╚════════════════════════════╝
   ╔═══════════════════════════════════════════════╗
   ║   Please put in your Bitcoin Wallet Address:  ║
   ╚═══════════════════════════════════════════════╝
""")
input(">")

for i in range(100000000):
  if continuing == True:
      time.sleep(0.01)
      ranInt = randint(0,2500)
      if ranInt <= 1:
        randomBTC = randint(1,1000) / 100
        if randomBTC % 1 == 2:
           print(Fore.GREEN + "╔═══════════════════════════════════════════════════════════════════════════════════════╗")
           print(Fore.GREEN + "             " +secrets.token_hex(randint(17,22)) + "     -     " + str(randomBTC) + "BTC")
           print(Fore.GREEN + "╚═══════════════════════════════════════════════════════════════════════════════════════╝")
        else:
           print(Fore.GREEN + "╔═══════════════════════════════════════════════════════════════════════════════════════╗")
           print(Fore.GREEN + "             " +secrets.token_hex(randint(17,22)) + "     -     " + str(randomBTC) + "BTC")
           print(Fore.GREEN + "╚═══════════════════════════════════════════════════════════════════════════════════════╝")
           print("╔══════════════════════════╗")
           print("  Transfer Funds? (Y/N) ")
           print("╚══════════════════════════╝")
        answer = input(">")
        if answer == "y" or answer == "Y":
          continuing = True
        else:
          continuing = False
      else:
        print(Fore.RED + secrets.token_hex(randint(17,22)))
  else:
    break  
