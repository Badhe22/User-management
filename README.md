# 🧑‍💼 User Management System

A secure and scalable Django + React application for managing users with JWT authentication, Microsoft SSO support, and role-based access control.

---

## 🔐 Features

- **JWT Authentication** with access/refresh tokens
- **Microsoft SSO** login (OAuth integration)
- **Role-based Access**:
  - Admin: full CRUD on users
  - Normal users: view/update their own profile
- **User Activation Toggle** by Admin
- **Secure Protected APIs**
- **Frontend (React)**:
  - Login/logout functionality
  - Dashboard
  - Token handling with auto-refresh
  - Route protection

---
## ⚙️ Installation & Setup

1. Create virtual environment
   ```bash
   python -m venv venv
   source venv/bin/activate


2. Install packages
   pip install -r backend/requirements.txt
3. Add environment variables in backend/.env:
   ```bash
    SECRET_KEY=your_secret_key
    DEBUG=True
    MYSQL_DB=your_db
    MYSQL_USER=your_user
    MYSQL_PASSWORD=your_password
    MYSQL_HOST=localhost
   
    MYSQL_PORT=3306
    MICROSOFT_CLIENT_ID=your_client_id
    MICROSOFT_SECRET=your_client_secret

5. Run migrations
   ```bash
   cd backend
   python manage.py makemigrations
   python manage.py migrate

7. Create superuser
   ```bash
   python manage.py createsuperuser

9. Start the server
    ```bash
   python manage.py runserver



## Frontend (React)

1. Navigate to frontend folder
   ```bash
   cd frontend

3. Install dependencies
   ```bash
   npm install

5. Create .env in frontend/:
   ```bash
   REACT_APP_API_BASE_URL=http://localhost:8000

7. Run app
   ```bash
   npm start


🚀 Usage

1. Go to: http://localhost:3000
2. Login with admin credentials
3. On success, access token is stored and dashboard is shown
4. Logout clears token and redirects to login

📸 Screenshots
![Screenshot 2025-07-04 225919](https://github.com/user-attachments/assets/8297b76e-086a-4652-b2c3-1408c8327773)

![Screenshot 2025-07-04 230110](https://github.com/user-attachments/assets/2874021a-2258-4c5f-93a3-9b2b8e94a140)

![Screenshot 2025-07-04 230222](https://github.com/user-attachments/assets/378e5d68-f1b1-4852-80cd-ea53f4ebee0b)

![Screenshot 2025-07-04 230733](https://github.com/user-attachments/assets/770e047f-69c0-4566-951e-ffba5ffae865)

![Screenshot 2025-07-04 230813](https://github.com/user-attachments/assets/10176a24-fab1-48d3-a68a-d5668f57e459)





