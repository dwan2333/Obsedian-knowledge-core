```python fold:Logging_disable
import logging

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s:%(message)s")

logging.debug("Debug before disable")    # → shown
logging.info("Info before disable")      # → shown

# Disable all messages at INFO and lower (DEBUG and INFO)
logging.disable(logging.INFO)

logging.debug("Debug after disable")     # → NOT shown
logging.info("Info after disable")       # → NOT shown
logging.warning("Warning after disable") # → shown (WARNING > INFO)

# To re-enable everything again:
logging.disable(logging.NOTSET)
logging.debug("Debug re-enabled")        # → shown

```