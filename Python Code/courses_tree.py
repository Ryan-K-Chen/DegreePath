import json


courses = {}
with open('courses_dictionary.json') as json_file:
    courses = json.load(json_file)

existing_dep = []

akash_dict = {}
akash_dict['courses_tree'] = []
# ece2020 = {}
# ece2020['department'] = 'ece'
# ece2020['number'] = '2020'
# akash_dict['courses_tree'].append(ece2020)


for key, value in courses.items():
    dep = courses[key]['Department']
    if dep in existing_dep:
        pass
    else:
        akash_dict['courses_tree'].append({'title': dep, 'value': dep, 'children': [], 'selectable': False})
        existing_dep.append(dep)

    for index, value in enumerate(akash_dict['courses_tree']):
        if dep == akash_dict['courses_tree'][index]['title']:
            indexOfDep = index


    akash_dict['courses_tree'][indexOfDep]['children'].append({'title': courses[key]['Department'] + ' ' + courses[key]['Course Number'], 'value': courses[key]['Department'] + ' ' + courses[key]['Course Number']})




indentedDictionary = json.dumps(akash_dict, indent=4)
print(indentedDictionary) ## prints out each entry in the dictionary

## Exports the courses dictionary as a json file
with open('courses_tree.json', 'w') as json_file:
    json.dump(akash_dict, json_file, indent=4)