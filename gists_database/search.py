from .models import Gist
from datetime import datetime

def search_gists(db_connection, **kwargs):
    results = []
    c = db_connection.cursor()
    github_id = None
    created_at = None
    
    if kwargs:
        for key,value in kwargs.items():
            if key == "github_id":
                github_id = value
            if key == "created_at":
                created_at = value
    
    if github_id:
        c.execute("SELECT * FROM gists WHERE github_id = :github_id",
                                                        {"github_id":github_id})
        list_of_tuples = c.fetchall()
        for gist in list_of_tuples:
            g = Gist(gist)
            results.append(g)
        return results
    
    if created_at:
        c.execute("SELECT * FROM gists WHERE datetime(created_at) = datetime(:created_at)",
                                                        {"created_at":created_at})
        list_of_tuples = c.fetchall()
        for gist in list_of_tuples:
            g = Gist(gist)
            results.append(g)
        return results
    
    
    c.execute("SELECT * FROM gists")
    list_of_tuples = c.fetchall()

    for gist in list_of_tuples:
        g = Gist(gist)
        results.append(g)
    return results
        
            
    
