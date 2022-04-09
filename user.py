# import the function that will return an instance of a connection
from mysqlconnection import connectToMySQL

def function(arg):
    from xml.dom.xmlbuilder import _DOMInputSourceCharacterStreamType
# model the class after the friend table from our database
class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('users').query_db(query)
        # Create an empty list to append our instances of friends
        users = []
        # Iterate over the db results and create instances of friends with cls.
        for user in results:
            users.append( cls(user) )
        return users
    
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM users WHERE id=%(id)s;" #Select all the data from only one user
        results = connectToMySQL('users').query_db(query, data) #now we have to 1. connect to mySQL and connect to 'users' db. 
        #2. query that db with our new query 3. insert the data from above so the classmethod recognizes the id, first_name etc.
        return cls(results[0]) #not sure about the cls, but the query always comes back as a list
        #so you have to 1. iterate through the list for multiple items. or 2. specify you want the first item in the list
        # (Which would be the only item in this list since it's only returning one user with a specific id
    
    @classmethod
    def create_new_user(cls, data):
        query = "INSERT INTO users(first_name, last_name, email) VALUES(%(first_name)s, %(last_name)s, %(email)s);"
        result = connectToMySQL('users').query_db(query, data)
        return result
    
    @classmethod
    def delete(cls, data):
        query = "DELETE FROM users where id= %(id)s"
        result = connectToMySQL('users').query_db(query, data)
        return result
        
    @classmethod
    def edit(cls, data):
        query = "UPDATE users SET first_name = %(first_name)s, last_name= %(last_name)s, email=%(email)s), updated_at = NOW() WHERE id=%(id)s"
        result = connectToMySQL('users').query_db(query,data)
        return result

