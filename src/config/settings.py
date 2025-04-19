from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore", env_file_encoding="utf-8")

    GROQ_API_KEY: str 
    ELEVENLABS_API_KEY: str
    ELEVENLABS_VOICE_ID: str
    TOGETHER_API_KEY: str

    QDRANT_API_KEY: str | None
    QDRANT_URL: str
    QDRANT_PORT: str = "6333"
    QDRANT_HOST: str | None = None

    TEXT_MODEL_NAME: str = "llama-3.3-70b-versatile"
    SMALL_TEXT_MODEL_NAME: str = "gemma2-9b-it"
    STT_MODEL_NAME: str = "whisper-large-v3-turbo"
    TTS_MODEL_NAME: str = "eleven_flash_v2_5"
    TTI_MODEL_NAME: str = "black-forest-labs/FLUX.1-schnell-Free"
    ITT_MODEL_NAME: str = "llama-3.2-90b-vision-preview"

    MEMORY_TOP_K: int = 3
    ROUTER_MESSAGES_TO_ANALYZE: int = 3
    TOTAL_MESSAGES_SUMMARY_TRIGGER: int = 20
    TOTAL_MESSAGES_AFTER_SUMMARY: int = 5

    # Database configuration
    MEMORY_DB_PATH: str | None = None
    
    @property
    def SHORT_TERM_MEMORY_DB_PATH(self) -> str:
        if self.MEMORY_DB_PATH:
            return self.MEMORY_DB_PATH
        
        # Default to project-relative path if not specified
        default_path = Path(__file__).parent.parent.parent / "data" / "memory.db"
        return str(default_path)
    
    def __init__(self, **data):
        super().__init__(**data)
        # Ensure data directory exists
        from os import makedirs
        from os.path import dirname
        makedirs(dirname(self.SHORT_TERM_MEMORY_DB_PATH), exist_ok=True)


settings = Settings()

