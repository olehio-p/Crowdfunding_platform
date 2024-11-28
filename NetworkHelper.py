import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Crowdfunding_platform.settings")


import django
django.setup()


import requests

BASE_URL = 'http://localhost:8101/api'
TOKEN_URL = f'{BASE_URL}-token-auth/'
USERNAME = 'test'
PASSWORD = 'test'

course_levels_url = f'{BASE_URL}/course-levels/'
courses_url = f'{BASE_URL}/courses/'

def get_auth_token():
    response = requests.post(TOKEN_URL, data={'username': USERNAME, 'password': PASSWORD})
    if response.status_code == 200:
        token = response.json().get('token')
        print("Token obtained successfully.")
        return token
    else:
        print("Failed to obtain token:", response.status_code, response.text)
        return None

def get_headers(token):
    return {'Authorization': f'Token {token}'}

def get_course_levels(token):
    response = requests.get(course_levels_url, headers=get_headers(token))
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to retrieve course levels:", response.status_code)
        return None

def create_course_level(token, level_name, description):
    data = {
        'level_name': level_name,
        'description': description
    }
    response = requests.post(course_levels_url, headers=get_headers(token), json=data)
    if response.status_code == 201:
        print("Course level created successfully:", response.json())
    else:
        print("Failed to create course level:", response.status_code, response.text)

def get_courses(token):
    response = requests.get(courses_url, headers=get_headers(token))
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to retrieve courses:", response.status_code)
        return None

def create_course(token, name, description, duration, price, level_id):
    data = {
        'name': name,
        'description': description,
        'duration': duration,
        'price': price,
        'level_id': level_id
    }
    response = requests.post(courses_url, headers=get_headers(token), json=data)
    if response.status_code == 201:
        print("Course created successfully:", response.json())
    else:
        print("Failed to create course:", response.status_code, response.text)

if __name__ == "__main__":
    token = get_auth_token()
    if token:
        course_levels = get_course_levels(token)
        print("Course Levels:", course_levels)

        create_course_level(token, "Expert", "Aimed at professionals looking to deepen expertise.")

        courses = get_courses(token)
        print("Courses:", courses)
