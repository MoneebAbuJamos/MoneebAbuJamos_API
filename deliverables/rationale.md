# Engineering Rationale

## Model and Tool Selection

* The Qwen GGUF model was selected due to its relatively small size and ability to run efficiently on CPU using llama.cpp.
* This choice ensures full offline capability while maintaining acceptable performance.
* FastAPI was chosen for its simplicity, speed, and support for building structured APIs.
* Docker was used to ensure reproducibility and ease of deployment.

## OCR Approach

* Tesseract was selected as the OCR engine because it is lightweight, open-source, and fully offline.
* It integrates easily with Python and works well for structured text extraction.

## Local LLM Approach

* llama-cpp-python was used to run the GGUF model locally.
* This approach eliminates dependency on external APIs and ensures the system can operate in air-gapped environments.
* It also simplifies deployment by embedding the model directly within the system.

## Architecture Decisions

* The system follows a layered architecture:

  * API layer (routes)
  * Service layer (business logic)
  * Data/model layer
* This separation improves clarity and maintainability.
* Each feature (OCR, RAG, LLM, ML) is implemented as an independent service.

## Software Engineering Decisions

* Responsibilities are separated between routes and services to avoid tightly coupled code.
* Models are loaded once and reused across requests to improve performance.
* Configuration is handled centrally to avoid hardcoding values.
* The API exposes only necessary endpoints instead of exposing internal logic.

## Design Patterns

* Service Layer Pattern: used to separate business logic from API routes.
* Singleton-like Model Loading: models are initialized once and reused.
* Modular Design: each capability is implemented in a separate module.

## Maintainability and Extensibility

* New AI capabilities can be added by introducing new service and route modules.
* Existing components are loosely coupled, making changes easier.
* Code structure supports future improvements without major refactoring.

## Tradeoffs

* A smaller LLM model was chosen instead of a larger one to reduce resource usage and Docker image size.
* Precomputing the vector database improves runtime speed but increases project size.
* CPU-based inference is slower than GPU but ensures compatibility across environments.

## Offline Capability

* All models (LLM, embedding model, ML model) are stored locally.
* The system does not require any external API or internet connection.
* Vector database is pre-built to allow immediate use.

## Assumptions and Limitations

* The system assumes a CPU-only environment.
* Performance is limited compared to large cloud-based models.
* OCR accuracy depends on input image quality.
* No GPU acceleration is used.
* The system is designed for demonstration and evaluation purposes rather than production-scale workloads.
