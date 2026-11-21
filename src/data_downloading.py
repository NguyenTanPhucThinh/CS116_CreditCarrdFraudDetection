import kagglehub

kagglehub.login() 
# Download latest version
path = kagglehub.competition_download('playground-series-s6e11', output_dir='data')

print("Path to competition files:", path)