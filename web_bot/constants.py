"""
Name: constants.py
Author: Almog Maimon
Purpose: The constants for the bot.
Date: 14/09/2022
"""

URL = "https://agendamentosonline.mne.gov.pt/AgendamentosOnline/index.jsf"
CONSOLE_PLACE = "Telaviv"
ORDER_CATEGORY = "identificação"

FOUND_NOTHING_TEXT = "De momento não existem vagas disponíveis, por favor tente mais tarde."


class Credentials:
    """The credentials we use for the order."""
    ID_NUMBER = 9099256779
    BIRTH_DATE = "17-11-1981"


class ElementsIDs:
    """The ids of elements in the web page."""
    COOKIES_DISABLE_BUTTON = "j_idt68"
    CLOSE_POPUP_BUTTON = "j_idt61"
    SCHEDULE_BUTTON = "indexForm:j_idt29"

    ID_NUMBER_INPUT = "ccnum"
    DATE_INPUT = "dataNascimento_input"

    SELECT_PLACE_BUTTON = "postcons"
    PLACE_DROPDOWN = "postcons_panel"

    SELECT_ORDER_CATEGORY = "categato"
    CATEGORY_DROPDOWN = "categato_panel"
    TYPE_FORM_BUTTON = "bAddAto"

    TERMS_AGREE_CHECKBOX = "selCond_input"
    SUBMIT_BUTTON = "bCal"
    GO_BACK_BUTTON = "j_idt174"

    RESULTS_DIV = "j_idt171"
