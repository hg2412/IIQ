# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 01:35:59 2016

@author: Haoxiang
"""
import csv
import random
import os
import NewsSearch as NS

def clean_company_name(s):
    s = s.replace(",", "")
    s = s.replace("'", "")
    return s.strip()
    
def read_company_list(filename):
    comp_list = []
    with open(filename,'rU') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"', dialect=csv.excel_tab)
        for row in reader:
            comp_list.append(clean_company_name(row[0]))
    return comp_list
    

def get_random_sample(comp_list, size  = 30):
    randIndex = random.sample(range(len(comp_list)), size)
    result = [comp_list[i] for i in randIndex]
    return result
    
def write_as_csv(outputname, result):
    with open(outputname, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = ['Company', 'URL', 'Title', 'Description', 'Date'])
        writer.writeheader()
        for r in result:
            writer.writerow(dict((k, v.encode('utf-8')) for k, v in r.iteritems()))
    print outputname + " writed."

if __name__ == "__main__":
    comp_list = read_company_list("Top300 Patent Companies.csv")
    sample = get_random_sample(comp_list, 30)
    dir_name = 'Sample News Stories'
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
    for comp in sample:
        response = NS.search_news([comp])[0]['value']
        result = []
        for r in response:
            data ={}
            data['Company'] = comp
            data['URL'] = r['url']
            data['Title'] = r['name']
            data['Description'] = r['description']
            data['Date'] = r['datePublished']
    
            result.append(data)
        write_as_csv(dir_name + '/' + comp + '.csv', result)
    
                

    
    



        
        
    