# ToDo App

A simple to-do list application built on Frappe

## Prerequisites

Before cloning and running the app, you need to have the following installed:

1. **Python 3.10+**
2. **Node.js 18+** 
3. **MariaDB 10.6+** or **PostgreSQL 13+**
4. **Redis**
5. **Git**
6. **pip and npm**

## Installation & Setup

### Step 1: Install Frappe Bench

First, install the Frappe Bench CLI tool:

```bash
pip install frappe-bench
```

### Step 2: Create a New Bench

Create a new Frappe bench (development environment):

```bash
# Create a new bench with Frappe framework
bench init --frappe-branch version-15 frappe-bench

# Navigate to the bench directory
cd frappe-bench
```

### Step 3: Clone the ToDo App

Clone the todo_app from GitHub:

```bash
# Get the app from GitHub repository
bench get-app https://github.com/rishabrath31/todo_app.git

# Alternative: Clone to a specific branch if needed
# bench get-app https://github.com/rishabrath31/todo_app.git --branch main
```

### Step 4: Create a New Site

Create a new site where the app will be installed:

```bash
# Create a new site (replace 'todo.local' with your preferred site name)
bench new-site todo.local

# You'll be prompted to set a MariaDB root password and Administrator password
```

### Step 5: Install the App

Install the todo_app on the newly created site:

```bash
# Install the todo_app on your site
bench --site todo.local install-app todo_app
```

### Step 6: Start the Development Server

Start the Frappe development server:

```bash
# Start the bench in development mode
bench start

# Alternative: Start in background
# bench start --skip-redis-config-generation
```

### Step 7: Access the Application

Once the server is running, you can access the application:

1. **Web Interface**: Open `http://todo.local:8000` in your browser
2. **Login**: Use the Administrator credentials set during site creation
3. **API**: Available at `http://todo.local:8000/api/`
