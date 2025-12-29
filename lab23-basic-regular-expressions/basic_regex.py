import re

# Compile a regex pattern to match digits
pattern = re.compile(r"\d+")

test_string = "The rainfall 2021 was greater than 2019 and 2020 combined."

# Find all matches
matches = pattern.findall(test_string)
print("Matches found:", matches)

# Replace digits with placeholder
replaced_string = pattern.sub("XXXX", test_string)
print("Replaced String:", replaced_string)

# Regex groups for dates
date_pattern = re.compile(r"(\d{4})-(\d{2})-(\d{2})")

date_string = "Date of birth: 1990-08-15 and starting date 2020-01-01."

date_matches = date_pattern.findall(date_string)
print("Date Matches:", date_matches)

# Named groups
named_date_pattern = re.compile(
    r"(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})"
)

for match in named_date_pattern.finditer(date_string):
    print(
        "Year:", match.group("year"),
        "Month:", match.group("month"),
        "Day:", match.group("day")
    )
