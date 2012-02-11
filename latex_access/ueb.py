# ueb.py
#    A part of the latex-access project at http://latex-access.sourceforge.net/
#    Author: Daniel Dalton <daniel.dalton10@gmail.com>
#    Copyright (C) 2011 Daniel Dalton/latex-access Contributors
#
#    This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation;
#    either version 2 of the License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
#    See the GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License along with this program; if not, visit <http://www.gnu.org/licenses>
#
'''Module to provide UEB translations for the latex_access
module.'''


import latex_access
from latex_access import get_arg
from latex_access import get_optional_arg

class ueb(latex_access.translator):
    '''Class for ueb translations.'''

    def __init__(self):
        latex_access.translator.__init__(self)
        self.files.append("ueb.table")
        self.load_files()
        new_table={"$":self.uebDollar,
                   "\\dot":("","`"),"\\ddot":("","``"),
                   "^":self.super,"_":self.sub,"\\sqrt":self.sqrt,"\\frac":self.frac,
                   "\\tag":self.tag,"\\mathbf":("_",""),"\\mathbb":("_",""),"\\colvec":("{"," ","o"),"\\tcolvec":("{"," "," ","o"),"\\bar":self.bar,"\\hat":self.bar,"\\overline":self.bar,".":self.dot,",":self.comma}

# Ueb upper numbers follow start from j abc...i as j = 0 a = b =2 etc.
        self.upperNumbers=('j','a','b','c','d','e','f','g','h','i')

        for number in range (0,9): # add the numbers
            new_table[str(number)]=self.numbers

        for letter in range (65,91): # Ascii upper case
            new_table ["%c" % (letter)] = self.upperLetter

        for letter in range (97,122): # Ascii, lower case
            new_table["%c" % (letter)] = self.lowerLetter
    
        for (k,v) in new_table.iteritems():
            self.table[k]=v

    def super(self,input,start):
        '''Translate  superscripts into UEB.

        Returns a touple with translated string and index of
        first char after end of super.'''
        short = False
        arg=get_arg(input,start)
        if '@brl@' in arg[0]:
            trans = arg[0].replace("@brl@","").replace("@/brl@","")
            if trans[0] == '#' and trans[1].isdigit () and len(trans) ==2:
                short = True
        if len(arg[0]) <=1 or short:
            translation = ";9" + self.translate(arg[0])
        else:
            translation = ";9\"<" + self.translate(arg[0])+"\">"
        return (translation,arg[1])

    def sub(self,input,start):
        '''Translates ueb subscripts.

        Returns a touple, as above'''
        short = False 
        arg=get_arg(input,start)
        if '@brl@' in arg[0]:
            trans = arg[0].replace("@brl@","").replace("@/brl@","")
            if trans[0] == '#' and trans[1].isdigit () and len(trans) ==2:
                short = True
        if len(arg[0]) <=1 or short:
            translation = ";5"+self.translate(arg[0])
        else:
            translation = ";5\"<"+self.translate(arg[0]) + "\">"
        return (translation,arg[1])

    def sqrt(self,input,start):
        '''Translatesroots in latex.

        Returns a touple as above.'''
        arg=get_optional_arg(input,start)
        if arg:
            translation=";;%9"+self.translate(arg[0])
            arg=get_arg(input,arg[1])
            translation+=self.translate(arg[0])+"+"
        else:
            arg=get_arg(input,start)
            translation="%"+self.translate(arg[0])+"+"
        return (translation,arg[1])

    def frac(self,input,start):
        '''Translates fractions into ueb.

        Returns touple as above'''
        numerator=get_arg(input,start)
        denominator=get_arg(input,numerator[1])

        if str(numerator[0]).replace('#','').replace('@brl@','').replace('@/brl@','').isdigit() and str(denominator[0]).replace('#', '').replace('@brl@','').replace('@/brl@','').isdigit():
            translation=numerator[0]+"/"+denominator[0]
        else: # complex fraction 
            translation = ";("+self.translate(numerator[0])+"./"+self.translate(denominator[0])+";)"
        return (translation, denominator[1])


    def bar(self, input, start):
        '''Handles bar/overline.

        Returns toutple'''
        arg=get_arg(input,start)
        if len(arg[0])==1:
            translation=":%s" % arg[0]
        else:
            translation=":{%so" % self.translate(arg[0])
        return (translation,arg[1])

    def tag(self,input,start):
        '''Translate  tags into Nemeth.

        Returns a touple with translated string and index of
        first char after end of tag.'''
        arg=get_arg(input,start)
        translation = ' "<'+arg[0]+'">'
        return (translation, arg[1])

    def uebDollar (self, input, start):
        """Handle dollars.

        This function uses the self.dollars method to check if dollars
    should be removed and if not change the dollar to ueb, `s."""
        translation=self.dollar(input,start)
        if translation[0]:
            translationout="`s"
        else:
            translationout = ''
        translation=(translationout, translation[1])
        return translation
    
    def numbers(self,input,start):
        '''Translates numbers in latex.

        Returns a touple as above.'''
        numberstart = start-1 # since it's not a latex command we are interested in the current char 
        if self.lastnumber >= 0 and numberstart == self.lastnumber:
            translation = "" # inside a number no hash "#" sign necessary 
        else:
            translation = '#'
        numberstart+=1
        translation += self.upperNumbers[int(input[start-1])] # and get the upper number eg. 3 = c
        self.lastnumber = numberstart # Record where last number is 
        return (translation, numberstart)
    
    def dot (self, input, start):
        '''Translates dots (.) in latex.

        Returns a touple as above.'''
        if self.lastnumber >= 0 and start-1 == self.lastnumber:
            self.lastnumber = start
        translation='4'
        return (translation, start)
    
    def comma (self, input, start):
        '''Translates commas (,) in latex.

        Returns a touple as above.'''
        if self.lastnumber >= 0 and start-1 == self.lastnumber:
            self.lastnumber = start
        translation='1'
        return (translation, start)

    def letterSign (self,input,start):
        '''Determines whether the letter sign is necessary. 

        Returns a boolean.'''
        lettersign = False # no lettersign yet
