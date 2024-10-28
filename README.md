## Running a visual model from HuggingFace with FastAPI in Docker.

### The starter file is [model_starter.py](model_starter.py) with a model from Hugging Face: https://huggingface.co/dandelin/vilt-b32-finetuned-vqa

The final app is in [main.py](main.py) and final model(and processor) code is in [model.py](model.py).

## Setup Docker and VS Code

STEP 1 : Run `docker init`

STEP 2 : Select Python image and use this command during docker init

```
CMD uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

STEP 3: Remove `-slim` and add this to Dockerfile (to install transformers)

```
# Install Rust compiler
RUN curl https://sh.rustup.rs -sSf | bash -s -- -y
ENV PATH="/root/.cargo/bin:${PATH}"
```

STEP 4: Remove the custom user from the Dockerfile to simplify, because HF needs write permissions to download and save the model.

STEP 3: Add volume to `compose.yaml` for proper sync:

```
    volumes:
      - .:/app
```

STEP 4: Run `docker compose up --build`

STEP 5: Docker desktop > Run the app; (http://localhost:8000/docs) -> FastAPI Swagger UI 
## Authorization has been added using FastAPI Security. 
