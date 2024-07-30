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

## Approach

### Initial Setup

1. **System Requirements**: Ensure the system meets the necessary requirements for Docker Desktop, including Windows 10 64-bit with Pro, Enterprise, or Education editions, and virtualization enabled in the BIOS.

2. **Installation**:
   - **WSL 2**: Enable Windows Subsystem for Linux 2.
   - **Docker Desktop**: Install Docker Desktop with the WSL 2 backend.

### Configuration

1. **Docker Desktop Settings**:
   - Configure Docker Desktop to use the WSL 2 based engine.
   - Enable WSL integration for the installed Linux distributions.
   - Adjust resource limits (CPU, Memory, Swap) as needed.

2. **Testing**:
   - Create a simple Dockerfile and test building and running Docker containers.
   - Verify connectivity between the Flask backend and React frontend.

### Application Setup

1. **Flask Backend**:
   - Set up a Flask application with endpoints for file upload and text summarization.
   - Ensure proper configuration of CORS and logging for debugging.

2. **React Frontend**:
   - Set up a React application with file upload and text summarization functionality.
   - Integrate with the Flask backend using Axios for HTTP requests.

## Challenges and Solutions

### Challenge 1: Model Selection

- **Problem**: Determining the best model for text summarization.
- **Solution**: Considered several models including:
  - `t5-small`: Good summarization but limited by its smaller size.
  - `distilbart-cnn-12-6`: Faster inference but slightly lower quality summaries.
  - `facebook/bart-large-cnn`: Provided the best balance of speed and summary quality.
  
  After evaluating the performance and summary quality, we selected `facebook/bart-large-cnn` for its superior summarization capabilities.

### Challenge 2: Docker Desktop Installation Issues

- **Problem**: Docker Desktop was not starting correctly, showing errors related to WSL 2 and virtualization.
- **Solution**:
  - Verified that virtualization was enabled in the BIOS.
  - Ensured WSL 2 was correctly installed and set as the default version.
  - Reinstalled Docker Desktop with the latest version.
  - Configured Docker Desktop to use the WSL 2 backend and enabled necessary integrations.

### Challenge 3: Flask Server Crashing

- **Problem**: The Flask server was crashing shortly after starting.
- **Solution**:
  - Reviewed and updated the Flask application code to ensure proper resource management and error handling.
  - Enabled detailed logging to identify and resolve any issues causing the crash.
  - Used monitoring tools to track memory usage and prevent memory leaks.

### Challenge 4: Connectivity Issues Between Frontend and Backend

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


