#Net_O_Phish

##Summary
This program is the web server to be used in tandem with the Phishery program. This server will listen for and log requests when recipients of Phishery emails click on spoofed links. These requests will have embedded information specific to the email recipient which will provide insight into who clicks the links. 

##Setup

Additionally, this program relies on an external mysql server instance. The mysql server may vary upon implementation, but the configuration details should be placed in the private config.yaml file.

DAO representations of the tables should be defined in DAO.py

Twisted resources found in TwistedResources.py represent individual url paths for the web server. These may be created and changed as needed to accept parameters from the Phishery emails. The server will run on the port specified by twisted.port in config.yaml 
* [Twisted Documentation](http://twistedmatrix.com/trac/)

##Getting Started

This program requires python 3, and the following dependencies:
* PyMySQL
* PyYAML
* SQLAlchemy
* Twisted

These can be installed using pip3.
```
pip3 install <dependency>
```

Once these are installed, the program can be started using the following command:
```
python3 WebServer.py
```

At this point, the server is listening , and requests may be directed to it.

Logs of the requests can be found in /out/requests.log