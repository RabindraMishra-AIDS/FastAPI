# FastAPI CRUD Application

This project demonstrates a simple CRUD (Create, Read, Update, Delete) API using **FastAPI**, a modern, fast (high-performance) web framework for building APIs with Python 3.6+ based on standard Python type hints.

---

## **About FastAPI**
FastAPI is a Python framework designed for building APIs quickly and efficiently. It provides:
- Automatic validation of request and response data using Pydantic.
- Automatic generation of OpenAPI documentation (Swagger UI).
- High performance, comparable to Node.js and Go.

---

## **Project Setup**

Follow these steps to set up and run the project locally:

### **1. Create a Virtual Environment**
Run the following commands to create and activate a virtual environment:

```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### **2. Install Dependencies**
Install the required dependencies from the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### **3. Run the Application**
Start the FastAPI server:

```bash
uvicorn main:app --reload
```

- The API will be available at: `http://127.0.0.1:8000`
- Swagger UI documentation: `http://127.0.0.1:8000/docs`

---

## **Tools and Approaches**

- **FastAPI**: Core framework for building the API.
- **Pydantic**: Used for data validation and serialization.
- **Uvicorn**: ASGI server for running the FastAPI application.
- **Python Type Hints**: Used for better code readability and validation.

---

## **Contribution & Collaboration**

We welcome contributions to improve this project! Follow these steps to contribute:

1. **Fork the Repository**: Click the "Fork" button at the top of this repository.
2. **Clone the Repository**: Clone your forked repository to your local machine.
   ```bash
   git clone https://github.com/your-username/fastapi-crud.git
   ```
3. **Create a Branch**: Create a new branch for your feature or bug fix.
   ```bash
   git checkout -b feature-name
   ```
4. **Make Changes**: Add your changes and commit them.
   ```bash
   git add .
   git commit -m "Description of changes"
   ```
5. **Push Changes**: Push your changes to your forked repository.
   ```bash
   git push origin feature-name
   ```
6. **Create a Pull Request**: Open a pull request to the main repository.

---

## **API Endpoints**

### **GET Endpoints**
- `/`: Returns a welcome message.
- `/reportcard`: Fetches all report cards.

### **POST Endpoint**
- `/reportcard`: Adds a new report card.

### **PUT Endpoint**
- `/reportcard/{student_id}`: Updates an existing report card by `student_id`.

### **DELETE Endpoint**
- `/reportcard/{student_id}`: Deletes a report card by `student_id`.

---

# FastAPI CRUD Application

This project demonstrates a simple CRUD (Create, Read, Update, Delete) API using **FastAPI**, a modern, fast (high-performance) web framework for building APIs with Python 3.6+ based on standard Python type hints.

---

## **About FastAPI**
FastAPI is a Python framework designed for building APIs quickly and efficiently. It provides:
- Automatic validation of request and response data using Pydantic.
- Automatic generation of OpenAPI documentation (Swagger UI).
- High performance, comparable to Node.js and Go.

---

## **Project Setup**

Follow these steps to set up and run the project locally:

### **1. Create a Virtual Environment**
Run the following commands to create and activate a virtual environment:

```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### **2. Install Dependencies**
Install the required dependencies from the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### **3. Run the Application**
Start the FastAPI server:

```bash
uvicorn main:app --reload
```

- The API will be available at: `http://127.0.0.1:8000`
- Swagger UI documentation: `http://127.0.0.1:8000/docs`

---

## **Tools and Approaches**

- **FastAPI**: Core framework for building the API.
- **Pydantic**: Used for data validation and serialization.
- **Uvicorn**: ASGI server for running the FastAPI application.
- **Python Type Hints**: Used for better code readability and validation.

---

## **Contribution & Collaboration**

We welcome contributions to improve this project! Follow these steps to contribute:

1. **Fork the Repository**: Click the "Fork" button at the top of this repository.
2. **Clone the Repository**: Clone your forked repository to your local machine.
   ```bash
   git clone https://github.com/your-username/fastapi-crud.git
   ```
3. **Create a Branch**: Create a new branch for your feature or bug fix.
   ```bash
   git checkout -b feature-name
   ```
4. **Make Changes**: Add your changes and commit them.
   ```bash
   git add .
   git commit -m "Description of changes"
   ```
5. **Push Changes**: Push your changes to your forked repository.
   ```bash
   git push origin feature-name
   ```
6. **Create a Pull Request**: Open a pull request to the main repository.

---

## **API Endpoints**

### **GET Endpoints**
- `/`: Returns a welcome message.
- `/reportcard`: Fetches all report cards.

### **POST Endpoint**
- `/reportcard`: Adds a new report card.

### **PUT Endpoint**
- `/reportcard/{student_id}`: Updates an existing report card by `student_id`.

### **DELETE Endpoint**
- `/reportcard/{student_id}`: Deletes a report card by `student_id`.

---
