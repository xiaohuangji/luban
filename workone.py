import parse
import search

output = open('/Users/renren/study/utfwww.txt', 'w')
def writeToFile(work):
	for str in work:
		output.write(str)
		
def workone(work):
	wid=work[1].replace('\r\n','')
	line= search.getResult(wid) 
	work[3] = parse.parseApplicants(line)+"\r\n"
	work[5] = parse.parseInventors(line)+"\r\n"
	work[7] = parse.parseTitle(line)+"\r\n"
	work[9]= parse.parseAbstract(line)+"\r\n"
	writeToFile(work)

