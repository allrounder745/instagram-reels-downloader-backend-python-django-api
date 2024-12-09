# Instagram Reels Downloader Backend Python Django API

Welcome to the Insta Reels Downloader Backend Python Django API repository! This project provides a backend API for downloading Instagram Reels, built with Django. It powers the site [reeldown.io](https://reeldown.io).

## Features

- **Instagram Reels Downloader**: Easily download Instagram Reels by providing the URL.
- **Django Framework**: Built using the robust Django framework, ensuring a scalable and maintainable codebase.
- **RESTful API**: Simple and intuitive API endpoints for seamless integration.

## Live Demo

Check out the live site using this API: [reeldown.io](https://reeldown.io)

## Frontend Repository

This backend API is implemented in a React Vite application. You can find the frontend repository here: [insta-reels-downloader-frontend-react](https://github.com/ziauldin123/insta-reels-downloader-frontend-react)

## Getting Started

### Prerequisites

- Python 3.8+
- Django 3.2+
- pip (Python package installer)

### Installation

1. **Fork the Repository**: Click on the `Fork` button at the top-right corner of this repository to fork it to your own GitHub account.

2. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/insta-reels-downloader-backend-django-api.git
   cd insta-reels-downloader-backend-django-api
3. **Create a Virtual Environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
4. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
5. **Run Migrations**:
   ```bash
   python manage.py migrate
6. **Start the Development Server**:
   ```bash
   python manage.py runserver

### Usage

After starting the development server, you can access the API at `http://127.0.0.1:8000/reels/api/download/`.

### API Endpoints

- **Download Reel**: POST `/api/download/`
  - **Request Body**:
    ```json
    {
      "url": "https://www.instagram.com/reel/XXXXXXXXXX/"
    }
    ```
  - **Response**:
    ```json
    {
      "download_link": "https://path-to-downloaded-reel"
    }
    ```

### Built With

- [Django](https://www.djangoproject.com/) - The web framework used for building the backend API.
- [Django REST framework](https://www.django-rest-framework.org/) - A powerful and flexible toolkit for building Web APIs.

### Contributing

We welcome contributions! Follow these steps to contribute:

1. **Fork the project**.
2. **Create your feature branch** (`git checkout -b feature/AmazingFeature`).
3. **Commit your changes** (`git commit -m 'Add some AmazingFeature'`).
4. **Push to the branch** (`git push origin feature/AmazingFeature`).
5. **Open a Pull Request**.

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### Contact

For any inquiries, please contact us at [contact@reeldown.io](mailto:mziauldin2@gmail.com).



