# to do:
# Add API request parameter to for single connector 
# Add flags to restrict to md or json
# Add flag to overwrite existing md and json or write new files only
# Add temp section to append placeholder json until fields added and populated in the connectors db/API response
# Confirm naming conventions
# Confirm permalinks
# windows cli 
# help : python getconnectorscontent.py --help
# for single connector : python getconnectorscontent.py --connectorid 99999
# for all connectors: python getconnectorscontent.py


# https://pypi.org/project/python-slugify/
# add slugify replacements for ampersand?

import argparse
import requests
import re
import os
import json
import array as arr
from slugify import slugify

parser = argparse.ArgumentParser(description='Get connector content')
parser.add_argument("-c", "--connectorid", help="Get connector for given ID",type=int)
args = parser.parse_args()
json_data = []
response = False

if args.connectorid is not None:
	connectorsapiurl = 'https://my.cyclr.com/api/connectors/'+str(args.connectorid)
	response = requests.get(connectorsapiurl)
else:
	response = requests.get('https://my.cyclr.com/api/connectors?pageSize=1000&details=true')

if response.status_code == 200 :
	if args.connectorid is not None:
		json_data = [response.json()]
	else:
		json_data = response.json()

	template_md = os.path.join(os.path.dirname(__file__), './assets/templateconnector.md')
	# print(__file__)
	# print(template_md)
	# connector content summary
	file_summary_json = "../../_data/v2/admin/connector-content-summary.json"
	file_summary_json_full = os.path.join(os.path.dirname(__file__), file_summary_json)
	# dict lists which connectors do and don't have v1 content
	connector_content_dict = {
	"v1content":{},
	"nocontent":{} 
	}
	# parse each connector in the response array
	for item in json_data:
		# derive the connector filenames 
		connector_name = item['Name']
		connector_slug = slugify(connector_name)
		connector_icon = item['Icon']
		connector_description = item['Description']
		connector_category = 'All'
		connector_categories = ",".join(item['Categories'])
		# file_name = re.sub("[^a-zA-Z0-9]", "", connector_name).lower()
		file_name = connector_slug
		file_md = '../../pages/v2/connectors/connector-'+file_name+'.md'
		file_md_full = os.path.join(os.path.dirname(__file__), file_md)
		file_json = "../../_data/v2/connectors/connector-"+file_name+".json"
		file_json_full = os.path.join(os.path.dirname(__file__), file_json)
		# v1 md file - check if to be included, set front matter flag if md exists
		contentv1_file = '../../_includes/v2/connector/v1content/'+file_name+'.md'
		contentv1_file_full = os.path.join(os.path.dirname(__file__), contentv1_file)
		contentv1exists = os.path.exists(contentv1_file_full)
		# print("Write md "+file_md_full+" and json "+file_json_full)
		if type(item['Categories']) is list and item['Categories']:
			connector_category = item['Categories'][0]
		# inject the connector name into the md template
		# open the template file and the new file
		with open(template_md,'r') as fromfile, open(file_md_full,'w') as tofile:
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
						# add this connector to the v1content array
						connector_content_dict["v1content"][connector_name] = connector_slug
					else:
						newline = re.sub("connectorcontentv1", "false", line)
						# add this connetor to the nocontent array
						connector_content_dict["nocontent"][connector_name] = connector_slug
				else:
					newline = line
				# write to new md
				tofile.write(newline), 
			tofile.close()
			fromfile.close()

		# write the connector content summary to the json file

		json_content = json.dumps(connector_content_dict)
		with open(file_summary_json_full, "w") as filesummaryjson:
			filesummaryjson.write(json_content)
			filesummaryjson.close()


		# write the connector object to the json file
		json_string = json.dumps(item, indent=4)
		with open(file_json_full, "w") as filejson:
			filejson.write(json_string)
			filejson.close()