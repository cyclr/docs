# 
# windows cli : python connectorcontentsummary.py

import requests
import re
import os
import json
from slugify import slugify

response = requests.get('https://my.cyclr.com/api/connectors?pageSize=1000&details=true')
if response.status_code == 200 :
	json_data = response.json()
	summary_file_name = connector_slug
	file_data = '../../pages/v2/connectors/connector-content-summary-.md'
	file_md_full = os.path.join(os.path.dirname(__file__), file_md)
	# parse each connector in the response array
	for item in json_data:
		# derive the connector filenames 
		connector_name = item['Name']
		connector_slug = slugify(connector_name)
		connector_icon = item['Icon']
		connector_description = item['Description']
		connector_category = 'All'
		connector_categories = ",".join(item['Categories'])
		file_name = connector_slug
		file_md = '../../pages/v2/connectors/connector-'+file_name+'.md'
		file_md_full = os.path.join(os.path.dirname(__file__), file_md)
		# v1 md file - check if to be included, set front matter flag if md exists
		contentv1_file = '../../_includes/v2/connector/v1content/'+file_name+'.md'
		contentv1_file_full = os.path.join(os.path.dirname(__file__), contentv1_file)
		contentv1exists = os.path.exists(contentv1_file_full)
		# print("Write md "+file_md_full+" and json "+file_json_full)
		if type(item['Categories']) is list and item['Categories']:
			connector_category = item['Categories'][0]
		# inject the connector name into the md template
		# open the template file and the new file
		with open(template_md,'r') as fromfile, open(file_md_full,'a') as tofile:
			for line in fromfile:
				# omit description from front matter if no value
				if "connectordescription" in line and connector_description is None:
					continue					
				elif "connectordescription" in line:
					newline = re.sub("connectordescription", connector_description, line)
				elif "connectortitle" in line:
					newline = re.sub("connectortitle", connector_name, line)
				elif "connectoricon" in line:
					newline = re.sub("connectoricon", connector_icon, line)
				elif "connectorcategory" in line:
					newline = re.sub("connectorcategory", connector_category, line)
				elif "connectorcategories" in line:
					newline = re.sub("connectorcategories", "["+connector_categories+"]", line)
				elif "connectorname" in line:
					newline = re.sub("connectorname", file_name, line)
				elif "connectorcontentv1" in line:
					# set the v1 content flag if the relevant md exists
					if contentv1exists == True:
						newline = re.sub("connectorcontentv1", "true", line)
					else:
						newline = re.sub("connectorcontentv1", "false", line)
				else:
					newline = line
				# append to new md
				tofile.write(newline)
