import requests
from django.shortcuts import render, redirect
from django.contrib import messages

API_BASE_URL = 'http://localhost:8101/api'
API_TOKEN_URL = f'{API_BASE_URL}-token-auth/'

USERNAME = 'test'
PASSWORD = 'test'

TOKEN = None

def get_or_refresh_token():
    global TOKEN
    if not TOKEN:
        response = requests.post(API_TOKEN_URL, data={'username': USERNAME, 'password': PASSWORD})
        if response.status_code == 200:
            TOKEN = response.json().get('token')
            print("Token obtained successfully.")
        else:
            print("Failed to obtain token:", response.status_code, response.text)
            TOKEN = None
    return TOKEN

def course_list(request):
    global TOKEN
    token = get_or_refresh_token()
    if not token:
        messages.error(request, "Не вдалося отримати токен авторизації.")
        return render(request, 'course_list.html', {'courses': []})

    try:
        response = requests.get(f"{API_BASE_URL}/courses/", headers={'Authorization': f'Token {token}'})
        if response.status_code == 401:
            TOKEN = None
            return course_list(request)
        response.raise_for_status()
        courses = response.json()
    except requests.RequestException as e:
        messages.error(request, f"Помилка при завантаженні курсів: {e}")
        courses = []

    return render(request, 'course_list.html', {'courses': courses})

def delete_course(request, course_id):
    global TOKEN
    token = get_or_refresh_token()
    if not token:
        messages.error(request, "Не вдалося отримати токен авторизації.")
        return redirect('course_list')

    if request.method == "POST":
        try:
            response = requests.delete(
                f"{API_BASE_URL}/courses/{course_id}/",
                headers={'Authorization': f'Token {token}'}
            )
            if response.status_code == 401:
                TOKEN = None
                return delete_course(request, course_id)
            response.raise_for_status()
            messages.success(request, "Курс видалено успішно.")
        except requests.RequestException as e:
            messages.error(request, f"Помилка при видаленні курсу: {e}")

    return redirect('course_list')
