import MySQLdb

def addNewInstructionSet(sketchID, countLines, countArcs):
    """
    Adds a new row to the InstructionSet.
    """
    sqlcmd = """INSERT INTO InstructionSets (Lines, Arcs)
                VALUES (%d, %d)""" % (countLines, countArcs)
    print(sqlcmd)

def addNewSketch(twitterId, InstructionSetId):
    """
    Creates a new row in the Sketches table for new art piece.
    """
    sqlcmd = """INSERT INTO Sketches (TwitterID, FavCount, RetweetCount, InstructionSetID)
                VALUES (%d, %d, %d, %d)""" % (twitterId,0,0,InstructionSetId)
    print(sqlcmd)

def updateSketchInformation(sketchId, favCount, retweetCount):
    """
    Updates the Sketches table to latest count for favourites and retweets.
    """
    sqlcmd = """UPDATE Sketches
                SET FavCount = %d, RetweetCount = %d
                WHERE SketchID = %d""" % (favCount,retweetCount,sketchId)
    print(sqlcmd)