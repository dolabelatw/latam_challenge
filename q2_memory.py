import re
from collections import Counter
import pandas as pd
from typing import List, Tuple


def q2_memory(df: pd.DataFrame) -> List[Tuple[str, int]]:
    """
    Memory-Optimized Solution: Finds the top 10 most used emojis, minimizing memory usage.
    """
    # Use the refined regex pattern for capturing only emojis
    emoji_pattern = re.compile(
        r'[\U0001F600-\U0001F64F'
        r'\U0001F300-\U0001F5FF'
        r'\U0001F680-\U0001F6FF'
        r'\U0001F1E0-\U0001F1FF'
        r'\U00002702-\U000027B0'
        r'\U000024C2-\U0001F251'
        r'\U0001F900-\U0001F9FF'
        r'\U0001FA70-\U0001FAFF'
        r'\U00002600-\U000026FF'
        r'\U0001F700-\U0001F77F'
        r'\U00002000-\U000027BF]+', 
        flags=re.UNICODE
    )

    # Extract emojis and count directly
    emojis = df['content'].apply(lambda x: emoji_pattern.findall(x))
    emoji_counts = Counter(emojis.explode())
    
    # Get the top 10 emojis
    top_emojis = emoji_counts.most_common(10)
    return top_emojis