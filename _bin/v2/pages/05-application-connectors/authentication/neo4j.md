---
title: Neo4j Connector Guide
sidebar: cyclr_sidebar
permalink: neo4j-connector
tags: [connector]
---
{::options parse_block_html="true" /}
<section class="card">
# Neo4j Connector

You need the following details to setup the **Neo4j** connector in Cyclr:

- An AuraDB or self-hosted Neo4j Database.
- A Username and Password of a user assigned to that Database.
- The corresponding "neo4j+s" address. Example: **"neo4j+s://db123456.databases.neo4j.io"**
- We officially support Neo4j version 4.0 or greater.

### Cyclr Setup

A **Neo4j** Connector within Cyclr required the following values during the setup phase:

**Username**: The username attached to your Neo4j instance.

**Password**: The password attached to your Neo4j instance.

**Base URL**: The connection URL for your Neo4j Instance, it must use the 'neo4j+s' protocol, not HTTP.

**Database**: The name of the Database within your Neo4j instance you wish to connect to.

_You can connect 1 Database to a neo4j connector. If you wish to use multiple databases, you will need to install multiple connectors._

</section>
