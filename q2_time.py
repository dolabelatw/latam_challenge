import re
from collections import Counter
import pandas as pd
from typing import List, Tuple

def q2_time(df: pd.DataFrame) -> List[Tuple[str, int]]:
    """
    Time-Optimized Solution: Finds the top 10 most used emojis, minimizing execution time.
    """
    # Define regex pattern for capturing only emojis
    emoji_pattern = re.compile(
        r'[\U0001F600-\U0001F64F'  # Emoticons
        r'\U0001F300-\U0001F5FF'   # Symbols & Pictographs
        r'\U0001F680-\U0001F6FF'   # Transport & Map Symbols
        r'\U0001F1E0-\U0001F1FF'   # Flags (iOS)
        r'\U00002702-\U000027B0'   # Dingbats
        r'\U000024C2-\U0001F251'   # Enclosed characters
        r'\U0001F900-\U0001F9FF'   # Supplemental Symbols and Pictographs
        r'\U0001FA70-\U0001FAFF'   # Symbols and Pictographs Extended-A
        r'\U00002600-\U000026FF'   # Miscellaneous Symbols
        r'\U0001F700-\U0001F77F'   # Alchemical Symbols
        r'\U00002000-\U000027BF]+',  # Other symbols
        flags=re.UNICODE
    )

    # Extract emojis from text using the refined regex pattern
    emojis = df['content'].apply(lambda x: emoji_pattern.findall(x)).explode()
    
    # Count emojis and get the top 10
    emoji_counts = Counter(emojis)
    top_emojis = emoji_counts.most_common(10)
    
    return top_emojis
