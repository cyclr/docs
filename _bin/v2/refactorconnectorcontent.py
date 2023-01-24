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


parser = argparse.ArgumentParser(description='Refactor connector guides to separate authentication and other informmation')
parser.add_argument("-c", "--json", help="Create md files for all v1 files in [jsonfile].json")
args = parser.parse_args()

authfolder = '../../pages/v2/05-application-connectors/authentication'
authfoldernew = './pages/05-application-connectors/authentication'
infofoldernew = './pages/05-application-connectors/information'
authfolderfull = os.path.join(os.path.dirname(__file__), authfolder)
authfoldernewfull = os.path.join(os.path.dirname(__file__), authfoldernew)
infofoldernewfull = os.path.join(os.path.dirname(__file__), infofoldernew)
kramdownoption = '{::options parse_block_html="true" /}'
regexh2 = "^##[\s]Additional information"
ext = ('.md')
for authfile in os.listdir(authfolderfull):
    if authfile.endswith(ext):
        authfilefull = authfolderfull+"/"+authfile
        authfilenewfull = authfoldernewfull+"/"+authfile
        infofile = os.path.basename(authfile).split('.')[0]+"-information.md"
        infofilefull = infofoldernewfull+"/"+infofile
        # open authfile
        with open(authfilefull,'r', encoding='utf-8') as sourcefile:
            sourcelines = [sourceline for sourceline in sourcefile]
        sourcefile.close()
        with open(infofilefull,'w',encoding='utf-8') as toinfofile, open(authfilenewfull,'w',encoding='utf-8') as toauthfile:
            frontmatter = False
            frontmattercomplete = False
            firstauthline = True
            firstcontentline = False
            authcontent = False
            infocontent = False
            for line in sourcelines:
                if frontmattercomplete == True:
                    if authcontent == True:
                        # check if line contains the Additional Information heading
                        # if not, write to the auth file
                        # if yes, authcontent = False infocontent = True, close authfile
                        if bool(re.search(regexh2, line, re.IGNORECASE)) == True:
                            print(authfilefull+" GOT info heading "+line)
                            authcontent = False
                            infocontent = True
                            toinfofile.write(prevline)
                        else:
                            if firstauthline == False:
                                toauthfile.write(prevline)
                            firstauthline = False
                    elif infocontent == True:
                        # write to infofile
                        if firstcontentline == False:
                            print("\t\tINFO :"+infofilefull)
                            firstcontentline = True
                        toinfofile.write(prevline)
                elif line.startswith("---") and frontmatter == False:
                    frontmatter = True
                    newline = line
                    toauthfile.write(newline)
                    toinfofile.write(newline)
                elif line.startswith("---") and frontmatter == True:
                    frontmattercomplete = True
                    authcontent = True
                    infocontent = False
                    newline = line
                    toauthfile.write(newline)
                    toinfofile.write(newline)
                    toinfofile.write(kramdownoption+"\n")
                elif frontmatter == True:
                    newline = line
                    toauthfile.write(newline)
                    # adjust front matter for info file
                    if "title:" in line:
                        newline = re.sub("Authentication", "Information", line)
                    elif "permalink:" in line:
                        newline = re.sub("-connector", "-information" , line)
                    toinfofile.write(newline)
                prevline = line
            if authcontent == True:
                toauthfile.write(prevline)
            elif infocontent == True:
                toinfofile.write(prevline)
            toauthfile.close()
            toinfofile.close()
    else:
        continue
