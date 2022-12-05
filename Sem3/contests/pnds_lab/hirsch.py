import pandas as pd

papers = input()
links = input()

papers_frame = pd.read_csv(papers, sep=';', index_col='id')
papers_frame = papers_frame.set_index('title')
author_frame = papers_frame.assign(num_of_papers=1).groupby('author').sum()

links_frame = pd.read_csv(links, sep=';', index_col='paper_id')
links_frame = links_frame.assign(num_of_citations=1).groupby('reference').sum()
links_frame.index.rename('title', inplace=True)

papers_frame = pd.merge(papers_frame, links_frame, on='title')

author_frame = pd.merge(author_frame, papers_frame.groupby('author').sum(), on='author')
author_frame['hirsch_rate'] = author_frame['num_of_citations'] / author_frame['num_of_papers']
author_frame = author_frame.sort_values(by='hirsch_rate', ascending=False)

for i in range(3):
    print(author_frame.index[i] + ' ' + "%.3f" % author_frame.iloc[i, 2])
