# Unit Converter

A simple Django web application that allows you to convert between different units of **length**, **weight**, and **temperature**. 

---

## Features

- Convert between various units of length, weight, and temperature.
- Clean and minimal Bootstrap-based interface.
- Form validation and instant result display.

---

## How to Use

1. **Clone the repository** and install dependencies (preferably in a virtual environment):

    ```bash
    git clone <repo-url>
    cd Unit-Converter
    python -m venv venv
    source venv/bin/activate
    pip install requirements.txt
    ```

2. **Run migrations** (no database models are used, but Django requires this step):

    ```bash
    python manage.py migrate
    ```

3. **Start the development server:**

    ```bash
    python manage.py runserver
    ```

4. **Open your browser** and go to [http://127.0.0.1:8000/length/](http://127.0.0.1:8000/length/) (or `/weight/` or `/temperature/`) to use the converter.

---

## Based on

This project is based on the learning and practice projects suggested by [roadmap.sh](https://roadmap.sh/projects/unit-converter), a popular resource for developers.

---


## License

This project is for educational purposes.