import requests

def get_user(user_name):    
    url = f"https://api.github.com/users/{user_name}"

    response = requests.get(url)    

    # Check if successful
    if response.status_code == 200:
        print("User_Name Status Code:", response.status_code)
    # Get specific data from the JSON
        data = response.json()       
        print("Name:", data['name'])
        print("Bio:", data['bio'])
        print("Location:", data['location'])
        print("Public Repos:", data['public_repos'])
        #print(data.keys())    
            
    elif response.status_code == 404:
        print(f"User_Name '{user_name}' not found")
        return None
    else:
        print(f'Error: {response.status_code}')
        return None 


#----------------------------------------------------------
def user_repos(user_name):
    url = f"https://api.github.com/users/{user_name}/repos?sort=updated&per_page=5"

    response = requests.get(url)

    # data is just dictionaries no lists.

    print("\nUser_Repositories Status Code:", response.status_code)

    if response.status_code == 200:
        print("User_Repositories Status Code:", response.status_code)
    # Get specific data from the JSON
        data = response.json()     
        print(data)
    elif response.status_code == 404:
        print(f"Repositories for '{user_name}' not found")
        return None        
        
    else:
        print(f'Error: {response.status_code}')
        return None



# ask for user name and run get_user function
#user_name = input(f'Enter GitHub username to lookup:\n')
user_name = "andreigurd"
#get_user(user_name)
user_repos(user_name)


