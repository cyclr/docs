# windows cli : python refactorconnectorguides.py
# 
# parses pages/v2/05-application-connectors/authentication
# writes additional information to pages/v2/05-application-connectors/infomration
#   adjusts front matter variables title, permalink
#   skips all content prior to the title 
# writes new authentication file without the additional information
import os
import argparse
import re
import json



parser = argparse.ArgumentParser(description='Refactor connector guides to separate authentication and other informmation')
parser.add_argument("-c", "--json", help="Create md files for all v1 files in [jsonfile].json")
args = parser.parse_args()


authfolder = './pages/05-application-connectors/authentication'
infofolder = './pages/05-application-connectors/information'
authfolderfull = os.path.join(os.path.dirname(__file__), authfolder)
infofolderfull = os.path.join(os.path.dirname(__file__), infofolder)
# regex string for headings
regexHeadingInformtion = "^#[\s]"


ext = ('.md')
for authfile in os.listdir(authfolderfull):
    if authfile.endswith(ext):
        authfilefull = authfolderfull+"/"+authfile
        infofile = os.path.basename(authfile).split('.')[0]+"-information.md"
        infofilefill = infofolderfull+"/"+infofile
        print("Split "+authfilefull+" to create "+infofilefill)
        # open authfile
        with open(authfilefull,'r') as sourcefile:
            sourcelines = [sourceline for sourceline in sourefile]
        sourcefile.close()
        frontmatter = False
        frontmattercomplete = False
        authcontent = False
        infocontent = False
        with open(infofilefill,'w',encoding='utf-8') as toinfofile:
            for line in sourcelines:
                if frontmattercomplete == True:
                    if authcontent == True:
                        # check if line contains the Additional Information heading
                        # if not, write to the auth file
                        # if yes, authcontent = False infocontent = True, close authfile
                    if infocontent == True
                        # write to infofile
                elif frontmatter == True;
                    # adjust front matter
                    #   title
                    #   permalink 
                elif line.startswith("---") and frontmatter == False:
                    frontmatter = True
                    newline = line
                    toinfofile.write(newline)
                elif line.startswith("---") and frontmatter == True:
                    frontmattercomplete = True
                    authcontent = True
                    newline = line
                    toinfofile.write(newline)
        toinfofile.close
        # create infofile
        # load authfile lines
        # close authfile
        # foreach line 
        #   parse - front matter / auth content  / info content
        # write front matter lines to auth, info 
        #   adjust auth front matter , replace title, permalink
        #   write auth content lines to auth file
        #   write info content lines to info file
        # close authfile
        # close infofile

    else:
        continue