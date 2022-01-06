from flask import Blueprint, Response, jsonify
from .database import get_last_n_records
import json

bp = Blueprint('history', __name__, url_prefix='/history')

@bp.route('/<int:count>', methods=['GET'])
def get_history(count: int):
    history = {
        'count': 0,
        'items': []
    }
    if count > 0:
        results = get_last_n_records(count)
        history['count'] = len(results)
        for row in results:
            history['items'].append({'index': row.index, 'value': row.value})
    return jsonify(history)