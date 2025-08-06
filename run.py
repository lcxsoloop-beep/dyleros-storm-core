import json
from fsbo_scraper import scrape_fsbo_by_zip
from validator import validate_numbers

def load_config():
    with open('config.json') as f:
        return json.load(f)

def save_leads(leads, filename='leads_verified.csv'):
    with open(filename, 'w') as f:
        f.write('Name,Phone,Address,Zip\n')
        for lead in leads:
            f.write(f"{lead['name']},{lead['phone']},{lead['address']},{lead['zip']}\n")

def main():
    config = load_config()
    zips = input("Enter comma-separated ZIP codes (e.g., 76179,90210): ").split(',')
    print("\n[+] Scraping FSBO.com for ZIPs...\n")
    raw_leads = scrape_fsbo_by_zip(zips)

    print(f"[+] Scraped {len(raw_leads)} leads. Validating...\n")
    verified_leads = validate_numbers(raw_leads, config['clearout_api_key'])

    print(f"[+] {len(verified_leads)} leads verified. Saving to CSV...\n")
    save_leads(verified_leads)
    print("\n✅ leads_verified.csv generated. Upload this to GHL to start your outreach.\n")

if __name__ == '__main__':
    main()
