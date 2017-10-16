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

#
# === Create Stack class
#
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

#
# === Show the content of the stack
#
def showStatus():
	t.staClear()
	if anglesDegrees:
		t.staPrint("DEG")
	else:
		t.staPrint("RAD")

#
# === Show the content of the stack
#
def showStack():
	t.msgClear()
	if stack.size() > 0:
		for i in range(0, stack.size()):
			t.msgPrint(stack.gimme(i))

#
# === Show help information
#
def showHelp():
	t.cmdPrint("HELP information")
	t.cmdPrint(" ")
	t.cmdPrint("Commands")
	t.cmdPrint(" ")
	t.cmdPrint("^, *, /, +, -   : Arithmetic functions, work")
	t.cmdPrint("                     on top two entries of stack")
	t.cmdPrint(" ")
	t.cmdPrint("SIN, COS, TAN,  : Goniometric functions, work ")
	t.cmdPrint("ASIN, ACOS, ATAN     on top entry of stack")
	t.cmdPrint(" ")
	t.cmdPrint("PI, E           : Constants")
	t.cmdPrint(" ")
	t.cmdPrint("DEG, RAD        : Mode switch Degrees - Radians")
	t.cmdPrint(" ")
	t.cmdPrint("POP             : Remove top entry from stack")
	t.cmdPrint("SWAP            : Switch top two entries from stack")
	t.cmdPrint(" ")

#
# === check whether a string is a number
#
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
        
#
# === Variables
#
anglesDegrees = True					# Are we in Degrees mode?

# ------------------------------------------------------------------------
#													Start executable code
# ------------------------------------------------------------------------


#
# === Instantiate terminal screen object
#
t = term("Status", "Commands", "Stack")

ClientID = commands.getoutput("whoami")

t.cmdPrint("Hi " + ClientID + " - started gawCalc program for you")
t.cmdPrint("--- type '?' if you would like help")
t.cmdPrint(" ")

stack = Stack()

showStack()
showStatus()

go_on = True
while go_on:
	reply = t.inpRead().upper()
	t.cmdPrint(reply)
	replies = reply.split(" ")

	for repl in replies:

		if repl in [ "EXIT", "X", "QUIT", "Q"]:
			go_on = False
			break

		elif repl in [ "HELP", "H", "?"]:
			showHelp()

		elif is_number(repl):
			stack.push(repl)

		elif repl == "^":
			if stack.size() > 1:
				r = float(stack.pop())
				stack.push(str(math.pow(float(stack.pop()), r)))
			else:
				t.staPrint("To few entries on stack to do "+repl)

		elif repl == "*":
			if stack.size() > 1:
				r = float(stack.pop())
				stack.push(str(float(stack.pop()) * r))
			else:
				t.staPrint("To few entries on stack to do "+repl)

		elif repl == "/":
			if stack.size() > 1:
				r = float(stack.pop())
				stack.push(str(float(stack.pop()) / r))
			else:
				t.staPrint("To few entries on stack to do "+repl)

		elif repl == "+":
			if stack.size() > 1:
				r = float(stack.pop())
				stack.push(str(float(stack.pop()) + r))
			else:
				t.staPrint("To few entries on stack to do "+repl)

		elif repl == "-":
			if stack.size() > 1:
				r = float(stack.pop())
				stack.push(str(float(stack.pop()) - r))
			else:
				t.staPrint("To few entries on stack to do "+repl)

		elif repl == "RAD":
			anglesDegrees = False

		elif repl == "DEG":
			anglesDegrees = True

		elif repl == "PI":
			stack.push(str(math.pi))

		elif repl == "E":
			stack.push(str(math.e))

		elif repl == "SIN":
			if stack.size() > 0:
				r = float(stack.pop())
				if anglesDegrees:
					stack.push(str(math.sin(math.radians(r))))
				else:
					stack.push(str(math.sin(r)))
			else:
				t.cmdPrint("To few entries on stack to do "+repl)

		elif repl == "COS":
			if stack.size() > 0:
				r = float(stack.pop())
				if anglesDegrees:
					stack.push(str(math.cos(math.radians(r))))
				else:
					stack.push(str(math.cos(r)))
			else:
				t.cmdPrint("To few entries on stack to do "+repl)

		elif repl == "TAN":
			if stack.size() > 0:
				r = float(stack.pop())
				if anglesDegrees:
					stack.push(str(math.tan(math.radians(r))))
				else:
					stack.push(str(math.tan(r)))
			else:
				t.cmdPrint("To few entries on stack to do "+repl)

		elif repl == "ASIN":
			if stack.size() > 0:
				r = float(stack.pop())
				if anglesDegrees:
					stack.push(str(math.degrees(math.asin(r))))
				else:
					stack.push(str(math.asin(r)))
			else:
				t.cmdPrint("To few entries on stack to do "+repl)

		elif repl == "ACOS":
			if stack.size() > 0:
				r = float(stack.pop())
				if anglesDegrees:
					stack.push(str(math.degrees(math.acos(r))))
				else:
					stack.push(str(math.acos(r)))
			else:
				t.cmdPrint("To few entries on stack to do "+repl)

		elif repl == "ATAN":
			if stack.size() > 0:
				r = float(stack.pop())
				if anglesDegrees:
					stack.push(str(math.degrees(math.atan(r))))
				else:
					stack.push(str(math.atan(r)))
			else:
				t.cmdPrint("To few entries on stack to do "+repl)

		elif repl == "POP":
			a = stack.pop()

		elif repl == "SWAP":
			a = stack.pop()
			b = stack.pop()
			stack.push(a)
			stack.push(b)

		showStack()
		showStatus()

t.Close()

print "gawCalc program stopped, goodbye " + ClientID

exit()
