<section>
    <div>
      <p>{{ connectordata.Description }}</p>
    </div>
</section>


{% if connectordata.Authentication %}
<section>
## Authentication
<table>
  <tbody>
	{% for prop in connectordata.Authentication %}
    <tr>
      <td>{{ prop[0] }}</td><td>{{ prop[1] | raw }}</td>
    </tr>
	{% endfor %}
  </tbody>
</table> 
</section>
{% endif %}

{% if connectordata.Documentation %}
	{% for section in connectordata.Documentation %}
<section>
## {{ section.Title }}
<div>
	{{ section.Content | raw }}
</div>
</section>
	{% endfor %}
{% endif %}



## Categories
<ul>
{% for category in connectordata.Categories %}
	<li>{{ category }}</li>
{% endfor %}
</ul>

## API Methods
<div class="no_toc_section">
	<div class="accordion accordion-flush no_toc_section" id="accordionFlushMethods">
	{% for category in connectordata.MethodCategories %}
		<div class="accordion-item">
				### {{ category.Category }}
		    <h3 class="accordion-header" id="flush-heading{{category.Category | slugify}}">
				<button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#flush-collapse{{category.Category | slugify}}" aria-expanded="false" aria-controls="flush-collapse{{category.Category | slugify}}">
				{{ category.Category }}
				</button>
		    </h3>
		    <div id="flush-collapse{{category.Category | slugify}}" class="accordion-collapse collapse" aria-labelledby="flush-heading{{category.Category | slugify}}" data-bs-parent="#accordionFlushMethods">
				<div class="accordion-body">
				{% for method in category.Methods %}
					#### {{ method.MethodType }} : {{ method.Name }}
					<p>{{ method.Description }}</p>
				{% endfor %}
				</div>
		    </div>
	  	</div>
	{% endfor %}
	</div>
</div>