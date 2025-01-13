"""
File: tariblockexplorer.py 
Author: Kyle Strycharz                                                                                                               
Last Modified: 1/12/2024   
Python: 3.13.0                                              
Version: 1.1.0
 

                                                      
Description:                                                                     
Scrapes textexplore-nextnet.tari.com  for block infomation                                                                                                       |
Usage:

    newObject = tariBlockExplorer() when appending this file
    
    In new file
    import tariblockexplorer
    newObject = tariblockexplorer.tariBlockExplorer()

Mutiple methods are avaliable. Including:

        - getLatestBlock - Retrieves most recent mined block on Tari chain
        - getBlockInfo(int blockNumber) - Retrieves information about a provided block
        - getBlockOutputs(int blockNumber) - Retrievs a lit of everyting relating to a specified block
        - getMinerInfo(int blockNumber) - Retrieves a list of everything relating to each output(miner) for a specified block
        - getCoinbaseInfo(int blockNumber) - Retrieves information about each miner's Coinbase Extra Data for a given block in cleartext
        - decodeString(int blockNumber) - decodes a hex string in this format [aa, bb, cc, dd, ...] into a cleartext string
        - printList(int blockNumber) - used to print a list in an organizaed way (DEBUGGING)
        - getBlockPages() - returns a list of additional links with url endpoints with more outputs assosicated with a block. blocks/<blocknum>
        returns only the first 9 outputs. The additional pages cover the rest. (outputsNextLink value when /block is returned)

**Any function starting with a get, returns a list. This allows for app builders to manipulate data how they like



Implement class into your applicaiton. See test cases at botom of this file           


                                                                         |
"""

import requests



class tariBLockExplorer:

    #Initialize critical variables
    mainSite_url = "https://textexplore-nextnet.tari.com"
    blockExplorer_url = "https://textexplore-nextnet.tari.com/blocks/"
    addJson = "?&json"
    


    ##NEED TO MAKE REQUEST A GLOBAL VAR TOO

    #Returns the number of the latest block (Tip of Chain)
    def getLatestBlock(self):
        #print("requesting current block")
        try:
            chainInfo = requests.get(self.mainSite_url + self.addJson).json()
         
            latestBlock = chainInfo["tipInfo"]["metadata"]["best_block_height"]

        except Exception as e: 
            
            latestBlock = "Failed to retrieve chain tip from Tari Block Explorer."

       # print("RETURNING BLOCK DATA: " + latestBlock)
        return latestBlock
        
    
    #Returns a json response containing info on a specic block number

    def getBlockInfo(self, blockNumber):
        #print(blockNumber)
        #print("Preparing to request for: " + blockNumber)


        try:
            blockInfo = requests.get(self.blockExplorer_url + str(blockNumber) + self.addJson).json()

        except Exception as e:

            blockInfo = f"Failed to retrieve information on block #{blockNumber}"


   
        
        return blockInfo
    

    #Returns a list of additional links for block outputs. /block on api only responds with first 9. The rest are generated on additional pages
    def getBlockPages(self, link):

        #link = "86219?outputs_from=20&outputs_to=30&inputs_from=0&inputs_to=10&kernels_from=0&kernels_to=Na"
        
        # QUERY BLOCK
        

        blockLinks = []
        blockLinks.append(link)
        blockInfo = self.getBlockInfo(link)

        while blockInfo["body"]["outputsNextLink"] is not None:
           
            outputsNextLink = blockInfo["body"]["outputsNextLink"]
            newLink = outputsNextLink.split("/blocks/")[1] if "/blocks/" in outputsNextLink else ""
            blockLinks.append(newLink)
            blockInfo = self.getBlockInfo(newLink)

        return blockLinks
        

    #Returns a json  list of miners who miner a block
    def getBlockOutputs(self, blockNumber):

        blockLinks = self.getBlockPages(blockNumber)
        #print(blockLinks)
        outputsList = []

        for link in blockLinks:
            #print(link)
            blockInfo = self.getBlockInfo(link)
        
            if type(blockInfo) == str:
                return blockInfo

            outputsData = blockInfo["body"]["outputs"]

            for output in outputsData:
                outputsList.append(output)
            #try:
            #    outputsList.append(blockInfo["body"]["outputs"])
            #except KeyError as e:
            #    return f"Key {e} not found in block info"
        #print(len(outputsList))
        return outputsList




                
               




    #Parses Miner info from block info. Returns a list of kernels responsible
    def getMinerInfo(self, blockNumber):
        
        miners = []


       
        outputList = self.getBlockOutputs(blockNumber)
        
        
        
        for x in range (len(outputList)):


            try:
                miners.append(outputList[x]["features"])
            except KeyError as e:
                
                return f"Key {e} not found in block output info"
            except TypeError as e:
                return f"outputList is a {e} Variabel passes is not a List error. Invalid blockOutput info."


    

        return miners
    
    #Maybe this could take a miners variable, but I am not sure, ATM it will ask for a block number

    #Returns the following info:
    # Element     Value 
    #   0         <TBD IDK>
    #   1         anon key hashed in blake2b (Tari's implementation (insert link here)) Then encoded in base 58
    #   2         Miner version
    #   3         <TBD IDK>
    def getCoinbaseInfo(self, blockNumber):

        miners = self.getMinerInfo(blockNumber)

        coinbaseDecoded = []

        
 

        for x in range(len(miners)):
            temp = miners[x]["coinbase_extra"]["data"]
            try:
                
                
                temp = miners[x]["coinbase_extra"]["data"]
                
            except Exception as e:
                return f"temp has {e}"
            except KeyError as e:
                return f"Key {e} not found in Miner info"


            if type(temp) != list:
                return f"{temp} is not a hex list"
            

            decodedHex = self.decodeString(temp)

            coinbaseDecoded.append(decodedHex)
        
        
        #self.printList(coinbaseHexList) #Debugging Only

        return coinbaseDecoded



    #Decodes a given hex. Mainly for Coinbase Extra Data value for each output
    #TODO regex to determine if it is proper hex
    def decodeString(self, hex):

         decoded_string = ''.join(chr(x) if 32 <= x <= 126 else '?' for x in hex)

         return decoded_string



    #Prints a list, for Debugging only. Each item is seperated by a line.
    #Make more organizaed
  
  

# TEST CASES

#test = tariBLockExplorer()

#Get latest block
#print(test.getLatestBlock())

#Get ouput of block

#print(test.getBlockOutputs(86219))
#test.getBlockOutputs(86219)
#print(test.getMinerInfo(86219))
#print(test.getCoinbaseInfo(86219))
#print(test.getBlockPages(86219))














