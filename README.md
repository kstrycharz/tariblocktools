

# Tari Block Tools

Python programs for interacting with Tari block explorer.

---

## **Project Overview**

This repository contains two main modules:

1. **`tariHashing.py`**
2. **`tariblockexplorer.py`**

---

## **Dependencies**

### Required Python Packages:
- `requests`: For making HTTP requests to the Tari block explorer.
- `tari_hashing`: A Rust module for hashing.  

**Note**:  
- The Rust-based `tari_hashing` module is located in:  
  `\rust\target\wheels\tari_hashing-0.1.0-cp313-none-win_amd64.whl`.  
- You may need to recompile `lib.rs` to support your operating system and Python version.

---

## **Project Overview**

This repository contains two main modules:

1. **`tariHashing.py`**
   - Converts anonymous IDs (`anon_id`) into Blake2b hashed Base58 Monero encoded strings using a Rust-backed hashing module.

2. **`tariblockexplorer.py`**
   - Interfaces with the Tari block explorer (`textexplore-nextnet.tari.com`) to retrieve block information, outputs, and miner details.
  
---

## **Dependencies**

### Required Python Packages:
- `requests`: For making HTTP requests to the Tari block explorer.
- `tari_hashing`: A Rust module for hashing.  

**Note**:  
- The Rust-based `tari_hashing` module is located in:  
  `Tari-DiscordBot\rust\target\wheels\tari_hashing-0.1.0-cp313-none-win_amd64.whl`.  
- You may need to recompile `lib.rs` to support your operating system and Python version.

---

## **Usage**

### Module 1: `tariHashing.py`

#### **Description**  
Handles anonymous ID (`anon_id`) conversion to a hashed Base58 string.

#### **Class: `anonIdOperations`**
**Methods**:
- **`anonToBase58(anonId: str) -> str`**  
  Converts a single `anon_id` to its hashed Base58 Monero representation.

- **`anonListToBase58(anonIdList: list) -> list`**  
  Converts a list of `anon_id`s to their hashed Base58 Monero representations.


### Module 2: `tariblockexplorer.py`

#### **Description** 
Provides methods to retrieve and manipulate Tari blockchain data from the explorer.

#### **Class: `tariBlockExplorer`**
**Methods**:

- **`getLatestBlock() -> str`**
  Retrieves the most recently mined block number.

- **`getBlockInfo(blockNumber: int) -> list`**
Returns detailed information about a specific block.

- **`getBlockOutputs(blockNumber: int) -> list`**
  Returns a list of all outputs related to a block.

- **`getMinerInfo(blockNumber: int) -> list`**
  Retrieves miner information from the outputs of a block.

- **`getCoinbaseInfo(blockNumber: int) -> list`**
  Extracts the cleartext Coinbase extra data for each miner in a given block.

- **`decodeString(hex: list) -> str`**
  Decodes a hex string into cleartext.

- **`printList(list: list)`**
  Prints list items for debugging purposes.
