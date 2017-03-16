# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 22:51:07 2017

@author: HP 15 AB032TX
"""

Questions=['what','who','where','how','when','whom','why']

Table=[]


Q=raw_input().split()
G={}
G['faculty']=['faculty','teacher','tutor']
G['attendance']=['presence','turnout','attendance','debarred']


G['subject']=['network','dsa']
G['building']=['sjt','tt','gdn','mb','smv','cdmm']
G['hostel']=['block','hostel']
Extras=['best','worst','top 5','top 3','top 10']
Subjects=[]
Hostel=['a','b','m','d','e','f','g','h','j','p','n','l','k']

def generalise(Q):
    for word in range(len(Q)):
    	for key in G.keys():
    		if Q[word] in G[key]:
    			if key=='subject':
	    			Subjects.append(Q[word])
	    		Q[word]=key

def hasHostel(Q):
	out=True
	for word in Q:
		
		if word=='hostel':
			out=True
			Table.append('hostel')
			break
	
	if out:
		for word in Q:
			if word in Hostel:
				
				return word
		
		return 'nothing'
	return False
				
def hasQuestion(Q):
    for i in Q:
        if i in Questions:
            return i
    return False        

             
            
    return Subjects

def hasattendance(Q): 
    for word in Q:
        if word in G['attendance']:
        	Table.append('attendance')
        	return True
    
        	
    return False
def hasFaculty(Q):
    out=False
    for word in Q:
        if word in G['faculty']:
            out= True
            break
    if out:
    	Table.append('faculty')
    return out
            
def extraKeys(Q):
	for word in Q:
		if word in Extras:
			return word

	return ''		

query=['Show ']
fQuery=['SELECT ']
generalise(Q)
Asked=0
if hasattendance(Q):
	query.append('attendance of')
	fQuery.append('attendance')
	Asked+=1

if hasFaculty(Q):
	query.append(extraKeys(Q))
	query.append('faculty of')
	fQuery.append('faculty')
	Asked+=1
if len(hasHostel(Q))!=7:
	fQuery.append('hostel')
	query.append('hostel ')
	query.append(hasHostel(Q))
	
fQuery.append('FROM')
Table=list(set(Table))
fQuery+=Table
if hasFaculty(Q) or hasattendance(Q):
	fQuery.append('WHERE SUBJECT =')
	fQuery+=Subjects
elif len(hasHostel(Q))!=7:
	fQuery.append('WHERE HOSTEL =')	


	fQuery+=hasHostel(Q)
query.append(' and '.join(Subjects))            
if Asked>1:
	print 'Ask One thing at a time'
else:	
	print ' '.join(query)
	print ' '.join(fQuery)
	

	
