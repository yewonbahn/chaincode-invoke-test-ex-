#!/usr/bin/env python



import time
import os
import random

from threading import Thread
from multiprocessing import Pool
from datetime import datetime
now = datetime.today()
start_time=time.time()
def f(name,start,end):
	a="peer chaincode invoke -o localhost:7050 --ordererTLSHostnameOverride orderer.example.com --tls --cafile ${PWD}/organizations/ordererOrganizations/example.com/orderers/orderer.example.com/msp/tlscacerts/tlsca.example.com-cert.pem -C mychannel -n basic --peerAddresses localhost:7051 --tlsRootCertFiles ${PWD}/organizations/peerOrganizations/org1.example.com/peers/peer0.org1.example.com/tls/ca.crt --peerAddresses localhost:9051 --tlsRootCertFiles ${PWD}/organizations/peerOrganizations/org2.example.com/peers/peer0.org2.example.com/tls/ca.crt -c '{\"Args\":[\"CreateAsset\","
	b=",\"extract image\","
	c=",\"MFTECmd.exe\",\"C:programfiles\",\"File_Created\",\"Directory\",\"yewon\"]}'"
	e=",\"extract image\""
	d=random.randint(1, 1000000000)
	for i in range(start,end):
		d=random.randint(1, 5000000000)
		answer=a+"\""+now.isoformat()+"\""+e+",\""+str(d)+"\""+c
		print os.system(answer)
		print(i)
   

if __name__ == '__main__': 

	th1 = Thread(target=f, args=(1, 0, 12500))
	th2 = Thread(target=f, args=(2, 12500, 25000))
	th3 = Thread(target=f, args=(3, 25000, 37500 ))
	th4 = Thread(target=f, args=(4, 37500, 50000))
	th5 = Thread(target=f, args=(5, 50000, 62500))
	th6 = Thread(target=f, args=(6, 62500, 75000))
	th7 = Thread(target=f, args=(5, 75000, 87500))
	th8 = Thread(target=f, args=(6, 87500, 100000))

    
	th1.start()
	th2.start()
	th3.start()
	th4.start()
	th5.start()
	th6.start()
	th7.start()
	th8.start()

	th1.join()
	th2.join()
	th3.join()
	th4.join()
	th5.join()
	th6.join()
	th7.join()
	th8.join()
	
	
