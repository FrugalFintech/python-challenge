# Calling python csv & os modules
import csv
import os

# I had trouble uploading the document, so I made a code to check the filepath first

# This is for filename; to make the code reusable (as long in same directory)
filename="budget_data.csv"

# Specify the absolute filepath with the filename concatenated at the end
absolute_filepath=r"C:\Users\himyn\OneDrive\Desktop\Bootcamp\Projects\Week3_(Python)\Starter_Code\PyBank\Resources"+"\\"+filename
 #There's also an option for os.path.join to make more robust

# If loop to check if the file is in the working directory; all code operates under it
if os.path.isfile(absolute_filepath):
    print("Hurray, you're in the right directory!")

    # Initialize variables: Set all var to 0 & make empty lists
    total_months = 0
    net_total = 0
    old_profit_loss = 0
    change_list = []
    date_list = []

    # Read the csv file data file
    with open(absolute_filepath, newline="") as budget_data:
        rawdata = csv.reader(budget_data, delimiter=",")

        # Skip the header row
        header = next(rawdata)

        # Loop through the rows in the data
        for row in rawdata:
            # Actually read the data
            date = row[0]
            profit_loss = int(row[1])

            # Total months is the row counter
            total_months += 1

            # Net total is the running sum
            net_total += profit_loss

            # If loop for rows after first month
            if total_months > 1:
            # Calculate the change & add it to the list
                change = profit_loss - old_profit_loss
                change_list.append(change)
                date_list.append(date)

            # Update profit/lost for next loop 
            old_profit_loss = profit_loss

    # Average change = sum of difference/the # of variables in list(count)
    average_change = sum(change_list) / len(change_list)

    # Find the greatest increase and decrease in profits
    greatest_increase = max(change_list)
    greatest_increase_date = date_list[change_list.index(greatest_increase)]  # Corresponding date

    greatest_decrease = min(change_list)
    greatest_decrease_date = date_list[change_list.index(greatest_decrease)]
    # Print results
    print("Financial Analysis")
    print("-------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${net_total}")
    print(f"Average Change: ${round(average_change, 2)}")
    print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
    print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")

    #Export text file
    with open("financial_analysis.txt", "w") as text_file:
        text_file.write("Financial Analysis\n")
        text_file.write("-------------------------\n")
        text_file.write(f"Total Months: {total_months}\n")
        text_file.write(f"Total: ${net_total}\n")
        text_file.write(f"Average Change: ${round(average_change, 2)}\n")
        text_file.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n")
        text_file.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n")
# This is from the intial if loop, let me know the filepath is buggy
else:
    print("Error, the file is not in the right direcotry")
    exit()


    