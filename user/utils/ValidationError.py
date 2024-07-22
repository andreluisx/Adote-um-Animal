import re

def validate_cpf(cpf):
    cpf = re.sub(r'\D', '', cpf)
    if len(cpf) != 11 or not cpf.isdigit():
        return False

    
    if cpf in [str(i) * 11 for i in range(10)]:
        return False

    for i in range(9, 11):
        value = sum((int(cpf[num]) * ((i+1) - num) for num in range(0, i)))
        check_digit = ((value * 10) % 11) % 10
        if check_digit != int(cpf[i]):
            return False

    return True

def extract_numbers(input_string):
    numbers = re.findall(r'\d+', input_string)
    return ''.join(numbers)

def validate_email(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

def validate_state(state):
    valid_states = [
        'AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ',
        'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO'
    ]
    return state in valid_states

def validate_phone_number(number):
    pattern = re.compile(r'^\(?\d{2}\)?[\s-]?\d{4,5}-?\d{4}$')
    return pattern.match(number)