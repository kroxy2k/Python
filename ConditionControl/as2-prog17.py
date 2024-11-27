''' In a company, worker efficiency is determined on the basis of the time required for a worker
to complete a particular job. If the time taken by the worker is between 2-3 hours, then the
worker is said to be highly efficient. If the time required by the worker is between 3-4 hours,
then the worker is ordered to improve speed. If the time taken is between 4-5 hours, the
worker is given training to improve his speed, and if the time taken by the worker is more than 5 hours, then the worker has to leave the company. If the time taken by the worker is
input through the keyboard, find the efficiency of the worker.'''
# Input the time taken by the worker
ttime = float(input("Enter the time taken by the worker (in hours): "))

# Determine efficiency based on time taken
if 2 <= ttime <= 3:
    print("The worker is highly efficient.")
elif 3 < ttime <= 4:
    print("The worker is ordered to improve speed.")
elif 4 < ttime <= 5:
    print("The worker is given training to improve speed.")
elif ttime> 5:
    print("The worker has to leave the company.")
else:
    print("Invalid input. Time taken must be at least 2 hours.")
