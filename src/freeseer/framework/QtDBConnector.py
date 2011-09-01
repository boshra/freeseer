#!/usr/bin/python
# -*- coding: utf-8 -*-

# freeseer - vga/presentation capture software
#
#  Copyright (C) 2011  Free and Open Source Software Learning Centre
#  http://fosslc.org
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.

# For support, questions, suggestions or any other inquiries, visit:
# http://wiki.github.com/fosslc/freeseer/

import os

from PyQt4 import QtSql

class QtDBConnector():
    presentationsModel = None
    
    def __init__(self, configdir, talkdb_file="presentations.db"):
        self.configdir = configdir
        self.talkdb_file = os.path.abspath("%s/%s" % (self.configdir, talkdb_file))
        
        if not os.path.isfile(self.talkdb_file):
            file = open(self.talkdb_file, 'w')
            file.write('')
            file.close()
        
        self.__open_table()
    
    def __open_table(self):
        self.talkdb = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        self.talkdb.setDatabaseName(self.talkdb_file)
        
        if (self.talkdb.open()):
            
            # check if presentations table exists and if not create it.
            if not self.talkdb.tables().contains("presentations"):
                self.__create_table()
                self.__insert_default_talk()
            
        else:
            print "Unable to create talkdb file."
            
    def __close_table(self):
        self.talkdb.close()
            
    def __create_table(self):
        """
        Creates the presentations table in the database. Should be used to
        initialize a new table.
        """
        query = QtSql.QSqlQuery('''CREATE TABLE IF NOT EXISTS presentations
                                       (Id INTEGER PRIMARY KEY,
                                        Speaker varchar(100),
                                        Title varchar(255) UNIQUE,
                                        Description text,
                                        Level varchar(25),
                                        Event varchar(100),
                                        Room varchar(25)),
                                        Time timestamp''')
        
    def __insert_default_talk(self):
        """
        Insert the default talk data into the database.
        """
        query = QtSql.QSqlQuery('''INSERT INTO presentations VALUES
                                (NULL,
                                 "Thanh Ha",
                                 "Intro to Freeseer",
                                 "",
                                 "",
                                 "SC2011",
                                 "",
                                 "T105")''')
        
    def get_talks(self):
        """
        Gets all the talks from the database including all columns.
        """
        result = QtSql.QSqlQuery('''SELECT * FROM presentations''')
        return result
    
    #
    # Data Model Retrieval 
    #
    def get_presentations_model(self):
        """
        Gets the Presentation Table Model.
        Useful for Qt GUI based Frontends to load the Model in Table Views.
        """
        if self.presentationsModel is None:
            self.presentationsModel = QtSql.QSqlTableModel()
            self.presentationsModel.setTable("presentations")
            self.presentationsModel.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
            self.presentationsModel.select()
        
        return self.presentationsModel
    
    def get_events_model(self):
        """
        Gets the Events Model.
        Useful for Qt GUI based Frontends to load the Model into Views.
        """
        self.eventsModel = QtSql.QSqlQueryModel()
        self.eventsModel.setQuery("SELECT DISTINCT Event FROM presentations")
            
        return self.eventsModel
    
    def get_rooms_model(self, event):
        """
        Gets the Rooms Model.
        Useful for Qt GUI based Frontends to load the Model into Views.
        """
        self.roomsModel = QtSql.QSqlQueryModel()
        self.roomsModel.setQuery("SELECT DISTINCT Room FROM presentations WHERE Event='%s' ORDER BY TIME ASC" % event)
            
        return self.roomsModel
    
    def get_talks_model(self, event, room):
        """
        Gets the Talks Model. A talk is defined as "<presenter> - <talk_title>"
        Useful for Qt GUI based Frontends to load the Model into Views.
        """
        self.talksModel = QtSql.QSqlQueryModel()
        self.talksModel.setQuery("SELECT (Speaker || ' - ' || Title) FROM presentations \
                                   WHERE Event='%s' and Room='%s' ORDER BY Time ASC" % (event, room))
            
        return self.talksModel
    
"""
Test code to independently test the methods in the QtDBConnector() class.    
"""    
if __name__ == "__main__":
    
    # Imports
    import sys
    import tempfile
    
    from PyQt4 import QtCore
    
    # Main
    app = QtCore.QCoreApplication(sys.argv)
    
    tmpdir = tempfile.gettempdir()
    print "Temp Directory: %s" % tmpdir # prints the current temporary directory
    
    testdbcon = QtDBConnector(os.path.abspath(tmpdir))
    
    print "Talks: "
    result = testdbcon.get_talks()
    while(result.next()):
        id = result.value(0).toString()
        presenter = result.value(1).toString()
        talk = result.value(2).toString()
        print "%s - %s - %s" % (id, presenter, talk)
        
    # Get the presentation table model
    testdbcon.get_presentations_model()
    testdbcon.get_presentations_model()
    
    # Get the events model
    testdbcon.get_events_model()
    testdbcon.get_events_model()
    
    # Get the rooms model
    testdbcon.get_rooms_model("SC2011")
    testdbcon.get_rooms_model("SC2011")
    
    # Get the talks model
    testdbcon.get_talks_model("SC2011", "T105")
    testdbcon.get_talks_model("SC2011", "T105")
