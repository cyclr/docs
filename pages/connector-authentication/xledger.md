---
title: Xledger Authentication
sidebar: cyclr_sidebar
permalink: xledger-connector
tags: [connector]
---

## Partner Setup

#### Retrieving Certificate

*   Download the [Certificate Manager](https://www.microsoft.com/en-us/p/xledger-certificate-manager/9n0q2h72x5x8?activetab=pivot:overviewtab) from the Microsoft Store.
*   Click "Get New Certificate".
*   Fill in your username and password, and then click "Get Security Code" and check your emails for said security code.
*   Enter the security code, **enable "Exportable"**, and then click "Get Certificate".
*   You have now created a new Xledger certificate. You can access it by navigating to "certmgr" by typing "Manager user certificates" into the Windows search bar.
*   Under "Personal" > "Certificates", you should see a certificate issued by "XLEDGER.NET".
*   Double click on it, go to the "Details" tab, and then click "Copy to File".
*   Go through the stages until you hit "Export Private Key". Select "Yes, export the private key".
*   Continue through the stages until you land on "Security". Tick "Password" and enter an appropriate password.
*   Enter a valid file name and location in the next screen, and then finish the wizard.
*   You have successfully saved your Xledger certificate to a file. You will now need to convert it to a valid format that Cyclr can use.

#### Converting Certificate

*   If you are using a Windows system:
    * You will need to install OpenSSL.
    * Once installed, open a new Powershell window in the folder that contains the certificate. Type ``openssl.exe pkcs12 -in xledger-cert.pfx -out xledger-cert.pem -nodes`` replacing ``xledger-cert.pfx`` with the name of the created certificate from the previous step.
*   If you are using a Linux system:
    * You may already have OpenSSL installed, depending on your distribution. Type ``openssl version`` into a terminal to see if you have it installed.
    * Once installed/verified, type ``openssl pkcs12 -in xledger-cert.pfx -out xledger-cert.pem -nodes`` replacing ``xledger-cert.pfx`` with the name of the created certificate from the previous step.
*   Open the newly created ``xledger-cert.pem`` into a text editor of your liking. Copy all the text displayed. 

### Cyclr Setup

Setup your Xledger App within Cyclr:

*   Go to your **Cyclr Console**
*   Click the **Connectors** menu along the top
*   Choose Connector Library
*   Scroll down to **Xledger**
*   Click the **Setup** button

Enter the following values:

**User Name**: The username of your Xledger account.

**Password**:  The password of your Xledger account.

**Client Certificate**: This is the certificate that you copied down in the last step of the "Converging Certificate" instructions above.


Your Xledger Connector is now setup! You can test it by installing it in one of your Cyclr accounts and executing one of the methods to confirm it can return some data.
