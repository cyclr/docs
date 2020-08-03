---
title: SFTP Private Key Authentication
sidebar: cyclr_sidebar
permalink: sftp-private-key
tags: [connector]
---

To authenticate the SFTP Private Key connector you will need to provide the following values.

## HOST Uri ##

You need to provide the URI where the SFTP server is located.

````
sftp://example.com
````

## User Name ## 

You need to provide the username of the user to authenticate with the SFTP server as.

````
sftp_user
````

## Private Key ##

You need to provide the PKCS #1 RSA private key that the SFTP server knows as an _authorized_keys_ for the user.

````
-----BEGIN RSA PRIVATE KEY-----
MIIEogIBAAKCAQEAv9fnWThDaI2kVqkZrI0euSHEQBea2yewrcth78GpD9JfFMvd
gT8kjs5JzHFi8uo10YRdvexD0ILXzgt/AF7NuwWiw8VPQANAl9Y/11oZns+OUgzR
JojRFazycDymLgNxPpAqZdX9bO39M6Eo/3+zh/7Apudpx2Q3B6Y6RxKRukpuw5hQ
NCA1TaA6A7I2t7SYE6LiJapG4GP+w7oRYGUaZ2f/bvnGEaBBlN0d3ITJa4NvkfPF
D1bfkB/2wrol6wKgndo6Uzmqm3BFb+vZUU+M5I5vQyW0xl6mozpgAZDWV7g4G2ZM
AsXny+ijISJjHNXNRlzNZWqc4GxkrgazkeEGmQIDAQABAoIBAAQ6GZrZpoKTPF+8
chhfM6IYoF5ZJsxVX4s0w/+oYLU8iWPH6iWC4qdS3EVo6ik4B9+J7xbUMdpSR7b+
gdncPOQ2B5QQsOJUMAQocFeqYI4jPJuKNMGImjLEEMNwUqkI4mHig0yjHmZcCAwv
LNwUUDxa3JvQ1X/TMXM1smsGebeFCoVYggHeF4hiQRqa6Q9C1NvgMFEHt9PsW8Ag
Rt1VgMQtwLjN5p4HDn4Ttjd/lhtShIxSK10+idsAZewOhFt4GwjtJ/tV5mp8Hx+l
u6tATzKxpA9/wfKBBEuja3vXQWpICbDsohy4A0NfhF2PqMgMUHRNA8sKjZEVZuuA
9jyV4kECgYEA8rHkyUIDsTcNKRWL2QlHS8ORAKA6TqXzoAHBj5Cw8D2ydL230izM
JIf7cesH9/xjocoyv+3k5x8PB9a2cNYtOZATHUgQJuVEjiFLAVoQAgTm7Y41H8t9
FPxRkKE7FdGGIHSBjD/E5PMhGiiX1n8aVrm3qr3W+YRzTu7v0yDK6QUCgYEAylxV
U3dpkGnvsyvXtfBlee1QQFSAILaBcocbbxaNf6u+mdcWFqeLsFnJgj523EPBgtEz
P2JZT2SceGop7XXnZXPcOgf98kT3qd/ZsjTyhWCRvn2os8gBsXJ7wgif/Tzlgo/J
+PZlANQIHP2ANLwH9hX1QG24Z9sXk9AhNI4jy4UCgYBgfHcPyG39W3yg8874h2bP
6T1RuWHU+Mcluu0ALa8ao/y5yt808NhsQZ+mx6EQZ0gY/3EzutmBRWjNXgCEVbH/
K5dd0dOSEx4xP205aVvp4ZcJpLrcHCNrX3DyBheecgFYD9mdL5EQ0NQ9ORw8i6Wm
CwnJGNZJtu282OOB1Yy2HQKBgGolnthmdeg7uXFpmQAltoULd6IW8RK3yRUTS8+s
q9KBezxlN3/wqPR7VJlOPLjzjakaJWClLSXZJ75+KboWs6di6+1AzfNsO+FOu3mg
DmrqKekbLwgG7ORwofw42/tRGy6uUAqY7IhPsGXMj5iZ3S83e2stYqKPqUFu1kwk
FyClAoGAMdqMGicntRIqRjOB/P80rbD4w5VctjCzmB+qopbU8n/rqVcqqyXgqO8R
YXmlBTmJEWSQ52vNFxyjpeWFcwJBCF4QOJQucJCUgUzdOQgy0wZ3ieIfO2wOzehB
U+RfJn9l5kWbZLhVkb9AlVP8MA6VOM2U+LfW7Z/7gOslnoMMosk=
-----END RSA PRIVATE KEY-----
````

## Parsephrase (Optional) ##

If the private key requires a parsephrase you can provide it here, if there isn't a passphrase you should leave this blank.

## Server Time Zone ##

You need to provide the timezone used by the SFTP server, if not set correctly the **List Updated Files** method will not function correctly.

````
Europe/London
````

## IP Whitelisting ##

If the SFTP server is not publicly accessible ensure you allow Cyclr to connect.
See [Cyclr IP Whitelisting](https://docs.cyclr.com/cyclr-ip-whitelisting)
