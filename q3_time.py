from typing import List, Tuple
import pandas as pd 
import re
from collections import Counter
from typing import List, Tuple

def q3_time(df: pd.DataFrame) -> List[Tuple[str, int]]:
    """
    Time-Optimized Solution: Finds the top 10 influential users based on mentions, minimizing execution time.
    """
    # Extract mentions from text using regex
    mention_pattern = re.compile(r'@\w+')
    mentions = df['content'].apply(lambda x: mention_pattern.findall(x)).explode()
    
    # Count mentions and get the top 10
    mention_counts = Counter(mentions)
    top_mentions = mention_counts.most_common(10)
    
    return top_mentions