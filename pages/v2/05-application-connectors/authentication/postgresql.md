---
title: PostgreSQL authentication
sidebar: cyclr_sidebar
permalink: postgresql-connector
tags: [connector]
---
{::options parse_block_html="true" /}
<section class="card">

## Cyclr setup

Cyclr asks you for the below values when you install the PostgreSQL connector into an account:

| Value               | Description                                                  |
| :------------------ | :----------------------------------------------------------- |
| **Host**            | The IP address or fully qualified domain name of the PostgreSQL server. |
| **Post**            | The port to connect to the PostgreSQL server with.           |
| **Username**        | The username to connect to the PostgreSQL server with.       |
| **Password**        | The password to connect to the PostgreSQL server with.       |
| **Database**        | The name of the database on the PostgreSQL server to access. |
| **SSL Connection?** | Set to **True** to connect to the PostgreSQL server using an SSL connection. Set to **False** to connect to the PostgreSQL server directly. When enabled, the **Validate SSL Certificate** field needs to be provided. |
| **SSL Certificate** | The self-signed SSL certificate to use when establishing an SSL connection to the PostgreSQL server. Set to `False` to disable SSL certificate validation when establishing an SSL connection to the PostgreSQL server. |
| **SSH Tunnel?**     | Set to **True** to connect to the PostgreSQL server using an SSH tunnel. Set to **False** to connect to the PostgreSQL server without an SSH tunnel. When enabling this, **SSH Host** and **SSH Port** need to be provided. Which combination of **SSH Private Key**, **SSH Username**, and **SSH Password** is required depends on your SSH host. |
| **SSH Host**        | The IP address or fully qualified domain of the SSH tunnel to connect to the PostgreSQL server through. |
| **SSH Port**        | The port of the SSH tunnel to connect to the PostgreSQL server through. |
| **SSH Username**    | The username to connect to the SSH tunnel with.              |
| **SSH Password**    | The password to connect to the SSH tunnel with.              |
| **SSH Private Key** | The private key to connect to the SSH tunnel with.           |

> Note: You can use different details for different accounts.

</section>
