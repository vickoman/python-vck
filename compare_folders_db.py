#!/usr/bin/env python
import sys
import glob, os
import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","testuser","test123","TESTDB" )