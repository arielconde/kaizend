import os

stage = os.environ['STAGE'].upper()
output = f"We're running in stage {stage}"

if stage.startswith("PROD"):
	output = "DANGER!!! - " + output

print(output)
