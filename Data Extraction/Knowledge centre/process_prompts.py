import re

input_sets = []
target_sets = []

with open('train_P36_capital.txt', encoding = 'utf-8') as file:
    lines = file.read().split('\n\n')  # Split the file into sets based on blank lines

for set_text in lines:
    set_lines = set_text.split('\n')  # Split the set into lines
    inputs = ""
    targets = ""
    for line in set_lines:
        if line.startswith("inputs="):
            inputs = line[7:]  # Remove "inputs=" prefix
        elif line.startswith("targets="):
            targets = line[8:]  # Remove "targets=" prefix
    
    # Check if inputs contain exactly one "SUBJ" and one "OBJ"
    if inputs.count("SUBJ{") == 1 and inputs.count("OBJ{") == 1:
        input_sets.append(inputs)
        target_sets.append(targets)

input_sets_copy = input_sets.copy()

# Create a list to store indices of elements to remove
indices_to_remove = []

for i in range(len(input_sets_copy)):
    input_string = input_sets_copy[i]

    if re.search(r"(OBJ\{SUBJ\{)|(SUBJ\{OBJ\{)", input_string):
        indices_to_remove.append(i)
        continue

    # Define a regular expression pattern to match text inside SUBJ{} and OBJ{}.
    pattern1 = r"(SUBJ\{(.*?)\}.*?OBJ\{(.*?)\})"
    pattern2 = r"(OBJ\{(.*?)\}.*?SUBJ\{(.*?)\})"
    
    # Use re.search to find the pattern in the input string.
    match1 = re.search(pattern1, input_string)
    match2 = re.search(pattern2, input_string)

    if match1:
        subj_text = match1.group(2)
        obj_text = match1.group(3)
        input_sets[i] = f"The capital of {subj_text} is {obj_text}"
    elif match2:
        obj_text = match2.group(2)
        subj_text = match2.group(3)
        input_sets[i] = f"The capital of {subj_text} is {obj_text}"
    else:
        print("NULLLLL")

# Remove elements in reverse order to avoid index issues
for index in reversed(indices_to_remove):
    del input_sets[index]




# Write the extracted sets to a new file
with open('processed_train_P36_capital.txt', 'w', encoding = 'utf-8') as output_file:
    for inputs, targets in zip(input_sets, target_sets):
        set_text = f'inputs={inputs}\n' + f'targets={targets}\n\n'
        output_file.write(set_text)

print("Extraction complete. Results written to 'processed_train_P36_capital.txt'.")



