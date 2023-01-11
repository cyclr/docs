

<section class="userguide" markdown="1">

## User Guide

<div class="section-content" markdown="1">

### Purpose

> **_PLEASE NOTE:_** Using Utility Connectors counts toward your overall task usage.

The **Generic Webhook** Utility Connector provides the typical HTTP Methods - **DELETE** **GET** **PATCH** **POST** **PUT** - allowing you to make HTTP Requests towards remote systems.  We strongly recommend however that although these methods are available it is preferable to use a 'proper' fully featured Cyclr connector.

The utility also provides a **Webhook** Method that can be used to trigger a Cycle from an inbound HTTP POST Request.  Useful if an application connector does not include a method specific to that requirement.

Each instance of the Webhook Method uses a unique URL to which a POST Request can be made.  You will need to define the Request body fields as Custom Fields when setting up the connector (see below).

As with all connectors, the **Generic Webhook** Utility Connector can be added multiple times.  This allows the Connector to be setup and named appropriately for each use case.


### Webhooks and Synchronous Webhooks

When a Request is sent to a **Webhook** Step in a running Cycle, a Response is sent back straightaway confirming whether the Request was accepted or not.  If it was accepted, Cyclr will go on to run the Cycle using the data it was given, but you won't hear anything more about it.

This gives you a kind of "fire and forget" process: you tell Cyclr to do some work and it says "ok".

If you use a **Webhook** Step and a **Synchronous Response** Step in a Cycle, Cyclr is then able to receive a Request through a Webhook Step as normal, but rather than just sending an "ok" Response, it will keep the connection open and run through the rest of the Cycle.  Once a **Synchronous Response** Step is reached, Cyclr will then send back a Response.  You can define what comes back in the Response using the Synchronous Response's Step Setup.

This allows you to tell Cyclr to do some work and for it to say "ok, please wait... here's your result".

We refer to this setup as **Synchronous Webhooks**.


### Passing Control between Cycles

The **Generic Webhook** Utility Connector can be used to link Cycles together.  For example, a step in Cycle 1 can make an HTTP POST to a Webhook that has been set up as a trigger to start Cycle 2.

This linking of Cycles might be done when an integration is large and complex, and splitting it into smaller units will improve maintainability.  It might also be done when the same processing needs to be run in a number of situations and linking is preferable to duplicating the same sequence of steps in multiple Cycles.

To set this up you will need to add custom fields to the Generic Webhook connector for the information that will be passed between the Cycles (see below).  The same fields will need to be added to both the 'POST' in the HTTP Methods section and to the 'Webhook' in the Webhooks section of the Connector Settings.

You should then build both of the Templates (or Cycles) before making the linkage.  When you add the Webhook trigger to Cycle 2 you will be given the URL it will use to listen for inbound Requests.  This should be copied and entered as the URL Field in Step Setup of the POST Step in Cycle 1.

When testing or running this kind of 'linked Cycles' structure you must start Cycle 2 before Cycle 1.  If you do not do this there is a danger that the webhook receiver will not be active before the first POST is made.

In this example, 2 Cycles have been used but the same procedure can be set up to chain together a whole series of Cycles.


### Mid-Cycle Webhooks

Webhook Steps can be used as the *first* Step in a Cycle as a way to receive data for processing, but they can also be used *part-way through* a Cycle - or "Mid-Cycle" - as a way of holding a Transaction until ready to proceed.

A reason why a Transaction might need to be held could be when performing some remote account setup or requesting an intensive data query to be executed; tasks that could take minutes or even hours before they're completed.

A Transaction will run through a Cycle as normal until it reaches a mid-Cycle Webhook Step.  There it will wait until that Webhook Step receives a Request indicating the Transaction can continue.

Mid-Cycle Webhooks have a **Webhook Mapping** section in Step Setup where you define what will trigger a Transaction to continue: you select the field in received Webhook Requests that will contain a value that matches another field found in the existing Transactions, e.g. a Job or Order ID.

Each time the mid-Cycle Webhook receives a Request, it will look for the most recent Transaction that has a matching value for the Webhook Mapping defined, and run that Transaction from there.  This can be done multiple times, causing a Transaction to be run from the mid-Cycle Webhook more than once.  This can be useful when processing data such as Orders where a notification might be received each time its status changes (e.g. from Received, Picked, Packed to Despatched).  In this situation, if you only wanted to continue when the Order's status was "Despatched", you could use a Decision Step after the Webhook Step to check the current status.

### Related Topics

[How to add custom fields](./adding-custom-fields) 

</div>

</section>
