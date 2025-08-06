def scrape_fsbo_by_zip(zips):
    # Dummy data for testing
    dummy_leads = []
    for zip_code in zips:
        dummy_leads.append({
            'name': 'John Doe',
            'phone': '+1234567890',
            'address': '123 Example St',
            'zip': zip_code.strip()
        })
    return dummy_leads
