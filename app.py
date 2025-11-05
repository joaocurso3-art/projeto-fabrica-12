import pandas as pd

df = pd.read_csv("Spotify_YouTube.csv")
print("Informações gerais do DataFrame:")
print(df.info())
print("\nValores ausentes por coluna:")
print(df.isna().sum())

print("\nCinco primeiras linhas do DataFrame:")
print(df.head())

artistas_unicos = df['Artist'].unique()
quantidade_artistas = df['Artist'].nunique()
print(f"\nQuantidade de artistas distintos: {quantidade_artistas}")
print(f"Exemplos de artistas únicos: {artistas_unicos[:10]}")

top_artistas_musicas = df['Artist'].value_counts().head(10)
print("\nTop 10 artistas com mais músicas:")
print(top_artistas_musicas)

top_musicas_views = df[['Artist','Track','Views']].sort_values(by='Views', ascending=False).head(5)
print("\nTop 5 músicas com mais views no YouTube:")
print(top_musicas_views)

top_artistas_streams = (
    df.groupby('Artist')['Stream']
    .sum()
    .sort_values(ascending=False)
    .head(5)
    .reset_index()
)
top_artistas_streams.columns = ['Artista', 'Total_Streams']
print("\nTop 5 artistas com mais streams no Spotify:")
print(top_artistas_streams)
