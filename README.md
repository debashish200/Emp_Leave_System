Project Description 
-------------------
The Employee leave Management System is a web based application using Django framework to automate the process of managing employee leave requests. It provides a structured workflow for employees to appply for leave and for managers to approve or reject them.
The system also maintians leave balances and displays approved leaves in a calendar view,helping oragnizations track employee availability efficiently.

Objectives
-----------
->Automate leave request and approval process
->Reduce paperwork and manual tracking
->Maintain accurate leave balances
->Provide transparency between employees and managers
-> Visualise leave schedules using a calendar


Technologies Used
-----------------
Backend-Python,Djnago
Frontend-HTML,CSS,BootStrap
Database:SQLLite
Authentication:Django built-in auth system
Calendar:FullCalendar.js

User Roles
----------
Employee
-> Login securely
-> Apply for leave
-> View leave status
-> Check leave balance
-> View leave calendar

Manager
-> Login securely 
-> View pending leave requests 
-> Approve or reject leave requests
-> leave balance updates automatically 
-> view leave calendar

Features
---------
->User authentication & role-based access
->Leave request submission using ModelForms
->Leave approval workflow
->Automatic leave balance update
->Leave calendar with approved leaves
->Manager-only access to approval page
->Secure access control using decorators

Installation & Setup
-----------------------
1️⃣Create Virtual Environment
python -m venv venv
venv\Scripts\activate

2️⃣ Install Dependencies
   pip install django
   
3️⃣ Run Migrations
python manage.py makemigrations
python manage.py migrate

4️⃣ Create Superuser
python manage.py createsuperuser

5️⃣ Run Server
python manage.py runserver

How It Works
---------------
Employee logs in and applies for leave
Manager logs in and approves/rejects leave
On approval:
          Leave balance is reduced automatically
          Leave appears in the calendar
Employees can see updated leave balance

The following features can be added in future versions of this project:
----------------------------------------------------------------------
📧 Email notifications on leave approval/rejection
📱 Mobile responsive UI
📊 Admin dashboard with analytics
🕒 Half-day leave support
🗓️ Holiday calendar integration
🧾 Leave policy rules (max per month/year)
🔔 SMS/WhatsApp alerts
🌐 REST API using Django REST Framework
🧑‍🤝‍🧑 Team-wise leave visibility
📄 PDF reports for HR


