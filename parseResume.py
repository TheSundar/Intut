import os

from docreader import document_to_text
from skills import Ui_MainWindow

import re


def get_email(content):
    match = re.search(r'[\w\.-]+@[\w\.-]+', content)
    return match.group(0)


def get_phone(content):
    match = re.findall("(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})", content)
    return match

def skills_sets(content):
    skill_list = []
    skillSet = ['C/C++', 'Python', 'Java', 'C#', 'SML', 'JavaScript', 'HTML/CSS', 'Latex', 'Python', 'Javascript', 'HTML/CSS', 'SML', 'C', \
                'PHP', 'Arduino', 'Max 7', 'Pascal', 'BASIC', 'Java', 'C', 'SML.', 'Adobe CS5','MS Office','Eclipse','LaTeX','Cantonese', 'Mandarin',\
                'Microsoft Office', 'Excel','PowerPoint','Revit', 'Maya', 'AutoCAD 2D/3D', 'Architectural Desktop','Form-Z 3D', 'Rhinoceros 3D','MicroStation 2D/3D',\
                'Photoshop','InDesign','HTML','Adobe','SEO strategy & analysis','Assembly','Matlab','Simulink','DSP','Sublime Text','ADA']

    skillSet1= ['AutoCAD','CAD','Adobe','4th,Dimension/4D','ABAP','ABC','ActionScript','Ada','Agilent,VEE','Algol','Alice','Angelscript','Apex',\
                'APL','AppleScript','Arduino','ASP','AspectJ','Assembly','ATLAS','Augeas','AutoHotkey','AutoIt',\
                'AutoLISP','Automator','Awk','Bash','(Visual),Basic','bc','BCPL','BETA','BlitzMax','Bourne,Shell',\
                'Bro','C','C,Shell','C#','C++','C++/CLI','C-Omega','Caml','Ceylon','CFML','CHILL','CIL','CL,(OS/400)',\
                'Clarion','Clean','Clipper','Clojure','CLU','COBOL','Cobra','CoffeeScript','ColdFusion','COMAL','Common,Lisp',\
                'Coq','cT','Curl','Dart','DCL','DCPU-16,ASM','Delphi/Object,Pascal','DiBOL','Dylan','Ecl','ECMAScript',\
                'EGL','Eiffel','Elixir','Emacs,Lisp','Erlang','Etoys','Euphoria','EXEC','F#','Factor','Falcon','Fancy','Fantom','Felix',\
                'Forth','Fortran','Fortress','(Visual),FoxPro','Gambas','GNU,Octave','Google,AppsScript','Gosu','Groovy','Haskell',\
                'haXe','Heron','HPL','HyperTalk','Icon','IDL','Informix-4GL','INTERCAL','Io','Ioke','J#','JADE','Java',\
                'Java,FX,Script','JavaScript','JScript','JScript.NET','Julia','Korn,Shell','Kotlin','LabVIEW','Ladder,Logic','Lasso',\
                'Limbo','Lingo','Lisp','Logo','Logtalk','LotusScript','LPC','Lua','Lustre','M4','MAD','Magic','Magik','Malbolge',\
                'MANTIS','Maple','Mathematica','MATLAB','Matlab','Max/MSP','MAXScript','MEL','Mercury','Mirah','Miva','Monkey',\
                'Modula-2','Modula-3','MOO','Moto','MS-DOS,Batch','MUMPS','NATURAL','Nemerle','Nimrod','NQC','NSIS','Nu','NXT-G',\
                'Oberon','Object Rexx','Objective-C','Objective-J','OCaml','Occam','ooc','Opa','OpenCL','OpenEdge,ABL','OPL','Oz',\
                'Paradox','Parrot','Pascal','PASCAL','Perl','PHP','Pike','PILOT','PL/I','PL/SQL','Pliant','PostScript','POV-Ray','PowerBasic',\
                'PowerScript','PowerShell','Prolog','Puppet','Pure,Data','Python','Racket','REALBasic','REBOL',\
                'Revolution','REXX','RPG,(OS/400)','Ruby','Rust','S-PLUS','SAS','Sather','Scala','Scheme','Scilab','Scratch',\
                'Seed7','Shell','SIGNAL','Simula','Simulink','Slate','Smalltalk','Smarty','SPARK','SPSS','SQR','Squeak','Squirrel',\
                'Standard,ML','Suneido','SuperCollider','TACL','Tcl','Tex','thinBasic','TOM','Transact-SQL','Turing','TypeScript','Vala/Genie',\
                'VBScript','Verilog','VHDL','VimL','Visual,Basic,.NET','WebDNA','Whitespace','X10','xBase','XBase++','Xen','XPL','XSLT','XQuery',\
                'yacc','Yorick','Z,shell','HTML','CSS','SML','Photoshop','Microsoft Office','PowerPoint','Power Point','Excel','Patran','Abaqus','Django',\
                'JQuery','IOS','Android','wxPython','XML','SQL','PostgreSQL','SQLite','Oracle','Mysql','PyQT','Angular JS',\
                'Rest','NMR','MALDI','DSP','ARM','Cantonese','Mandarin','Microsoft Word','Embedded C','PCB']
    # print content.replace("\n"," ")

    match = re.findall(r"\s*[\w]*[/]*[\w]*\s*", content.replace("\n"," "))

    for text in match:
        if text.strip() in skillSet1:
            skill_list.append(text.strip())

    for i in set(skillSet1):
        if i in content:      # i in content: may not work for ['C#' in 'SMC# 1234,500'],   'Matlab' == 'MATLAB', 'C++' == 'C ++', 'C' matches to all 'C...'
            print i,          # 'PASCAL' == 'Pascal',

    # match = re.findall(r"\s*[\w\s]*[,]\s*", content)
    # print "match--",match

    return set(skill_list)

for i in os.listdir(r'H:\Resumes\\'):
    try:
        print '\n file name--->',i
        content = document_to_text(i,r'H:\Resumes\\'+i)
        if content:
            with open(i+'_text.txt','w') as resumefile:
                resumefile.write(content)

        # if i == 'sample7.pdf':
        #     print content.split(" ")
            # print str(content.replace('  ','')).splitlines()[0:3]
        # print get_email(content)
        # print get_phone(content)
        # print "skiils->",
        # skills_sets(content)

    except:
        import sys
        print sys.exc_info()
        pass
        # print 'problem with file : ',i