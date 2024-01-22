import logging
from datetime import datetime

import pytz # $ pip install pytz


timezone_paris = pytz.timezone('Europe/Paris')

current_time = datetime.now(timezone_paris)

current_time_formatted = current_time.strftime("%H:%M:%S")

print(current_time_formatted)

logging.basicConfig(filename=None, encoding='utf-8', level=logging.DEBUG)

logging.info(f"Lancement du traitement")

logging.debug(f"Demande d'heure sur le timezone : {timezone_paris}")

if timezone_paris is None:

    logging.error("aucune timezone n'a été renseignée")

    raise ValueError("aucune timezone n'a été renseignée")