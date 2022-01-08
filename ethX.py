import requests
import time
import sha3
from ecdsa import SigningKey,SECP256k1
from bs4 import beautifullSoup

i=1
while (i<=7):
  keccak = sha3.keccak_256()
  priv = SigningKey.generate(curve=SECP256k1)
  pub = priv.get_verifying_key().to_string()
  
