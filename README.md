# Document Summarizer Project

## Overview

This project provides a document summarization application using a Flask backend and a React frontend, containerized with Docker. The backend leverages the `facebook/bart-large-cnn` model from Hugging Face's `transformers` library for text summarization.

## Model Used

The project uses the `facebook/bart-large-cnn` model, a pre-trained BART model fine-tuned on CNN/DailyMail data, which is well-suited for summarization tasks.

## Tools and Libraries

- **Docker Desktop**: For containerizing the application.
- **Flask**: Backend framework to handle file uploads and API requests.
- **React**: Frontend framework for user interface.
- **Axios**: For making HTTP requests from the React frontend to the Flask backend.
- **Flask-CORS**: To handle Cross-Origin Resource Sharing (CORS) issues.
- **transformers**: Hugging Face library to use the pre-trained BART model.
- **psutil**: To monitor resource usage and prevent memory leaks.
- **memory-profiler**: To profile memory usage in the Flask application.

## Challenges and Solutions

### Challenge 1: Docker Desktop Installation Issues

- **Problem**: Docker Desktop was not starting correctly, showing errors related to WSL 2 and virtualization.
- **Solution**:
  - Verified that virtualization was enabled in the BIOS.
  - Ensured WSL 2 was correctly installed and set as the default version.
  - Reinstalled Docker Desktop with the latest version.
  - Configured Docker Desktop to use the WSL 2 backend and enabled necessary integrations.

### Challenge 2: Flask Server Crashing

- **Problem**: The Flask server was crashing shortly after starting.
- **Solution**:
  - Reviewed and updated the Flask application code to ensure proper resource management and error handling.
  - Enabled detailed logging to identify and resolve any issues causing the crash.
  - Used monitoring tools to track memory usage and prevent memory leaks.

### Challenge 3: Connectivity Issues Between Frontend and Backend

- **Problem**: The React frontend was unable to communicate with the Flask backend.
- **Solution**:
  - Verified that both the frontend and backend were running on the correct ports.
  - Configured CORS in the Flask backend to allow requests from the React frontend.
  - Tested endpoints using Postman to ensure they were functioning correctly.
  - Checked network requests in the browser's developer tools to identify and resolve any issues.

## Steps to Run the Project

### Prerequisites

- Docker Desktop installed and running.
- Git installed to clone the repository.

### Step-by-Step Instructions

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/sachinwashere/Lepide-Project.git
    cd Lepide-Project
    ```

2. **Build and Run the Docker Containers**:
    ```bash
    docker-compose up --build
    ```

3. **Access the Application**:
    - The React frontend will be available at `http://localhost:3000`.
    - The Flask backend API will be available at `http://localhost:5000`.


