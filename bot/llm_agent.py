from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def think(market, memory_text=""):
    prompt = f"""
あなたはプロのBTCデイトレーダー。

市場:
価格: {market['price']}
出来高: {market['volume']}

過去の反省:
{memory_text}

以下を出力:
1. 市場状態
2. 短期予測（上/下/横）
3. 行動（BUY/SELL/WAIT）
4. 自信(0-100)
5. 理由
"""

    res = client.chat.completions.create(
        model="gpt-5-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
    )

    return res.choices[0].message.content
