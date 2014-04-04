#If you were at our SQL Training, this is based off our 
# bootcamp database. Make sure to set up your own information 
# about your database before running!

import psycopg2
import psycopg2.extras
from db_info import HOST, NAME, USER, PW

#This line is where you set up your db connection. 
#It's better to put this in a function where you need it
# but to make it easy to find in my example, I made it global
con = psycopg2.connect(host=HOST, database=NAME, user=USER, password=PW)


def getTenMembersTuple():
    """
    This function uses the default psycopg2 cursor
    so cur.fetchall() will retun each row in your query as a tuple.
    """

    cur = con.cursor()
    cur.execute("SELECT * FROM members LIMIT 10;")
    ten_members = cur.fetchall()
    print '\n-----------First 10 members as tuples-----------'
    for t in ten_members:
        print t

    #If we want to get just the emails of the first ten members
    # we would need to figure out which column name was
    # and then search for that index in the tuple
    print '\n-----------First 10 members\'s emails-----------'
    for t in ten_members:
        print t[7]

    
def getTenMembersDict():
    """
    This function builds a DictCursor using the psycopg2 extras library
    and will return your query as a dictionary row.
    """

    cur = con.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute("SELECT * FROM members LIMIT 10;")
    ten_members = cur.fetchall()
    print '\n-----------First 10 members as DictRows-----------'
    for t in ten_members:
        print t

    #Now if we want the to just access their emails, 
    # all we need to do is call the name of the column
    print '\n-----------First 10 member\'s emails-----------'
    for t in ten_members:
        print t['email']


def main():
    getTenMembersTuple()
    getTenMembersDict()

if __name__=='__main__':
    main()
