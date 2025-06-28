import subprocess

# Get system infromation using uname
result= subprocess.run(['uname','-a'],capture_output=True, text=True)
print(f"Kernel information: {result.stdout.strip()}")

#List running process using ps
result = subprocess.run(['ps','aux'], capture_output=True,text=True)
print(f"Running process:\n{result.stdout}")
