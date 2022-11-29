import pandas as pd

papers = 'papers001.csv'
links = 'links001.csv'

papers_frame = pd.read_csv(papers, sep=';', index_col='id')
papers_frame = papers_frame.set_index('title')

print(papers_frame)

links_frame = pd.read_csv(links, sep=';', index_col='paper_id')
links_frame = links_frame.assign(num=1).groupby('reference').sum()
links_frame.index.rename('title', inplace=True)

print(links_frame)

papers_frame = pd.merge(papers_frame, links_frame, on='title')

print(papers_frame)
