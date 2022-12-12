
<section class="setup partner" markdown="1">

## Partner Setup

<div class="section-content" markdown="1">

The following parameters are required to connect to a MongoDB server:

- **Prefix**: Select either 'mongodb' or 'mongodb+srv'. Use 'mongodb+srv' if you are using Atlas or have set up a SRV DNS record.
- **Server**: The server parameter supports the following formats:
	- \_hostname with optional port, for example
	mydb.xyz.mongodb.net
	mydb.mongo.cosmos.azure.com:10255
	- \_multiple comma seperated hostnames with optional ports, for example
	mycluster-shard-00-00.xyz.mongodb.net:27017,mycluster-shard-00-01.xyz.mongodb.net:27017,mycluster-shard-00-02.xyz.mongodb.net:27017
- **User**
- **Password**
- **Database Name**: The database name you want to connect to.
- **Connection Properties**: Additional properties that may be required. Usually these can be identified in a connection string as anything appearing after the '?'. Some examples are:
	- \_Atlas: retryWrites=true&w=majority
	- \_Cosmos DB: ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@your-app-name@

See [the MongoDB documentation](https://docs.mongodb.com/manual/reference/connection-string/) for more information, including the creation of SRV DNS entries.

### Supported Versions
Currently, the following versions of MongoDB are supported:
- 5.2
- 5.1
- 5.0
- 4.4
- 4.2
- 4.0
- 3.6

</div>

</section>
