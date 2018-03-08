# Queries can be done at https://bigquery.cloud.google.com/dataset/fh-bigquery:reddit_posts
# First 1TB of data processing is free.

#standardSQL
SELECT title FROM `fh-bigquery.reddit_posts.2*` WHERE subreddit = 'MachineLearning' ORDER BY created_utc DESC LIMIT 10000 OFFSET 0
#standardSQL
SELECT title FROM `fh-bigquery.reddit_posts.2*` WHERE subreddit = 'MachineLearning' ORDER BY created_utc DESC LIMIT 10000 OFFSET 10000
#standardSQL
SELECT title FROM `fh-bigquery.reddit_posts.2*` WHERE subreddit = 'MachineLearning' ORDER BY created_utc DESC LIMIT 10000 OFFSET 20000
#standardSQL
SELECT title FROM `fh-bigquery.reddit_posts.full_corpus_201512` WHERE subreddit = 'MachineLearning' ORDER BY created_utc DESC LIMIT 10000 OFFSET 0
#standardSQL
SELECT title FROM `fh-bigquery.reddit_posts.full_corpus_201512` WHERE subreddit = 'MachineLearning' ORDER BY created_utc DESC LIMIT 10000 OFFSET 10000
