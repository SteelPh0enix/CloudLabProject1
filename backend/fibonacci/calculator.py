from flask import Blueprint, jsonify 
from .database import add_or_update_fibonacci_record, get_value_on_index

bp = Blueprint('calculator', __name__, url_prefix='/calculate')

def calculate_fibonacci(value: int) -> int:
    if value <= 0:
        return 0
    if value == 1:
        return 1
    return calculate_fibonacci(value - 1) + calculate_fibonacci(value - 2)

@bp.route('/<int:number>', methods=['GET'])
def calculate(number: int):
    if number < 50:
        record = get_value_on_index(number)
        value = 0
        if record is not None:
            value = record.value
        else:
            value = calculate_fibonacci(number)
        add_or_update_fibonacci_record(number, value)
        return jsonify(requested=number, value=value, requested_value_too_big=False)
    else:
        return jsonify(requested=number, value=0, requested_value_too_big=True)