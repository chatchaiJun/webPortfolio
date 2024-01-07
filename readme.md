# Portfolio Project README

Welcome to my portfolio project! This project showcases my work and achievements. Below are instructions on how to set up and run the project locally.

## Getting Started

### Prerequisites

- Python 3.x installed on your machine
- Git installed on your machine

### Setting up the environment

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/your-portfolio.git
   ```

2. Navigate to the project directory:

   ```bash
   cd your-portfolio
   ```

3. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

   (Note: You might need to use `python3` instead of `python` on some systems.)

4. Activate the virtual environment:

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On Unix or MacOS:

     ```bash
     source venv/bin/activate
     ```

### Installing Dependencies

Run the following command to install the project dependencies:

```bash
pip install -r requirements.txt
```

### Setting up media folders

Create the necessary media folders for the project:

```
mkdir media
mkdir featured_images
```

### Running the project

```
python manage.py runserver
```
