import re

# Define regular expressions for each data type
regex_patterns = {
    "emails": r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
    "urls": r"https?:\/\/[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(\/\S*)?",
    "phone_numbers": r"(\(\d{3}\)\s?|\d{3}[.-]?)\d{3}[.-]?\d{4}",
    "credit_cards": r"(?:\d{4}[-\s]?){3}\d{4}",
    "time_formats": r"(1[0-2]|0?[1-9]):[0-5][0-9](\s?[APMapm]{2})?|([01]?[0-9]|2[0-3]):[0-5][0-9]",
    "html_tags": r"<[^>]+>",
    "hashtags": r"#[A-Za-z0-9_]+",
    "currency": r"\$\d{1,3}(,\d{3})*(\.\d{2})?"
}

# Function to find matches based on regex patterns
def extract_data(text, patterns):
    extracted_data = {}
    for data_type, pattern in patterns.items():
        extracted_data[data_type] = re.findall(pattern, text)
    return extracted_data

# Actual input string
sample_text = """
    Here are some emails: user@example.com, firstname.lastname@company.co.uk.
    URLs: https://www.example.com, http://subdomain.example.org/page.
    Phone numbers: (123) 456-7890, 123-456-7890, 123.456.7890.
    Credit card numbers: 1234 5678 9012 3456, 1234-5678-9012-3456.
    Time formats: 14:30, 2:30 PM.
    HTML tags: <p>, <div class="example">, <img src="image.jpg" alt="description">.
    Hashtags: #example, #ThisIsAHashtag.
    Currency: $19.99, $1,234.56.
"""

# Extract data from the sample text
extracted_data = extract_data(sample_text, regex_patterns)

# Print extracted data to console
for data_type, matches in extracted_data.items():
    if matches:
        print(f"{data_type.capitalize()} found: {matches}")
    else:
        print(f"{data_type.capitalize()} found: None")

# Write extracted data to a file
with open("extracted_data.txt", "w") as f:
    for data_type, matches in extracted_data.items():
        f.write(f"{data_type.capitalize()} found:\n")
        if matches:
            for match in matches:
                f.write(f"  - {match}\n")
        else:
            f.write("  - None\n")
        f.write("\n")

