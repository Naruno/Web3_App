# Address Ping System (Web3) for Naruno
Address Ping System (Web3) is a tool designed to check the online status of servers associated with blockchain addresses in Naruno. With Web3, you can ensure that the servers you want to communicate with are online and reachable before sending any messages or making any transactions.

## Features
- Decentralized system
- Secure communication between nodes
- Fast and easy to use
- Checks online status of servers associated with blockchain addresses

## Installation
You can install Web3 by pip3:

```console
pip3 install web3_app
```

## Usage

*If you want to use web3_app you must to use Naruno. For now please checkout the [Baklava Testnet](https://naruno.org/baklava-testnet/).

Getting address of client and server:
```console
narunocli -pw
```

### Server
For a server to be pinged by Web3, it needs to have a corresponding Web3 entry with trusted user addresses set up.

```python
from web3_app import web3

my_web3_server = web3("MyNarunoPass")

my_web3_server.add_user("client_address")

my_web3_server.run()
```

also you can use in command line:
```console	
web3 --password MyNarunoPass --trusted_users ["client_address"] run
```

### Client
To use Web3, you can call the web3.ping function with your blockchain address and the server's blockchain address as parameters:

```python
from web3_app import web3

my_web3_client = web3("MyNarunoPass")

result = my_web3_client.ping("server_address")

print(result)

my_web3_client.close()
```

also you can use in command line:
```console	
web3 --password MyNarunoPass ping "server_address"
```


This will return a boolean value indicating whether the server associated with the provided blockchain address is online and reachable.

## Contributing
Contributions to Web3 are welcome! If you have any suggestions or find a bug, please open an issue on the GitHub repository. If you want to contribute code, please fork the repository and create a pull request.

## License
Web3 is released under the MPL-2.0 License.
