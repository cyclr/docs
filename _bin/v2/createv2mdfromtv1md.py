# windows cli : python createv2mdfromtv1md.py
# 
# creates pages/v2 md files from pages/v1 md files, using json array of md file objects to provide list of files for copy, with front matter for menus 
#
# adds front matter for jekyll-menus, and writes all content after front matter to the target file
#
import os
#import glob
import argparse
#from pickle import FALSE
import re
import json
#import array as arr


parser = argparse.ArgumentParser(description='Create v2 md files from v1 md files')
parser.add_argument("-c", "--json", help="Create md files for all v1 files in [jsonfile].json")
args = parser.parse_args()


sourcefolder = '../../pages/v1/'
targetfolder = '../../pages/v2/'
sourcefolderfull = os.path.join(os.path.dirname(__file__), sourcefolder)
targetfolderfull = os.path.join(os.path.dirname(__file__), targetfolder)
templatemdfile = os.path.join(os.path.dirname(__file__), './assets/templatefrontmattermenus.md')
templateindexfile = os.path.join(os.path.dirname(__file__), './assets/templateindex.md')
# temp content for category pages
targethubfolder = '../../_data/v2/categoriesnew/'
targethubfolderfull = os.path.join(os.path.dirname(__file__), targethubfolder)
# regex string for headings
regexh1 = "^#[\s]"
regexh2 = "^##[\s]"
regexeol = "[\s]#{1,}$"
regextable = "^\|"
regexcodefencebad = "^\u0060{4}"
regexcodefencehttp = "^\u0060{3}http"
codefence = "\u0060\u0060\u0060"
codefencehtml = "\u0060\u0060\u0060html"
tableclass = "{: .table .mt-2 .mb-5 }\n"


with open(templatemdfile,'r') as menufile:
    menulines = [menuline for menuline in menufile]
menufile.close()

with open(templateindexfile,'r') as indexfile:
    indexlines = [indexline for indexline in indexfile]
indexfile.close()

# get json file
jsonfilename = '../../_data/import/v1md.json'
if args.json is not None:
    jsonfilename = args.jsonfile+'.json'

jsonfilename_full = os.path.join(os.path.dirname(__file__), jsonfilename)


