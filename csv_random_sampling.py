import pandas as pd

input_file = "input.csv"
output_file = "output.csv"
sample_size = 47

features = pd.read_csv(input_file, usecols=['Properties', ' Sequence'])

df_sample = features.sample(sample_size)
df_sample.to_csv(output_file, index=False)