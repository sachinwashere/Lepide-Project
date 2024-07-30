# Lepide-Project

## Overview

This document provides a detailed explanation of the approach taken to set up Docker Desktop on Windows, the challenges encountered, and the solutions implemented to overcome them. The objective was to successfully run a Flask backend and a React frontend in Docker containers.

## Approach

### Initial Setup

1. **System Requirements**: Ensured the system met the necessary requirements for Docker Desktop, including Windows 10 64-bit with Pro, Enterprise, or Education editions, and virtualization enabled in the BIOS.

2. **Installation**:
   - **WSL 2**: Enabled Windows Subsystem for Linux 2.
   - **Docker Desktop**: Installed Docker Desktop with the WSL 2 backend.

### Configuration

1. **Docker Desktop Settings**:
   - Configured Docker Desktop to use the WSL 2 based engine.
   - Enabled WSL integration for the installed Linux distributions.
   - Adjusted resource limits (CPU, Memory, Swap) as needed.

2. **Testing**:
   - Created a simple Dockerfile and tested building and running Docker containers.
   - Verified connectivity between the Flask backend and React frontend.

### Application Setup

1. **Flask Backend**:
   - Set up a Flask application with endpoints for file upload and text summarization.
   - Ensured proper configuration of CORS and logging for debugging.

2. **React Frontend**:
   - Set up a React application with file upload and text summarization functionality.
   - Integrated with the Flask backend using Axios for HTTP requests.

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

## Conclusion

By following a systematic approach, we were able to successfully set up Docker Desktop on Windows, configure the Flask backend and React frontend, and resolve any issues encountered along the way. The project now runs smoothly with both the backend and frontend operating within Docker containers.

## Future Work

To further enhance the project, consider the following improvements:
- Implement comprehensive unit tests for both the backend and frontend.
- Set up continuous integration and continuous deployment (CI/CD) pipelines.
- Optimize Docker images for faster builds and reduced image size.

