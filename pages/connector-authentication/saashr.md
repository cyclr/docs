---
title: SaaShr Authentication
sidebar: cyclr_sidebar
permalink: saashr-connector
tags: [connector]
---

<a name="saashr-setup"></a>

# SaaShr setup

You will need the following to authenticate the SaaShr connector in an account:

1. The `username` for your SaaShr account.
2. The `password` for your SaaShr account. For the first time setup, this will be set as your account password.
3. The short `company name` for your SaaShr account.
4. The URL of your SaaShr installation. For example, if you access SaaShr using `https://secure.saashr.com` then enter `https://secure.saashr.com`.
5. The `API key` of your SaaShr account.

If you do not have any of this information, please contact your SaaShr account manager.

<a name="first-time-setup"></a>

### First time setup

When installing the SaaShr connector for the first time you need to enter an additional `setup password`. This will be provided by SaaShr as an auto-generated password that will be changed to the `password` value on first installation. Further authentications of the same SaaShr account will then only require the `password` that was entered on the first installation to be provided.

<a name="cyclr-setup"></a>

# Cyclr setup

<a name="account-setup"></a>

### Account setup

You will be asked for the following values when installing the SaaShr connector within an account:

| Value              | Description                                                                                                                                      |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Base URL**       | The URL of your SaaShr installation. For example, if you access SaaShr using `https://secure.saashr.com` then enter `https://secure.saashr.com`. |
| **Company Name**   | The short company name for your SaaShr account. All methods will make calls using this company name.                                             |
| **Username**       | The username for your SaaShr account.                                                                                                            |
| **Password**       | The password for your SaaShr account. For the first time setup, this will be set as your account password for subsequent installations.          |
| **Setup Password** | Only required if this is your first time integrating with the API. This is an auto-generated password provided by SaaShr.                        |
| **API Key**        | The API key of your SaaShr account.                                                                                                              |
