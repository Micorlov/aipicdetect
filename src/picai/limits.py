"""Numeric limits shared by the server and the public copy, so the two never drift."""

MAX_UPLOAD_MB = 50
MAX_UPLOAD_BYTES = MAX_UPLOAD_MB * 1024 * 1024
RESULT_CACHE_LIMIT = 100  # scrubbed results kept in memory; oldest evicted first
DEFAULT_DAILY_LIMIT = 10  # analyses per client IP in any rolling 24 h window; 0 disables
