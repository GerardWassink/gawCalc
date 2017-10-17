#!/usr/bin/python

# ------------------------------------------------------------------------
# Program		:	gawCalc.py
# Author		:	Gerard Wassink
# Date			:	October 2017
#
# Function		:	Polish notation Calculator
#
# ------------------------------------------------------------------------
# 						GNU LICENSE CONDITIONS
# ------------------------------------------------------------------------
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
# ------------------------------------------------------------------------
#				Copyright (C) 2017 Gerard Wassink
# ------------------------------------------------------------------------

from gawterm import term				# screen class
import commands							# system commands
import math								# mathematical functions
import time								# time handling

# ------------------------------------------------------------------------
# 				Create Stack class
# ------------------------------------------------------------------------

class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)
         t.msgPrint(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)

     def gimme(self,ptr):
     	return(self.items[ptr])


# ------------------------------------------------------------------------
# 				Show the status
# ------------------------------------------------------------------------

def showStatus():
	t.staClear()
	if anglesDegrees:
		t.staPrint("DEG")
	else:
		t.staPrint("RAD")

# ------------------------------------------------------------------------
# 				Show the content of the stack
# ------------------------------------------------------------------------

def showStack():
	t.msgClear()
	if stack.size() > 0:
		for i in range(0, stack.size()):
			t.msgPrint(stack.gimme(i))


# ------------------------------------------------------------------------
# 				Show help information
# ------------------------------------------------------------------------

def showHelp():
	t.cmdPrint("HELP information")
	t.cmdPrint(" ")
	t.cmdPrint("Commands")
	t.cmdPrint(" ")
	t.cmdPrint("POP             : Remove top entry from stack")
	t.cmdPrint("SWAP            : Switch top two entries from stack")
	t.cmdPrint("DEG, RAD        : Mode switch Degrees - Radians")
	t.cmdPrint(" ")
	t.cmdPrint("^, *, /, +, -   : Calculus functions, work")
	t.cmdPrint("                     on top two entries of stack")
	t.cmdPrint("INV             : inverse (1/X) of top stack entry")
	t.cmdPrint(" ")
	t.cmdPrint("SIN, COS, TAN,  : Goniometric functions, work ")
	t.cmdPrint("ASIN, ACOS, ATAN     on top entry of stack")
	t.cmdPrint(" ")
	t.cmdPrint("EXP             : e ^ top stack entry")
	t.cmdPrint("FAC             : Factorial of top stack entry")
	t.cmdPrint("LN              : Natural log (base e) of top stack entry")
	t.cmdPrint("LOG             : Log (base 10) of top stack entry")
	t.cmdPrint("SQR             : Square root of top stack entry")
	t.cmdPrint(" ")
	t.cmdPrint("PI, E           : Constants")
	t.cmdPrint(" ")


# ------------------------------------------------------------------------
# 				Check whether a string is a number
# ------------------------------------------------------------------------

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
        

# ------------------------------------------------------------------------
#													Variables
# ------------------------------------------------------------------------

t = term("Status", "Commands", "Stack")	# Instantiate terminal screen object
stack = Stack()							# Instantiate stack object

ClientID = commands.getoutput("whoami")	# Get user name

anglesDegrees = True					# Are we in Degrees mode?


# ------------------------------------------------------------------------
#													Start executable code
# ------------------------------------------------------------------------

t.cmdPrint("                    _____     __   ")
t.cmdPrint("  ___ ____ __    __/ ___/__ _/ /___")
t.cmdPrint(" / _ `/ _ `/ |/|/ / /__/ _ `/ / __/")
t.cmdPrint(" \\_, /\\_,_/|__,__/\\___/\\_,_/_/\\__/ ")
t.cmdPrint("/___/                              ")
t.cmdPrint("")
t.cmdPrint("Hi " + ClientID + " - started gawCalc program for you")
t.cmdPrint("--- type '?' if you would like help")
t.cmdPrint(" ")


showStack()
showStatus()

