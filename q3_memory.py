from typing import List, Tuple
import pandas as pd 
from collections import Counter
import re 

def q3_memory(df: pd.DataFrame) -> List[Tuple[str, int]]:
    """
    Memory-Optimized Solution: Finds the top 10 influential users based on mentions, minimizing memory usage.
    """
    # Extract mentions and count directly
    mention_pattern = re.compile(r'@\w+')
    mentions = df['content'].apply(lambda x: mention_pattern.findall(x))
    mention_counts = Counter(mentions.explode())
    
    # Get the top 10 mentions
    top_mentions = mention_counts.most_common(10)
    
    return top_mentions