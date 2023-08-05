# Address Ping System (APS) for Naruno
Address Ping System (APS) is a tool designed to check the online status of servers associated with blockchain addresses in Naruno. With APS, you can ensure that the servers you want to communicate with are online and reachable before sending any messages or making any transactions.

## Features
- Decentralized system
- Secure communication between nodes
- Fast and easy to use
- Checks online status of servers associated with blockchain addresses

## Installation
You can install APS by pip3:

```console
pip3 install address_ping_system
```

## Usage

*If you want to use address_ping_system you must to use Naruno. For now please checkout the [Baklava Testnet](https://naruno.org/baklava-testnet/).

Getting address of client and server:
```console
narunocli -pw
```

### Server
For a server to be pinged by APS, it needs to have a corresponding APS entry with trusted user addresses set up.

```python
from address_ping_system import aps

my_aps_server = aps("MyNarunoPass")

my_aps_server.add_user("client_address")

my_aps_server.run()
```

also you can use in command line:
```console	
aps --password MyNarunoPass --trusted_users ["client_address"] run
```

### Client
To use APS, you can call the aps.ping function with your blockchain address and the server's blockchain address as parameters:

```python
from address_ping_system import aps

my_aps_client = aps("MyNarunoPass")

result = my_aps_client.ping("server_address")

print(result)

my_aps_client.close()
```

also you can use in command line:
```console	
aps --password MyNarunoPass ping "server_address"
```


This will return a boolean value indicating whether the server associated with the provided blockchain address is online and reachable.

## Contributing
Contributions to APS are welcome! If you have any suggestions or find a bug, please open an issue on the GitHub repository. If you want to contribute code, please fork the repository and create a pull request.

## License
APS is released under the MPL-2.0 License.
