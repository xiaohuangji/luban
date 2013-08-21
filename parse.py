import re


#rfile=open("/Users/renren/study/r.html")
#for line in rfile:
#   print line
    
    
def parseTitle(line):     
    title='' 
    pattern = re.compile(r'(.*)(bookmark</th>.*?\([AB]\d{1,2}\))(.+?)(</a>)')
    match = pattern.match(line)
    if match:
        title=match.group(3)
    return trimTitle(title)

def parseAbstract(line):
    abstract=''
    pattern = re.compile(r'(.*)(class="printAbstract">)(.+?)(</p>)')
    match = pattern.match(line)
    if match:
        abstract=match.group(3)
    return abstract

def parseInventors(line):
    inventors=''
    pattern = re.compile(r'(.*)(Inventor\(s\).*?printTableText">)(.+?)(<a)')
    match = pattern.match(line)
    if match:
        inventors=match.group(3)
    return trimInventors(inventors)

def parseApplicants(line):
    applicants=''
    pattern = re.compile(r'(.*)(Applicant\(s\).*?hidden">)(.+?)</span>')
    match = pattern.match(line)
    if match:
        applicants=match.group(3)
    return trimApplicants(applicants)

def trimTitle(title):
    pattern = re.compile(r'(\W*)(.+)')
    match = pattern.match(title)
    rtitle=''
    if match:
        rtitle=match.group(2)
    return rtitle.capitalize()

def trimInventors(inventors):
    inventors=inventors.strip('\t ').split(';')
    country = re.compile('\[.{2}\]')
    rinventors=''
    for inventor in inventors:
        inventor = inventor.title().strip('\t ')
        inventor=country.sub('',inventor).strip()
        alphs=inventor.split(' ')
        for alph in alphs:
            if (len(alph)==1):
                inventor=inventor.replace(' '+alph,' '+alph+".")
        rinventors=rinventors+inventor+","
    return rinventors.rstrip(',')
    
def trimApplicants(app):
    app = app.strip('\t() ').split(';')
    rapp=''
    for a in app:
        a=a.title().replace(',','');
        a=a.replace('Llc ','LLC ').replace('Inc ','Inc. ').replace('Corp ','Corp. ')
        a=a.replace('Gmbh ','GmbH ').replace('Ag ','AG ').replace('Co. Ltd ','Co.,Ltd. ')
        a=a.replace('Ltd ','Ltd. ').replace('Plc ','PLC ').replace('Aps ','APS ')
        a=a.replace('Co. Kg ','Co.KG ')
        a=a.strip();
        rapp=rapp+a+";"
    return rapp.rstrip(';')


