import requests

def get_user(user_name):    
    url = f"https://api.github.com/users/{user_name}"

    response = requests.get(url)    

    # Check if successful
    if response.status_code == 200:
        print("User Status Code:", response.status_code)
    # Get specific data from the JSON
    # .get returns value if key exists else None
    # or "N/A" is value given if .get is None or blank.
        data = response.json()       
        print("Name:", data.get('name') or "N/A")
        print("Bio:", data.get('bio') or "N/A")
        print("Location:", data.get('location') or "N/A")
        print("Public Repos:", data.get('public_repos', "N/A"))
        # .get(key, default) wont replace 0 with N/A
            
            
    elif response.status_code == 404:
        print(f"User '{user_name}' not found")
        return None
    else:
        print(f'Error: {response.status_code}')
        return None 


#----------------------------------------------------------
def user_repos(user_name):
    url = f"https://api.github.com/users/{user_name}/repos?sort=updated&per_page=5"

    response = requests.get(url)    
    
    if response.status_code == 200:
        print("User_Repositories Status Code:", response.status_code)
    # Get specific data from the JSON
        data = response.json()     
        ##print(data)
    elif response.status_code == 404:
        print(f"Repositories for '{user_name}' not found")
        return None        
        
    else:
        print(f'Error: {response.status_code}')
        return None

    # Lists their 5 most recent repositories
    
    print("Displaying 5 most recent repositories.") 
    for repo in data[:5]:        
        print("\nName:", repo.get('name') or "N/A")
        print("Description:", repo.get('description') or "N/A")
        print("Stars:", repo.get('stargazers_count', "N/A"))
        print("Language:", repo.get('language') or "N/A")


# ask for user name and run get_user function
#user_name = input(f'Enter GitHub username to lookup:\n')
user_name = "andreigurd"
#get_user(user_name)
user_repos(user_name)


