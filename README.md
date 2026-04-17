# 📝 Django Blogs

A personal blogging platform built with Django, deployed on PythonAnywhere. This project was created as a hands-on learning exercise in Django web development — covering everything from models and views to deployment.

🌐 **Live Demo:** [ayushpundir.pythonanywhere.com](https://ayushpundir.pythonanywhere.com/)

---

## 🚀 Features

- 📰 Browse blog posts organized by categories (Tech, Sports, Politics, Gaming, Weather, Health)
- 🔐 User authentication — Register & Login
- 🏷️ Category-based filtering
- 📌 Featured and Recent posts sections
- 📱 Clean, readable layout
- ⚙️ Admin panel for managing posts and users

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| Backend | Django (Python) |
| Database | SQLite3 |
| Frontend | HTML, CSS |
| Deployment | PythonAnywhere |

---

## 📁 Project Structure

```
django-blogs/
├── blog/               # Main blog app (models, views, urls)
├── users/              # Authentication app (login, register)
├── templates/          # HTML templates
├── static/             # CSS, JS, images
├── manage.py
└── requirements.txt
```

---

## ⚡ Getting Started Locally

### Prerequisites
- Python 3.x
- pip

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/ayushpundir12/<repo-name>.git
cd <repo-name>

# 2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Apply migrations
python manage.py migrate

# 5. Create a superuser (for admin access)
python manage.py createsuperuser

# 6. Run the development server
python manage.py runserver
```

Then open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.

---

## 🌍 Deployment

This project is deployed on **PythonAnywhere**. To deploy your own instance:

1. Upload your project files to PythonAnywhere
2. Set up a virtual environment and install requirements
3. Configure the WSGI file to point to your Django app
4. Set `DEBUG = False` and configure `ALLOWED_HOSTS` in `settings.py`
5. Collect static files: `python manage.py collectstatic`

---

## 📸 Screenshots

> _Add screenshots of your homepage, blog post page, and login screen here._

---

## 🙋‍♂️ About

Built by **Ayush Pundir** as a personal learning project to explore Django and web development. Every feature in this project was a step forward in that journey.

- 🐙 GitHub: [@ayushpundir12](https://github.com/ayushpundir12)
- 💼 LinkedIn: [Ayush Pundir](https://www.linkedin.com/in/ayush-pundir-/)
