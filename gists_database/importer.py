import requests

SQL_INSERT_TEMPLATE = ''' INSERT INTO gists (github_id, html_url, git_pull_url, 
                                            git_push_url, commits_url, forks_url, 
                                            public, created_at, updated_at, 
                                            comments, comments_url)
                                            
                            VALUES (:github_id, :html_url, :git_pull_url, 
                                            :git_push_url, :commits_url, :forks_url, 
                                            :public, :created_at, :updated_at, 
                                            :comments, :comments_url);
'''

def import_gists_to_database(db, username, commit=True):
    
    url = 'https://api.github.com/users/{}/gists'.format(username)
    response = requests.get(url)
    response.raise_for_status()
    list_of_gists = response.json()
   
    for gist in list_of_gists:

        params = {
            'github_id':gist['id'],
            'html_url':gist['html_url'],
            'git_pull_url':gist['git_pull_url'],
            'git_push_url':gist['git_push_url'],
            'commits_url':gist['commits_url'],
            'forks_url':gist['forks_url'],
            'public':gist['public'],
            'created_at':gist['created_at'],
            'updated_at':gist['updated_at'],
            'comments':gist['comments'],
            'comments_url':gist['comments_url']       
        }
        
        db.execute(SQL_INSERT_TEMPLATE, params)
        
    if commit:
        db.commit()
        
    

    
