---
title: Miva authentication
sidebar: cyclr_sidebar
permalink: miva-information
tags: [connector]
linkedpage: true
---
{::options parse_block_html="true" /}
<section class="card">
  
## Additional information

### Generate a HMAC for step script

All Miva API requests require you to send a HMAC signature with every request. The connector automatically generates a HMAC signature before every request and uses the request body as part of the encoding when when it generates the signature.

If you use step script with a `before_action` function to modify the body of a request, the function causes a mismatch between the generated HMAC signature and the request body. To avoid the problem, you need to manually regenerate the HMAC signature. In this case, you need to add a `RegenerateHmacSignature()` call before the final `return true`. For example:

```javascript
function before_action() {
    if (method_request != null && method_request.fields == null) {
	method_request.fields = ['id', 'first_name', 'last_name'];
    }
	
    RegenerateHmacSignature(); /* Regenerate HMAC signature. */
    return true;
}
```

</section>