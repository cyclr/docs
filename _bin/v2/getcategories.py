# windows cli : python getcategories.py
# submit request to Cyclr categories API
# parse response, build md file for each catgory
# requires https://github.com/un33k/python-slugify

import requests
import re
import os
import json
from slugify import slugify

response = requests.get('https://my.cyclr.com/api/categories')
if response.status_code == 200 :
	json_data = response.json()

	template_md = os.path.join(os.path.dirname(__file__), './assets/templatecategory.md')
	template_yml = os.path.join(os.path.dirname(__file__), './assets/templatecategory.yml')
	# print(__file__)
	# print(template_md)
	# parse each category in the response array
	for item in json_data:
		# derive the category filenames 
		category_name = item
		category_slug = slugify(item)
		file_name = re.sub("[^a-zA-Z0-9]", "", category_name).lower()
		file_name = re.sub("[^a-zA-Z0-9]", "", category_name).lower()
		file_name_slug = category_slug
		# file_md = '../../pages/v2/04-application-connector-guides/'+file_name+'.md'
		file_md = '../../pages/v2/04-application-connector-guides/'+file_name_slug+'.md'
		file_md_full = os.path.join(os.path.dirname(__file__), file_md)
		# file_yml = '../../_data/v2/categories/'+file_name+'.yml'
		file_yml = '../../_data/v2/categories/'+file_name_slug+'.yml'
		file_yml_full = os.path.join(os.path.dirname(__file__), file_yml)
		# print("Write md "+file_md_full)
		# inject the category strings into the md template
		# open the template file and the new file
		with open(template_md,'r') as fromfile, open(file_md_full,'a') as tofile:
			for line in fromfile:
				# omit description from front matter if no value
				if "categoryname" in line:
					newline = re.sub("categoryname", category_name, line)
				elif "categoryslug" in line:
					newline = re.sub("categoryslug", category_slug, line)
				else:
					newline = line
				# append to new md
				tofile.write(newline)
		tofile.close();

		with open(template_yml,'r') as fromfile, open(file_yml_full,'a') as tofile:
			for line in fromfile:
				if "categoryname" in line:
					newline = re.sub("categoryname", category_name, line)
				else:
					newline = line
				# append to new md
				tofile.write(newline)
		tofile.close();
