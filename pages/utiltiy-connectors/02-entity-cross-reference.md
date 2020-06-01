---
title: Entity Cross Reference
sidebar: cyclr_sidebar
permalink: entity-cross-reference-connector
tags: [utility-connector]
---

## Entity Cross Reference Use Case

Entity Cross Reference is a built-in Cyclr connector that manages references across two systems for you.

A common use case for it is to synchronise entities in e.g. a CRM system and an email marketing system by keeping track of the number of entities in them.

## Create Entity Cross Reference

To create an Entity Cross Reference, the minimum values you should set are the IDs of Entity 1 and Entity 2 plus the name of the source application.

We also provide two pairs of additional fields in the Create method: Entity Name and Entity Record Count.

If you have any extra entity property, it can be added as a custom field following this naming convention: `Entity1.ExtraProperty` and `Entity2.ExtraProperty`.

If you have additional shared information for both entities, it can be added as a custom field in this naming convention: `AdditionalInfo`. Shared fields cannot begin with `[].`, `Entity1.` or `Entity2.`.

## Get Entity Cross Reference(s)

There are three methods for getting Entity Cross Reference(s):

- Get All Cross References: returns all cross references in a collection.
- Get Cross Reference By Entity 1 ID: finds Entity 1, Entity 2 and their shared information using the ID of Entity 1.
- Get Cross Reference by Entity 2 ID: finds Entity 1, Entity 2 and their shared information using the ID of Entity 2.

## Update Entity Cross Reference

You can update any entity (Entity 1 and Entity 2) and their shared information by providing the ID for one of the entities.

In the Update method, all properties in both entities and their shared properties are optional, which means only the provided value will be saved, i.e. incremental updates.

For example, if you want to update the Entity 1 Record count, you only need to set its new value and provide the ID of either Entity 1 or Entity 2.

## Delete Entity Cross Reference

You can delete any entity (Entity 1 and Entity 2) and their shared information by providing the ID of one of the entities.
