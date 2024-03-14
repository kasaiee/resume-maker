def get_form_set_keys(request):
    form_set_keys = [k for k in request.POST if k.startswith('form-')]
    unique_indexes = list({k.split('-')[1] for k in form_set_keys})
    unique_indexes.sort()
    return unique_indexes


def get_form_set_values(request, key):
    data = request.POST
    prefix = f'form-{key}'
    return {
        'title': data[f'{prefix}-title'],
        'description': data[f'{prefix}-description'],
        'employer': data[f'{prefix}-employer'],
        'employee_start_date': data[f'{prefix}-employee_start_date'],
        'employee_end_date': data[f'{prefix}-employee_end_date'],
    }