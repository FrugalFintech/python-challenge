import csv
import os

# Same if loop as PyBank
filename="election_data.csv"
absolute_filepath=r"C:\Users\himyn\OneDrive\Desktop\Bootcamp\Projects\Week3_(Python)\Starter_Code\PyPoll\Resources"+"\\"+filename

if os.path.isfile(absolute_filepath):
    print("Hurray, you're in the right directory!")

    # Initialize variables & make dictionary
    total_votes = 0
    candidates = {}

    # Read file
    with open(absolute_filepath, newline="") as rawdata:
        reader = csv.reader(rawdata, delimiter=",")

        # Skip the header row
        header = next(reader)

        # Count votes for each candidate
        for row in reader:
            total_votes += 1
            candidate_name = row[2]

            # If candidate name in list, add to counter. If not, start new count
            if candidate_name in candidates:
                candidates[candidate_name] += 1
            else:
                candidates[candidate_name] = 1

    # Print the results
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {total_votes}")
    print("-------------------------")

    # Calculate and print results for each candidate
    for candidate, votes in candidates.items():
        percentage = (votes / total_votes) * 100
        print(f"{candidate}: {percentage:.3f}% ({votes})")

    print("-------------------------")

    # Find the winner based on popular vote
    winner = max(candidates, key=candidates.get)
    print(f"Winner: {winner}")

    # Save as a text file
    with open("election_results.txt", "w") as output_file:
        output_file.write("Election Results\n")
        output_file.write("-------------------------\n")
        output_file.write(f"Total Votes: {total_votes}\n")
        output_file.write("-------------------------\n")

        # Write results for each candidate to the file
        for candidate, votes in candidates.items():
            percentage = (votes / total_votes) * 100
            output_file.write(f"{candidate}: {percentage:.3f}% ({votes})\n")

        output_file.write("-------------------------\n")
        output_file.write(f"Winner: {winner}\n")
        
# Same else loop as PyBank
else:
    print("Error, the file is not in the right direcotry")
    exit()