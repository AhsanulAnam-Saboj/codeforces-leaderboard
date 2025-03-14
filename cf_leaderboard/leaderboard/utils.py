import requests

def fetch_codeforces_rating(handle):
        """Fetch the latest rating and maximum rating of a Codeforces user."""
        url = f"https://codeforces.com/api/user.rating?handle={handle}"
        
        # Make the API request
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            
            if data["status"] == "OK":
                if data["result"]:
                    # The result contains the user's rating history
                    ratings = [entry['newRating'] for entry in data["result"]]
                    
                    # Get the latest rating (last entry in the list)
                    current_rating = ratings[-1]
                    
                    # Get the maximum rating from all the rating changes
                    max_rating = max(ratings)
                    
                    # Return both current rating and max rating
                    
                    rating_dic = {
                        'current_rating' : current_rating,
                        'max_rating' : max_rating
                    }
                    return rating_dic
                else:
                    return None, None
            else:
                print("Error fetching rating:", data["comment"])
                return None, None
        else:
            print(f"Failed to fetch data. HTTP Status Code: {response.status_code}")
            return None, None
