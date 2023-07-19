---
title: Libraries
sidebar: cyclr_sidebar
permalink: libraries
tags: [templates]

menus:
    scripting:
        title: Libraries
        identifier: libraries
        toggleonly: menutoggleonly
        weight: 6                                                                                  
---
{::options parse_block_html="true" /}
<section class="card">

The following libraries are available within Cyclr’s script engine:

**Note:** These libraries are ready to use in script, so you don’t need to load them with a `require` call.

| **Library name** | **Description** | **External documentation** |
|---|---|---|
| `moment` |  Parse, validate, manipulate, and display dates and times in JavaScript. Cyclr also supports the Moment Timezone extension, which enables formatting and converting of dates in any timezone. | [Moment documentation](https://momentjs.com/).<br>[Moment Timezone documentation](https://momentjs.com/timezone/). |
| `crypto-js` | JavaScript library of crypto standards.<br>**Warning**: The output of encrypted data is always in a hex string. The library doesn’t support formatting options such as `CryptoJS.enc` when you call `toString`. | [CryptoJS documentation](https://github.com/brix/crypto-js). |

</section>
<section class="card">

