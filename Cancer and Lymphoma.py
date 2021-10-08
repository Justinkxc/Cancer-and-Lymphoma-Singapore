import requests
import matplotlib.pyplot as plt
import numpy as np

data = np.random.randn(50)

import pprint

pp = pprint.PrettyPrinter(indent=4)

# --Requesting data--#
cancer_data = requests.get(
    "https://data.gov.sg/api/action/datastore_search?resource_id=82a47c6d-0539-4f1d-bdf9-ff96b9ed6cf2&limit=30")
# print(cancer_data)
# print(cancer_data.text)

cancer_json = cancer_data.json()
print(pp.pprint(cancer_json))
print(cancer_json.keys())
print(len(cancer_json["result"]["records"]))

cancer_data = requests.get(
    "https://data.gov.sg/api/action/datastore_search?resource_id=82a47c6d-0539-4f1d-bdf9-ff96b9ed6cf2&limit=100")
cancer_json = cancer_data.json()

gender = {}
for record in cancer_json["result"]["records"]:
    sex = record["gender"]
    period = (record["start_of_period"], record["end_of_period"])
    cancer_type = record["type_of_cancer"]
    try:
        cancer_incidence = float(record["incidence_rate"])
    except:
        cancer_incidence = 0

    if sex not in gender:
        gender[sex] = {}

    if period not in gender[sex]:
        gender[sex][period] = {}

    gender[sex][period][cancer_type] = cancer_incidence

years_male = list(gender["male"].keys())
# print(years_male)
years_female = list(gender["female"].keys())
# print(years_female)

# ---Plotting for males---#

plt.style.use('seaborn')

# plot for males 2011 - 2015
data = gender["male"][years_male[0]]
plt.figure(figsize=(10, 5))
plt.bar(range(len(data)), data.values(), align='center')
plt.xticks(range(len(data)), list(data.keys()))
plt.title("Top 5 Leading Cancers for Males (2011-2015)")
plt.xlabel("Type of Cancer")
plt.ylabel("Incidence Rate (Per 100,000 per year)")
plt.show()
# plt.savefig("Male 2015", dpi=300)

# plot for males 2012 - 2016
data = gender["male"][years_male[1]]
plt.figure(figsize=(10, 5))
plt.bar(range(len(data)), data.values(), align='center')
plt.xticks(range(len(data)), list(data.keys()))
plt.title("Top 5 Leading Cancers for Males in (2012-2016)")
plt.xlabel("Type of Cancer")
plt.ylabel("Incidence Rate (Per 100,000 per year)")
plt.show()
# plt.savefig("Male 2016", dpi=300)

# plot for males 2013 - 2017
data = gender["male"][years_male[2]]
plt.figure(figsize=(10, 5))
plt.bar(range(len(data)), data.values(), align='center')
plt.xticks(range(len(data)), list(data.keys()))
plt.title("Top 5 Leading Cancers for Males in (2013-2017)")
plt.xlabel("Type of Cancer")
plt.ylabel("Age Standardised Incidence Rate (Per 100,000 per year)")
plt.show()
# plt.savefig("Male 2017", dpi=300)


# ---Plotting for lymphoma---#

lymphoma = []
lymphoma.append(gender["male"][years_male[0]]["lymphoid neoplasms"])
lymphoma.append(gender["male"][years_male[1]]["lymphoid neoplasms"])
lymphoma.append(gender["male"][years_male[2]]["lymphoid neoplasms"])

years = ["2011-2015", "2012-2016", "2013-2017"]
x = [0, 1, 2]

# lymphoma = dict(zip(years, lymphoma))

plt.style.use('seaborn')
plt.figure(figsize=(10, 5))
plt.title("Lymphoid Neoplasms")
plt.xlabel("Year")
plt.ylabel("Age Standardised Incidence Rate (Per 100,000 per year)")
plt.plot(lymphoma, ".-", label="lymphoid neoplasms")
plt.xticks(x, years)
plt.tight_layout()
plt.legend(loc='best')
plt.show()
# plt.savefig("lymphoma", dpi=300)

# ---Plotting for female---#

plt.style.use('ggplot')

# plot for females 2011 - 2015
data = gender["female"][years_female[0]]
plt.figure(figsize=(10, 5))
plt.bar(range(len(data)), data.values(), align='center')
plt.xticks(range(len(data)), list(data.keys()))
plt.title("Top 5 Leading Cancers for Males (2011-2015)")
plt.xlabel("Type of Cancer")
plt.ylabel("Age Standaradised Incidence Rate (Per 100,000 per year)")
plt.show()
# plt.savefig("female 2015", dpi=300)

# plot for males 2012 - 2016
data = gender["female"][years_female[1]]
plt.figure(figsize=(10, 5))
plt.bar(range(len(data)), data.values(), align='center')
plt.xticks(range(len(data)), list(data.keys()))
plt.title("Top 5 Leading Cancers for Males in (2012-2016)")
plt.xlabel("Type of Cancer")
plt.ylabel("Age Standardised Incidence Rate (Per 100,000 per year)")
plt.show()
# plt.savefig("female 2016", dpi=300)

# plot for males 2013 - 2017
data = gender["female"][years_female[2]]
plt.figure(figsize=(10, 5))
plt.bar(range(len(data)), data.values(), align='center')
plt.xticks(range(len(data)), list(data.keys()))
plt.title("Top 5 Leading Cancers for Males in (2013-2017)")
plt.xlabel("Type of Cancer")
plt.ylabel("Age Standardised Incidence Rate (Per 100,000 per year)")
plt.show()
# plt.savefig("female 2017", dpi=300)