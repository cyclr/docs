---
title: Google Ads - Workspace Authentication
sidebar: cyclr_sidebar
permalink: google-calendar-workspace-connector
tags: [connector]
---

## Account Level Setup

#### Google Authentication

Follow the instructions in our [Google Authentication](https://github.com/cyclr/docs/blob/master/pages/connector-authentication/google-authentication.md) guide.

#### Select or create a Google Ads manager account

From Google Ads Documentation [Google Ads](https://developers.google.com/google-ads/api/docs/first-call/dev-token)

Step 1: You must have a [Google Ads manager account](https://support.google.com/google-ads/answer/7459399) to apply for access to the API.

Manager accounts cannot be created using the same email address as an existing Google Ads account. You must therefore use an email address that hasn't already been associated with a Google Ads account to create your manager account.

Step 2: Apply for access to the Google Ads API
Sign up for Google Ads API access through your manager account. [Sign in](https://ads.google.com/home/tools/manager-accounts/), then navigate to TOOLS & SETTINGS > SETUP > API Center. The API Center option appears only for Google Ads manager accounts.

All fields on the API Access form must be completed, and the Terms and Conditions accepted. Make sure your information is correct and your company's website URL is functioning. If the website is not a live page, we won't be able to process your application.

Make sure the API contact email you provide leads to a regularly monitored inbox. If we cannot contact you at this email address, we won't be able to process your application, and it will be rejected.

You can edit your API contact email in the API Center.

We strongly encourage you to keep this information up-to-date, even after the application process, so we can send you important service announcements.

Step 3: Continue your application
To ensure the tool or software app you propose to use with the Google Ads API is in compliance with our Terms and Conditions and Policies, including Required Minimum Functionality (RMF) (if applicable), click the Apply for Basic Access link in the API Center, and complete the Google Ads API Token Application form.

## Token review team has approved my developer token

Your assigned developer token will be activated once your application for API access is approved. Your token will be available through your API Center—accessible through the Account settings menu for the manager account from which you applied. You'll be able to access the API by including it in your request headers when interacting with our system.

To retrieve your developer token, sign in to your manager account. You must be signed-in to a Google Ads manager account before continuing.

Navigate to TOOLS & SETTINGS > SETUP > API Center. This option appears only for Google Ads manager accounts.

If your developer token is pending approval, you can start developing immediately with the pending token you received during signup, using a test manager account.

Your pending developer token must be approved before using it with production Google Ads accounts.

## Link accounts to your manager accounts

From Google Documentation [Google Documentation](https://support.google.com/google-ads/answer/7459601?hl=en-GB)
To use your manager account, you can begin by linking it to existing individual or manager accounts.

You also have the option of creating new Google Ads accounts from your manager account. These accounts are automatically linked to your manager account.

Before you start
This article shows you how to link existing accounts to your manager account. You may want to begin by reading About linking accounts to manager accounts.

Instructions

- Sign in to your Google Ads manager account.
- From the page menu on the left, click Settings, then click Sub-account settings at the top of the page.
- Click the plus button .
- Click Link existing account.
- Enter the Google Ads account's Customer ID number. To link multiple accounts at once, enter one customer ID per line.
- Click Send invitation.
- Users with access to the Google Ads account you sent a link request to will receive account alerts and emails inviting them to link to your account.

Users with administrative access to the invited account, or access to a linked manager account that has administrative ownership of that account, can accept your invitation by going to the 'Account access' section of the Google Ads account.

During this process, you'll see a pending notification for the (soon-to-be) client account in your manager account's 'Pending invitations'. Learn more about managing invitations. Once the invited account accepts your invitation, you'll receive an email confirmation and the account will automatically be linked to your manager account.
