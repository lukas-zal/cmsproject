-- WE DROP TABLES IF THEY EXSIST
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS project_tasks;
DROP TABLE IF EXISTS projects;
DROP TABLE IF EXISTS consultants;
DROP TABLE IF EXISTS clients;

-- CLIENTS
CREATE TABLE clients (
    client_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    industry VARCHAR(255),
    contact_email VARCHAR(255),
    contact_phone VARCHAR(50),
    address TEXT
);

-- CONSULTANTS
CREATE TABLE consultants (
    consultant_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(150) NOT NULL,
    last_name VARCHAR(150) NOT NULL,
    role VARCHAR(150),
    phone VARCHAR(50),
    email VARCHAR(255)
);

-- PROJECTS
CREATE TABLE projects (
    project_id INT AUTO_INCREMENT PRIMARY KEY,
    client_id INT NOT NULL,
    title VARCHAR(255) NOT NULL,
    start_date DATE,
    end_date DATE,
    status VARCHAR(100),

    FOREIGN KEY (client_id) REFERENCES clients(client_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

-- PROJECT TASKS
CREATE TABLE project_tasks (
    task_id INT AUTO_INCREMENT PRIMARY KEY,
    project_id INT NOT NULL,
    assigned_to INT,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    due_date DATE,
    status VARCHAR(100),

    FOREIGN KEY (project_id) REFERENCES projects(project_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,

    FOREIGN KEY (assigned_to) REFERENCES consultants(consultant_id)
        ON DELETE SET NULL
        ON UPDATE CASCADE
);

-- USERS
CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    consultant_id INT,
    username VARCHAR(150) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    role VARCHAR(100) DEFAULT 'consultant',

    FOREIGN KEY (consultant_id) REFERENCES consultants(consultant_id)
        ON DELETE SET NULL
        ON UPDATE CASCADE
);
