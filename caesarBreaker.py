#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This is an attempt to break
    Caeser's Cipher"""
import sys

def isNew(ch):
    freqLen = len(freq);
    for i in range(0, freqLen):
        if(freq[i][0] == ch):
            return i;
    return -1





def join(ch):
    l = isNew(ch);
    if(l==-1):
        freq.append([ch, 1]);
    
    else:
        freq[l][1]+=1;
        
        


def frequency(s):
    l = len(s)
    for i in range(0, l):
        ch = ord(s[i]);
        join(ch);
    from operator import itemgetter
    freq.sort(key=itemgetter(1), reverse = True)
    




#This portion performs rotation, based on the input condition decides the mod value. See checkCase.
def rotate(iChar, rot, con):
    pVal = ord(iChar);
    if(con == 0):
        val = chr((((pVal - 48) + rot) % 10) + 48);
    elif(con == 1):
        val = chr((((pVal - 65) + rot) % 26) + 65);
    elif(con == 2):
        val = chr((((pVal - 97) + rot) % 26) + 97);
    else:
        val = chr(pVal + rot);
    return val;







#The plaintext has a possibility of having 4 types of character values. Based on which the 
#Program to checkCase function categorizes them into:
#>> 0: Number (48 - 57)
#>> 1: UPERCASE (65 - 90)
#>> 2: lowercase (97 - 122)
#>> 3: SPECIAL!@#$%^&*() (EVERYTHING ELSE, LITERALLY)

def checkCase(iChar):
    val = ord(iChar);
    if(val >=48 and val <=57): #Number
        cas = 0;
        
    elif(val>=65 and val <=90): #CAPS
        cas = 1;
        
    elif(val>=97 and val <=122): #low
        cas = 2;
        
    else: #SPECIAL!@#$%^&*()_+-=
        cas = 3;
        
    return cas;



def caesar(plaintext, rot):
    l = len(plaintext);
    retS=""
    for i in range(0, l):
        con = checkCase(plaintext[i]);
        cc = rotate(plaintext[i], rot, con);
        retS = retS+cc;
    
    return retS;



ip  = sys.argv[1];
op = sys.argv[2];
cipherText = open(ip, 'r');
plainText = open(op, 'w');
x = cipherText.read();
freq =[];
frequency(x);
key = -(freq[1][0] -ord('e'));
plain = caesar(x, key);
x2 = plainText.write(plain);
plainText.close();
cipherText.close();
    


