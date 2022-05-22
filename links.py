import json
from pyrfc3339 import generate
from web3 import Web3   
from abis import abis
import random
ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))
abise = abis()
abi=json.loads(abise)
address=web3.toChecksumAddress("0x0476AfeAb5326Cdc159bF6Fd51f9d9ce4c6dDc7c")
contract=web3.eth.contract(address=address,abi=abi)


############################################################## user verification using aadhar ##############################################################
def add_aadhar(aadhar_no):
     web3.eth.defaultAccount = web3.eth.accounts[0]
     h=contract.functions.aadhar_user(str(aadhar_no)).transact()
     web3.eth.waitForTransactionReceipt(h)
     return h
     

def verify_user(aadhar_no):
  if len(str(aadhar_no))==12:  
    a=0
    web3.eth.defaultAccount = web3.eth.accounts[0]
    h=contract.functions.get_adhaar_status(str(aadhar_no)).call()
    #print(h)
    if h=="Not Voted":
      sett=add_aadhar(aadhar_no)
      #print(sett)
      return "not voted"
    else:
      return "You Already Voted"
  else:
    return "Invalid Aadhar Number" 

#####################################################################################################################################################
def ownerr():
    web3.eth.defaultAccount=web3.eth.accounts[0]
    h=contract.functions.owner().call()
    return h


def generate_add():
    a=random.randint(1,9)
    b=web3.eth.accounts[a]
    return b,a

def authorisess(b):
    web3.eth.defaultAccount = web3.eth.accounts[0]
    h=contract.functions.authorize(str(b)).transact()
    h=web3.eth.waitForTransactionReceipt(h)
    #print(h)
    return h






def add_candidate(name,region,party):
    web3.eth.defaultAccount = web3.eth.accounts[0]
    h=contract.functions.addCandidate(str(name),str(region),str(party)).transact()
    h=web3.eth.waitForTransactionReceipt(h)
    #print(h)
    return "sucess"





#####################################################################################################################################################

def vote(name,region,party,i):
  web3.eth.defaultAccount = web3.eth.accounts[i]
  print(web3.eth.defaultAccount)
  h=contract.functions.vote(str(name),str(region),str(party)).transact()
  #print(h)
  h=web3.eth.waitForTransactionReceipt(h)
  return h
  
def get_no_of_candidates():
    s=contract.functions.get_no_candidates().call()
    print(s)
    for i in range (int(s)):
      print(contract.functions.candidates(i).call())



def get_candidate_details(index):
    web3.eth.defaultAccount = web3.eth.accounts[0]
    l=[]
    for i in range(index):
      s=contract.functions.candidates(index).call()
      l.append(s)
    return l