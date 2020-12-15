import re
import PyPDF2 as p
import os
import pandas as pd
 
#/content/5thsem_2019.pdf
os.chdir('C:\shubham\data')
res =p.PdfFileReader('5_sem_2019.pdf', 'utf-8')
res.documentInfo
total_page = res.getNumPages()
print('total number of pages  : ' , total_page)
 
studata = {'name':[] , 'roll_number':[] ,'subject_1':[]  , 'sub_count': [] ,  'SGPA' : [] ,'pass_fail' : [] , 'CGPA' : []}
 
for i in range(total_page): 
    page_text =res.getPage(i).extractText()
    page_content = res.getPage(i).getContents() 
    wrong_symbol = [' »' , '» ' ,'»' ,'#' ,'501','#501','502', '503','504' , '505']     # subject code of interest( required semester)
    # cleaning of data 
    for bad in wrong_symbol:
        page_text = page_text.replace(bad , '@@')
        page = page_text.split('    ')                             # Designed for 4 space split of data
        print(page)
        
    for wrd in page:
        
        roll_number = re.findall('\d\d\d\d\d''C03''\d\d\d', wrd)
        
        x=page.index(wrd) + 1
        #name = refindall()
 
        #print('================================================')
        #print(len(roll_number))
        #print(roll_number)
        #print('================================================')
        if len(roll_number) >= 1:
            #print('============================+++++++++++++++++++++++++++++++++++++++++++++++++====================')
            #print(page[x])
            
            namlist = re.findall('[A-Z]+\s[A-Z]+|[A-Z]+[0-9]', page[x])
            pointers = re.findall('\d[.]\d' , page[x])
            sub_1 = re.findall('[A-Z][@]{2}|[A-Z][@]{4}|[A-Z][+#][@]{2}|[A-Z][+#][@]{4}' , page[x])
            pass_failed = re.findall('FAIL|PASS WITH GRACE|PASS' , page[x])
            grade_list =[]
            for grade in sub_1:
                grade_extract = grade.split('@')
                grade_list.append(grade_extract[0])
                
            
            
            nam = namlist[0]
            #print(nam)
            studata['roll_number'].append(roll_number[0])
            studata['sub_count'].append(len(grade_list))
            studata['name'].append(nam)
            studata['subject_1'].append(grade_list)
            studata['SGPA'].append(pointers[0])
            studata['CGPA'].append(pointers[1])
            studata['pass_fail'].append(pass_failed)
        
print('Total number of student. ===' , len(studata['name']))
print('list of students in Electrical Engineering')
print(studata['name'])
print(studata['roll_number'])

student_result = pd.DataFrame.from_dict(studata)

student_result.to_excel(r'C:\shubham\data\result_analysis.xlsx', index = False)

#sample =res.getPage(26).extractText()
