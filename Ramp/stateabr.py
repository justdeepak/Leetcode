import json


class StateName:
    def __init__(self):
        f = open('convert.json')
        self.data = json.load(f)
        f.close()
        self.stateList = abbrev2state = {
                'AK': 'Alaska',
                'AL': 'Alabama',
                'AR': 'Arkansas',
                'AZ': 'Arizona',
                'CA': 'California',
                'CO': 'Colorado',
                'CT': 'Connecticut',
                'DC': 'District of Columbia',
                'DE': 'Delaware',
                'FL': 'Florida',
                'GA': 'Georgia',
                'HI': 'Hawaii',
                'IA': 'Iowa',
                'ID': 'Idaho',
                'IL': 'Illinois',
                'IN': 'Indiana',
                'KS': 'Kansas',
                'KY': 'Kentucky',
                'LA': 'Louisiana',
                'MA': 'Massachusetts',
                'MD': 'Maryland',
                'ME': 'Maine',
                'MI': 'Michigan',
                'MN': 'Minnesota',
                'MO': 'Missouri',
                'MS': 'Mississippi',
                'MT': 'Montana',
                'NC': 'North Carolina',
                'ND': 'North Dakota',
                'NE': 'Nebraska',
                'NH': 'New Hampshire',
                'NJ': 'New Jersey',
                'NM': 'New Mexico',
                'NV': 'Nevada',
                'NY': 'New York',
                'OH': 'Ohio',
                'OK': 'Oklahoma',
                'OR': 'Oregon',
                'PA': 'Pennsylvania',
                'RI': 'Rhode Island',
                'SC': 'South Carolina',
                'SD': 'South Dakota',
                'TN': 'Tennessee',
                'TX': 'Texas',
                'UT': 'Utah',
                'VA': 'Virginia',
                'VT': 'Vermont',
                'WA': 'Washington',
                'WI': 'Wisconsin',
                'WV': 'West Virginia',
                'WY': 'Wyoming',
                'PR': 'Puerto Rico',
                'VI': 'Virigin Islands'
            }
        
    def replaceStateName(self, abbreviation, stateName):
        for i in self.data:
            if(i["state"] == abbreviation):
                i["stateCode"] = i["state"]
                i["state"] = stateName


if __name__ == "__main__":
    stateName = StateName()
    for abr in stateName.stateList:
        stateName.replaceStateName(abr, stateName.stateList[abr])

    print(stateName.data)