go_on = True
while go_on:
	reply = t.inpRead().upper()
	t.cmdPrint(reply)
	replies = reply.split(" ")

	for repl in replies:

		#
		# === Push numbers
		#
		if is_number(repl):				### If it's a number, push it 
			stack.push(repl)

		#
		# === Housekeeping
		#
		elif repl in [ "EXIT", "X", "QUIT", "Q"]:	### Quit program?
			go_on = False
			break

		elif repl in [ "HELP", "H", "?"]:	### Help request?
			showHelp()

		elif repl == "POP":			### Remove top stack entry
			a = stack.pop()

		elif repl == "SWAP":		### Swap top two stack entries
			a = stack.pop()
			b = stack.pop()
			stack.push(a)
			stack.push(b)
			
		elif repl == "RAD":				### Change mode to radians
			anglesDegrees = False

		elif repl == "DEG":				### Change mode to degrees
			anglesDegrees = True

		#
		# === Calculus functions
		#
		elif repl == "^":				### Raise to the power
			if stack.size() > 1:
				r = float(stack.pop())
				stack.push(str(math.pow(float(stack.pop()), r)))
			else:
				t.cmdPrint("To few entries on stack to do "+repl)

		elif repl == "*":				### Multiply
			if stack.size() > 1:
				r = float(stack.pop())
				stack.push(str(float(stack.pop()) * r))
			else:
				t.cmdPrint("To few entries on stack to do "+repl)

		elif repl == "/":				### Divide
			if stack.size() > 1:
				r = float(stack.pop())
				stack.push(str(float(stack.pop()) / r))
			else:
				t.cmdPrint("To few entries on stack to do "+repl)

		elif repl == "+":				### Addition
			if stack.size() > 1:
				r = float(stack.pop())
				stack.push(str(float(stack.pop()) + r))
			else:
				t.cmdPrint("To few entries on stack to do "+repl)

		elif repl == "-":				### Subtraction
			if stack.size() > 1:
				r = float(stack.pop())
				stack.push(str(float(stack.pop()) - r))
			else:
				t.cmdPrint("To few entries on stack to do "+repl)

		elif repl == "INV":				### Calulate inverse (1/x)
			stack.push(str(1 / float(stack.pop())))

		#
		# === Entering constants
		#
		elif repl == "PI":				### Push pi onto stack
			stack.push(str(math.pi))

		elif repl == "E":				### Push e onto stack
			stack.push(str(math.e))

		#
		# === Trigonometric functions
		#
		elif repl == "SIN":				### Calculate sine of angle on stack
			if stack.size() > 0:
				r = float(stack.pop())
				if anglesDegrees:
					stack.push(str(math.sin(math.radians(r))))
				else:
					stack.push(str(math.sin(r)))
			else:
				t.cmdPrint("To few entries on stack to do "+repl)

		elif repl == "COS":				### Calculate cosine of angle on stack
			if stack.size() > 0:
				r = float(stack.pop())
				if anglesDegrees:
					stack.push(str(math.cos(math.radians(r))))
				else:
					stack.push(str(math.cos(r)))
			else:
				t.cmdPrint("To few entries on stack to do "+repl)

		elif repl == "TAN":				### Calculate tangent of angle on stack
			if stack.size() > 0:
				r = float(stack.pop())
				if anglesDegrees:
					stack.push(str(math.tan(math.radians(r))))
				else:
					stack.push(str(math.tan(r)))
			else:
				t.cmdPrint("To few entries on stack to do "+repl)

		elif repl == "ASIN":			### Calculate arc sine of angle on stack
			if stack.size() > 0:
				r = float(stack.pop())
				if anglesDegrees:
					stack.push(str(math.degrees(math.asin(r))))
				else:
					stack.push(str(math.asin(r)))
			else:
				t.cmdPrint("To few entries on stack to do "+repl)

		elif repl == "ACOS":			### Calculate arc cosine of angle on stack
			if stack.size() > 0:
				r = float(stack.pop())
				if anglesDegrees:
					stack.push(str(math.degrees(math.acos(r))))
				else:
					stack.push(str(math.acos(r)))
			else:
				t.cmdPrint("To few entries on stack to do "+repl)

		elif repl == "ATAN":			### Calculate arc tangent of angle on stack
			if stack.size() > 0:
				r = float(stack.pop())
				if anglesDegrees:
					stack.push(str(math.degrees(math.atan(r))))
				else:
					stack.push(str(math.atan(r)))
			else:
				t.cmdPrint("To few entries on stack to do "+repl)

		#
		# === Mathematical functions
		#
		elif repl == "FAC":			### Calculate factorial of value on stack
			stack.push(str(math.factorial(float(stack.pop()))))

		elif repl == "SQR":			### Calculate square root of value on stack
			stack.push(str(math.sqrt(float(stack.pop()))))

		elif repl == "EXP":			### Calculate e^x of value on stack
			stack.push(str(math.exp(float(stack.pop()))))

		elif repl == "LN":			### Calculate natural log of value on stack
			stack.push(str(math.log(float(stack.pop()))))

		elif repl == "LOG":			### Calculate log base 10 of value on stack
			stack.push(str(math.log10(float(stack.pop()))))

		#
		# === Fall through
		#
		else:
			t.cmdPrint("Don't know how to handle "+repl)

		showStack()
		showStatus()

t.Close()

print "gawCalc program stopped, goodbye " + ClientID

exit()
