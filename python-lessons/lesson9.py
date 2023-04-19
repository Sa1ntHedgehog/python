from datetime import datetime
import time
seconds=2400150
days = seconds // (24 * 3600)
seconds %= 24 * 3600
hours = seconds // 3600
seconds %= 3600
minutes = seconds // 60
seconds %= 60
print(f'{days}:{hours}:{minutes}:{seconds}')