# open and read json file
with open(jsonfilename_full, 'r') as jsonfile:
    json_data = json.load(jsonfile)
    targethubymlfile = ''
    newhubfile = True
    pagewithsections = False
    for item in json_data:
        if item['v1md'] is None:
            continue
        elif item['v1md'] == 'index':
            pagewithsections = False
            # add folder if required
            if item['v2folder'] is not None:
                targetmdfolder = item['v2folder']
                targetmdfolderfull = os.path.join(os.path.dirname(__file__), targetfolder, targetmdfolder)
                if os.path.exists(targetmdfolderfull) == False:
                    os.mkdir(targetmdfolderfull)  
                # create the index.md, there are no source files for this
                if item['v2md'] == 'index':
                    targetmdfile = item['v2md']+".md"
                    targetmdfilefull = os.path.join(os.path.dirname(__file__), targetfolder, targetmdfolder, targetmdfile)
                    # print("index.md "+targetmdfilefull)
                    with open(targetmdfilefull,'w',encoding='utf-8') as toindexfile:
                        for indexline in indexlines:
                            addline = True
                            if "indexmenuname" in indexline:
	                            newline = re.sub("indexmenuname", item['menuname'], indexline)
                            elif "indexpermalink" in indexline:
                                newline = re.sub("indexpermalink", item['permalink'], indexline)
                            elif "indextags" in indexline:
                                newline = re.sub("indextags", item['permalink'], indexline)
                            elif "indextitle" in indexline:
                                newline = re.sub("indextitle", item['menutitle'], indexline)
                                # print("index.md title: "+newline)
                            elif "indexmenutitle" in indexline:
                                newline = re.sub("indexmenutitle", item['menutitle'], indexline)
                            elif "indexmenuidentifier" in indexline:
                                newline = re.sub("indexmenuidentifier", item['menuidentifier'], indexline)
                            elif "indexmenuicon" in indexline:
                                if item['menuicon'] is None:
                                    addline = False
                                else:
                                    newline = re.sub("indexmenuicon", item['menuicon'], indexline)
                            elif "indexmenutoggleonly" in indexline:
                                if item['menutoggleonly'] is None:
                                    addline = False
                                else:
                                    newline = re.sub("indexmenutoggleonly", item['menutoggleonly'], indexline)
                            elif "indexmenuweight" in indexline:
                                if item['menuweight'] is None:
                                    addline = False
                                else:
                                    newline = re.sub("indexmenuweight", str(item['menuweight']), indexline)
                            else:
                                newline = indexline
                            if addline == True:
                                toindexfile.write(newline)
                        toindexfile.close()
                    # add the target hub yml file
                    targethubymlfile=item['permalink']+".yml"
                    targetmdfilefull = os.path.join(os.path.dirname(__file__), targethubfolderfull, targethubymlfile)
                    if os.path.exists(targetmdfolderfull) == True:
                        with open(targetmdfilefull,'w',encoding='utf-8') as tohubfile:
                            tohubfile.write("title: "+item['menutitle']);
                            tohubfile.write("\ntext: Placeholder content for category page");
                            tohubfile.write("\nsections:\n");
                        tohubfile.close()
        elif item['v2folder'] is None:
            continue
        else:
            pagewithsections = True
            sourcemdfolder = item['v1folder']
            sourcemdfile = item['v1md']+".md"
            sourcefilefull = sourcefolderfull+sourcemdfolder+"/"+sourcemdfile
            targetmdfolder = item['v2folder']
            targetmdfolderfull = os.path.join(os.path.dirname(__file__), targetfolder, targetmdfolder)
            targetmdfile = item['v2md']+".md"
            targetmdfilefull = os.path.join(os.path.dirname(__file__), targetfolder, targetmdfolder, targetmdfile)
            # open files for current json item
            # print(sourcemdfile+" source for "+targetmdfile+"\n")
            if os.path.exists(targetmdfolderfull) == False:
                # print("mkdir "+targetmdfolderfull)
                os.mkdir(targetmdfolderfull)  
            # check source file exists
            if os.path.exists(sourcefilefull) == True:
                # print("Port "+sourcemdfolder+"/"+sourcemdfile+" to "+targetmdfolder+"/"+targetmdfile)
                with open(sourcefilefull,'r',encoding='utf-8') as fromfile, open(targetmdfilefull,'w',encoding='utf-8') as tofile:
                    frontmatter = False
                    frontmattercomplete = False
                    iscontent = False
                    # prevlinetable = False
                    # flags to determine HTML containers for the page content
                    firstcontentline = True
                    for line in fromfile:
                        if frontmattercomplete == True:
                            mdline = line
                            # add the html parse option
                            if firstcontentline == True and len(line.strip()) == 0:
                                # prevlinetable = False
                                continue
                            elif firstcontentline == True:
                                firstcontentline = False
                                tofile.write('{::options parse_block_html="true" /}')
                                tofile.write('\n<section class="card py-5 my-5">\n')
                            elif firstcontentline == False:
                                if bool(re.search(regexh1, line)) == True or bool(re.search(regexh2, line)) == True:
                                    tofile.write('\n</section>')
                                    tofile.write('\n<section class="card py-5 my-5">\n')
                                if bool(re.search(regexh1, line)) == True:
                                    mdline = re.sub("^#[\s]","## ",line)
                                    if (item['permalink']) is not None:
                                        print(item['permalink'] +" h1 line: "+line+" > "+mdline)
                                    else:
                                        print(" h1 line: "+line+" > "+mdline)
                            if bool(re.search(regexcodefencebad, mdline)) == True:
                                mdline = re.sub(regexcodefencebad,codefence,mdline)
                            mdline = re.sub(regexcodefencehttp,codefencehtml,mdline)
                            newline = re.sub(regexeol, "", mdline)
                            tofile.write(newline)
                        elif line.startswith("---") and frontmatter == False:
                            frontmatter = True
                            newline = line
                            tofile.write(newline)
                        elif line.startswith("---") and frontmatter == True:
                            # frontmatter menus
                            # clone the assets/frontmattermenu.md, substitute item values from json
                            if item['menuname'] is not None:                        
                                for menuline in menulines:
                                    addline = True
                                    if "menuname" in menuline:
	                                    newline = re.sub("menuname", item['menuname'], menuline)
                                    elif "menutitle" in menuline:
                                        newline = re.sub("menutitle", item['menutitle'], menuline)
                                    elif "menuidentifier" in menuline:
                                        newline = re.sub("menuidentifier", item['menuidentifier'], menuline)
                                    elif "menuicon" in menuline:
                                        if item['menuicon'] is None:
                                            addline = False
                                        else:
                                            newline = re.sub("menuicon", item['menuicon'], menuline)
                                    elif "menutoggleonly" in menuline:
                                        if item['menutoggleonly'] is None:
                                            addline = False
                                        else:
                                            newline = re.sub("menutoggleonly", item['menutoggleonly'], menuline)
                                    elif "menuweight" in menuline:
                                        if item['menuweight'] is None:
                                            addline = False
                                        else:
                                            newline = re.sub("menuweight", str(item['menuweight']), menuline)
                                    else:
                                        newline = menuline
                                    if addline == True:
                                        tofile.write(newline)
                            frontmattercomplete = True
                            frontmatter = False
                            newline = line
                            tofile.write(newline)
                        elif frontmatter == True and frontmattercomplete == False:
                            newline = line
                            tofile.write(newline)
                    if pagewithsections == True:
                        tofile.write('\n</section>\n')
                # close files 
                fromfile.close()
                tofile.close()


