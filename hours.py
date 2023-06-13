# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def add_hours(d1, d2):
    hm1 = d1.split("h")
    h1 = int(hm1[0])
    m1 = int(hm1[1])
    
    hm2 = d2.split("h")
    h2 = int(hm2[0])
    m2 = int(hm2[1])
    
    x = m1+m2
    new_m = x%60
    if new_m < 10:
        new_m = "0" +str(new_m)
    else:
        new_m = str(new_m)
    
    new_h = str(h1+h2+(x//60))
    
    res = new_h + 'h' + new_m
    
    return res

#print(add_hours("1h36","2h34"))

def main():
    hours = ["7h45","8h25","6h00"] # à remplir sur ce format hours = ["1h30","2h54"]
    
    res = "0h0"
    for h in hours:
        res = add_hours(res,h)
        
    print(res)
    
main()