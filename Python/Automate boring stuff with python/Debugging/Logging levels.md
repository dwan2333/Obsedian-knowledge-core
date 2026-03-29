```python fold:Logging_levels
import logging

logging.basicConfig(
    level=logging.DEBUG,    # capture DEBUG and above
    format="%(levelname)s : %(message)s"
)

logging.debug("This is a debug message")       # shown
logging.info("Informational message")          # shown
logging.warning("A warning occurred")          # shown
logging.error("An error happened!")            # shown
logging.critical("Critical issue!")            # shown

```