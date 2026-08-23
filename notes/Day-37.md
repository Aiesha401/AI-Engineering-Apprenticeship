# Day 37

## What did I build?

I containerized CommerceOps AI using Docker and successfully ran the application inside a Docker container. I also deployed the FastAPI application publicly and verified that the deployed `/chat` endpoint works.

## What did I learn?

I learned how Docker images and containers work, how a Dockerfile defines the application environment, and how environment variables can be passed into a container at runtime.

I also learned how to deploy a Dockerized FastAPI application to the cloud, configure the correct project root and Dockerfile path, and make Uvicorn listen on the platform-provided port.

## Biggest challenge today

The biggest challenge was getting the NVIDIA API key to work correctly inside the Docker container and troubleshooting the deployment configuration.

I also had issues with the Dockerfile path, Python imports inside the container, and the Docker build context.

## How did I solve it?

I compared the API key length and partial fingerprint between my local Python environment and Docker. I found that quotes in the `.env` value were being included by Docker, so I removed them and verified that both environments received the same value.

I then fixed the Docker and deployment configuration. The main issue with Render was that my Git repository root was one level above the `commerceops-ai` project, so I configured `commerceops-ai` as the Root Directory.

After deployment, I verified the public API through the Render URL and tested the `/chat` endpoint successfully.

## What surprised me?

I was surprised that Docker could run the same CommerceOps application with its own Python environment while still accessing the SQLite database and NVIDIA API.

I was also surprised that a small configuration such as the Root Directory could prevent the entire cloud deployment from finding the Dockerfile.

## One thing I still don't understand

I want to learn how Docker containers handle persistent databases and application data when deployed to production.

I also want to learn how to turn the deployed FastAPI backend into a proper user-facing chat interface instead of requiring users to use the Swagger documentation.