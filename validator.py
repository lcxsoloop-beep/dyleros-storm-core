def validate_numbers(leads, api_key):
    # Dummy validation
    return [lead for lead in leads if lead['phone'].startswith('+1')]
