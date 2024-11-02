# Tourism App Deployment Instructions

This document provides instructions for deploying the Tourism App using Docker.

## Prerequisites

- Docker installed on your machine.
- Docker Compose installed on your machine.

## Deployment Steps

1. **Clone the Repository**

   ```bash
   git clone https://github.com/your-repo/tourism-app.git
   cd tourism-app
   ```

2. **Build and Start the Containers**

   ```bash
   docker-compose up --build
   ```

3. **Access the Application**

   - Frontend: Open your browser and navigate to `http://localhost:3000`.
   - Backend: The API will be available at `http://localhost:8000`.

## Additional Commands

- **Stop the Containers**

  ```bash
  docker-compose down
  ```

- **Rebuild the Containers**

  ```bash
  docker-compose up --build
  ```

- **View Logs**

  ```bash
  docker-compose logs -f
  ```

## Troubleshooting

- If you encounter any issues during the build process, ensure that Docker and Docker Compose are correctly installed and that there are no port conflicts on your machine.

## Contributing

If you would like to contribute to this project, please follow the standard GitHub workflow:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Make your changes and commit them.
4. Push your changes to your fork.
5. Submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
