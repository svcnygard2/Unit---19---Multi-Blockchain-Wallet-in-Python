# Unit - 19 -Multi-Blockchain-Wallet-in-Python

This code creates a 'universal' wallet that manages multiple crypto coins allowing for portfolio-like management of multiple coins. For this test, I used Ethereum and Bitcoin Testnet. This code uses a command line tool, hd-wallet-derive that supports BIP32, BIP39, and BIP44 as well as non-standard derivation paths.

# Adding HD-Wallet-Derive
PHP should be installed for hd-wallet-derive to work.  The hd-wallet-derive library is written in the PHP language.  Install hd-wallet-derive by:
1. Open a fresh terminal as *Administrator*.
    - Input "C:\Program Files\Git\bin\bash.exe directly into the system search bar and launch as *Administrator*.

2. With your terminal open, cd into your 'Blockchain-Tools' folder and run the following code:
  - git clone https://github.com/dan-da/hd-wallet-derive
  - cd hd-wallet-derive
  - curl https://getcomposer.org/installer -o installer.php
  - php installer.php
  - php composer.phar install

### You should now have a folder called hd-wallet-derive. Verify that it works by:

3. Run the command to cd into hd-wallet-derive
4. Execute the following command:
  - ./hd-wallet-derive.php -g --key=xprv9tyUQV64JT5qs3RSTJkXCWKMyUgoQp7F3hA1xzG6ZGu6u6Q9VMNjGr67Lctvy5P8oyaYAL9CAWrUE9i6GoNMKUga5biW6Hx4tws2six3b9c --numderive=3 --preset=bitcoincore --cols=path,address --path-change

 5. Once verified open *Administrator* Bash and cd to Block-chain tools and runt he following:

  - export MSYS=winsymlinks:nativestrict
  - ln -s hd-wallet-derive/hd-wallet-derive.php derive

  To verify it's working type the following two commands into your command line:
  - export MSYS=winsymlinks:nativestrict
  - ln -s hd-wallet-derive/hd-wallet-derive.php derive

  Test that it's working by entering:
  - ./derive -g --mnemonic="YOU'RE MNEMONIC HERE" --cols=path,address,privkey,pubkey

  Here are [instructions](requirement.txt) on how to install the additional dependencies.

# Running wallet.py
### This function is built to send ETH and BTCTEST coins:

    def send_tx(coin, account, recipient, amount):
      tx = create_raw_tx(coin, account, recipient, amount)
      if coin == ETH:
          print(w3.eth.getBalance(eth_account.address))
          try:
            signed_tx = account.sign_transaction(tx)
            return print(w3.eth.sendRawTransaction(signed_tx.rawTransaction))
          except:
            return print ("Was not able to send" + f"{coin} coins.")
      if coin == BTCTEST:
          print(account.get_balance('btc'))
          try:
            signed_tx = account.sign_transaction(tx)
            NetworkAPI.broadcast_tx_testnet(signed_tx)
            transaction = account.get_transactions()[0]
            return print("Your Transaction Hash is : " + f"{transaction}.")
        except:
            return print ("Was not able to send" + f"{coin} coins.")

### To send Ether, use the following command:

    send_tx(ETH, eth_account, send_eth, 3)

![Test Ether Confirmation](Screenshots/eth.png)

### To send TEST BTC, use the following command:

    send_tx(BTCTEST, btctest_account, send_bit, 0.0000001)

![Test BTC Confirmation](Screenshots/bit_testnet_tx.png)

# IV. Next steps 
Next is to code for other coin types to increase the functionality of the wallet.

# I. Dependencies
- subprocess
- json
- os
- constants.py
- bit
- web3