# Last character was part of a number and letters are within range a-j 
        if self.lastnumber >= 0 and start == self.lastnumber and input[start].lower() in 'abcdefghij':
            lettersign = True

        try: # white space on either side of sing char 
            if start > 0 and input[start-1] == ' ' and input[start+1] == ' ':
                lettersign = True
        except:
            pass
        try: # char on it's own at beginning of line 
            if start == 0 and input[start+1] == ' ':
                lettersign = True
        except:
            pass
        try: # char on it's own at end of line 
            if input[start-1] == ' ' and start+1 == len(input):
                lettersign = True
        except:
            pass
        try: # some punctuation after a letter eg. A.
            if input[start+1] in '.,':
                lettersign = True
        except:
            pass

        if start > 1 and input[start-2:start-1].isupper () and input[start].islower (): # capital letters and now we are a lower case 
            lettersign= True 
        if len (input) == 1: # char by itself on line
            lettersign = True
        return lettersign 

    def lowerLetter (self,input,start):
        '''Translates lower case letters in latex.

        Returns a touple as above.'''
        start=start-1 # We are manipulating current char
        if self.letterSign(input,start): # add the letter sign 
          translation = ';'
        else:
            translation = ''
        translation += input[start]
        return (translation,start+1)

    def upperLetter (self, input, start):
        '''Translates upper case letters in latex.

        Returns a touple as above.'''
        start=start-1 # We are focused on current char 
        translation= "" # The brf translation 
        cap = True # Provide a capital sign unless special case (below)
        doublecap = False # Do we represent consecutive capital letters by ,,
        lettersign = self.letterSign (input,start) # Do we provide a lettersign (;)
        try: # Letter before wasn't a cap, but letter after is so start consecutive capitals (,,)
            if input[start+1].isupper () and not input[start-1].isupper ():
                doublecap = True
                cap = False # And no need for single , 
        except:
            pass
        try: # Handle double Cap on start of line 
            if start == 0 and input[start+1].isupper ():
                doublecap = True
                cap = False # No single cap necessary 
        except:
            pass
        try: # the double ,, has already been provided for this set of consecutive capital letters 
            if start > 0 and input[start-1].isupper ():
                cap = False
                doublecap =False
        except:
            pass
        if start == 0: # Handle cap at start of line 
            cap = True
        if lettersign: # Add a lettersign first 
            translation+= ';'
        if doublecap: # we add double capital sign 
            translation += ',,'
        elif cap: # Otherwise just add single cap sign 
            translation += ','
        translation+=input[start].lower () # Now add the lowercase equivilant to avoid dot 7 in some tables 
        return (translation, start+1)
    