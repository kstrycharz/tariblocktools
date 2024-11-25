
import tari_hashing


"""
File: tariHashing.py
Author: Kyle Strycharz                                                                                                               
Last Modified: 11/24/24
Python: 3.13.0                                          
Version: 1.0.0

Description: Used to convert your anon_id in app_config.json of Tari Universe to a blake2b hashed  base58 monero encoded string.

Packages:
        - tari_hashing: Module built in Rust to convert anon_ids to a blake2b hashed base58 monero encoded string. It can be found in this repo here: Tari-DiscordBot\rust\target\wheels\tari_hashing-0.1.0-cp313-none-win_amd64.whl
        NOTE: you made need to recompile lib.rs to support your OS and version of python

"""

class anonIdOperations:

    def anonToBase58(self, anonId):

        encoded_hash = tari_hashing.blake2b_base58(anonId)

        return encoded_hash
    
    def anonListToBase58(self, anonIdList):
        convertedList = []

        # Iterate over the list of anonIds and convert each
        for anonId in anonIdList:
            convertedList.append(self.anonToBase58(anonId))
        
        return convertedList




### Example usage

#privateAnon = "anon id"
#privateAnonList = ["anon id 1", "anon id 2"]


#exampleObject = anonIdOperations()
#print("Single String")

#print(exampleObject.anonToBase58(exampleObject))
