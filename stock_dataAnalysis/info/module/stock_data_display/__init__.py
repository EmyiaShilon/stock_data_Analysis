from flask import Blueprint

stock_data_display = Blueprint('stock_data_dispaly', __name__,)

from . import views