# import the function that will return an instance of a connection
from mysqlconnection import connectToMySQL
# model the class after the friend table from our database
class Users:
    DB = "users_schema"
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
        results = connectToMySQL(cls.DB).query_db(query)
        # Create an empty list to append our instances of friends
        Users = []
        # Iterate over the db results and create instances of friends with cls.
        for user in results:
            Users.append( cls(user) )
        return Users

    # @classmethod
    # def save(cls, data ):
    #     query = """
    #             INSERT into users 
    #             (first_name, last_name, email, created_at, updated_at) 
    #             VALUES 
    #             ( %(first_name)s , %(last_name)s , %(email)s , NOW() , NOW() )
        
    #     """
    #     # data is a dictionary that will be passed into the save method from server.py
    #     result = connectToMySQL(cls.DB).query_db(query,data)
    #     return result

    @classmethod
    def save(cls, data ):
        query = """
                INSERT into users
                (first_name, last_name, email)
                VALUES
                ( %(first_name)s , %(last_name)s , %(email)s)
        """ 

        result = connectToMySQL(cls.DB).query_db(query,data)
        return result