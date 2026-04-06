import logging
import os
import json

# Create logs folder if not exists
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

# Configure logging
logging.basicConfig(
    filename=f"{LOG_DIR}/interactions.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)
# clean logging output from dependencies
logging.getLogger("httpx").setLevel(logging.WARNING)
logging.getLogger("sentence_transformers").setLevel(logging.WARNING)

def log_event(event_type, data, session_id="default"):
    log_data = {
        "session_id": session_id,
        "event": event_type,
        "data": data
    }

    logging.info(json.dumps(log_data))