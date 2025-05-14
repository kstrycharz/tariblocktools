##EXAMPLE FOR QUERYING ENTIRE BLOCK EXPLORER FOR WHAT BLOCKS YOU WON via ANONID


import tariblockexplorer
import tariHashing

TU_ANON_ID = "" #Tari Universe App AnonID

anonConversion = tariHashing.anonIdOperations()




anon = anonConversion.anonToBase58(TU_ANON_ID)


explore = tariblockexplorer.tariBLockExplorer()


tip = explore.getLatestBlock()
query = 1


while query < int(tip):

    try:
        cb_info = explore.getCoinbaseInfo(query)
    
    
        for output in cb_info:
            output = output.split(',')
        
       
        try:
            if output[1] == anon:
                print(f"{anon} won block {query}")
        except:
            print(f"Error at Output {output}")
        
    except:
        print(f"Error at block {query}")

    print(f"Just Scanned {query}")
    tip = explore.getLatestBlock()
    query = query + 1

    

