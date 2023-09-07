import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
from matplotlib.colors import LogNorm, Normalize
# %matplotlib inline

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

file_name = "SPC_TRADE_FOOD.csv"
file_path = "data/SPC/"

# Open CSV file in pandas
df_raw = pd.read_csv(file_path + file_name)

#########################
##### MISE EN FORME #####
#########################

# Get column name
df_column_name = list(df_raw.columns.values)
# for el in df_column_name:
#     print(el)

# Get unique value of each column
# for el in df_column_name:
#     print(el)
#     print(df_raw[el].unique())

# Suppression des colonnes non utiles pour l'analyse (mono valeur ou vide)
df_net = df_raw.drop(columns=['DATAFLOW', 'FREQ: Frequency', 'INDICATOR: Indicator', 'UNIT_MULT: Unit multiplier',
                              'OBS_STATUS: Observation Status', 'DATA_SOURCE: Data source', 'OBS_COMMENT: Comment', 'UNIT_MEASURE: Unit of measure', 'EXPORTER: Exporter'])

# Renommer les colonnes
df_net = df_net.rename(columns={'IMPORTER: Importer': 'IMPORTATEURS',
                                'COMMODITY: Commodity': 'PRODUITS',
                                'TIME_PERIOD: Time': 'ANNEE',
                                'OBS_VALUE': 'VALEUR_T'
                                })

# print(df_net.head())

#########################
##### ANALYSE #####
#########################
# df_TF_1 = df_net.groupby('IMPORTATEURS').agg(
#     {'VALEUR_T': 'sum'}).sort_values('VALEUR_T', ascending=False)

# total_import_ton = df_net['VALEUR_T'].sum()

# df_TF_1['PCT_VALEUR_T'] = round(df_TF_1['VALEUR_T']*100/total_import_ton, 2)
# df_TF_1['PCT_VALEUR_T_CUMSUM'] = round(df_TF_1['PCT_VALEUR_T'].cumsum(), 2)

# print(total_import_ton)

# # Graphique GTF_1
# graph_title = "FOOD TRADE - Répartition quantité importée totale par pays de 1995 à 2018"
# title_family = 'serif'  # 'serif' | 'sans-serif' | 'cursive' | 'fantasy' | 'monospace'
# title_color = 'midnightblue'
# # 'normal' | 'bold' | 'heavy' | 'light' | 'ultrabold' | 'ultralight'
# title_weight = 'bold'
# title_size = 14
# title_x = 0.5
# title_y = 1

# fig, axe1 = plt.subplots(nrows=1, ncols=1, figsize=(20, 10), sharex=True)
# axe1.set_title(graph_title, x=title_x, y=title_y, fontdict={
#                'family': title_family, 'color': title_color, 'weight': title_weight, 'size': title_size})


# def autopct_tunning(p): return '{:1.1f}%'.format(p) if p > 1 else None


# axe1.pie(df_TF_1['PCT_VALEUR_T'],
#          labels=[x if df_TF_1.loc[df_TF_1.index.values == x, 'PCT_VALEUR_T'].iloc[0] > 1 else '' for x in df_TF_1.index.values], autopct=autopct_tunning, textprops={'fontsize': 8},)

# # axe1.legend(loc="center", bbox_to_anchor=(0, 0, 0, 0),
# #             ncol=2, fancybox=True, shadow=True)

# plt.show()
############################################################
# df_TF_2 = df_net.groupby('PRODUITS').agg(
#     {'VALEUR_T': 'sum'}).sort_values('VALEUR_T', ascending=False)

# total_produit_ton = df_net['VALEUR_T'].sum()

# df_TF_2['PCT_VALEUR_T'] = round(df_TF_2['VALEUR_T']*100/total_produit_ton, 2)
# df_TF_2['PCT_VALEUR_T_CUMSUM'] = round(df_TF_2['PCT_VALEUR_T'].cumsum(), 2)

# print(df_TF_2)

# # Graphique GTF_2
# graph_title = "FOOD TRADE - Quantité exportée vers les iles du pacifique par produits de 1995 à 2018"
# title_family = 'serif'  # 'serif' | 'sans-serif' | 'cursive' | 'fantasy' | 'monospace'
# title_color = 'midnightblue'
# # 'normal' | 'bold' | 'heavy' | 'light' | 'ultrabold' | 'ultralight'
# title_weight = 'bold'
# title_size = 14
# title_x = 0.5
# title_y = 1

# fig, axe1 = plt.subplots(nrows=1, ncols=1, figsize=(20, 10), sharex=True)
# axe1.set_title(graph_title, x=title_x, y=title_y, fontdict={
#                'family': title_family, 'color': title_color, 'weight': title_weight, 'size': title_size})

# axe1.barh(df_TF_2.index.values, df_TF_2['VALEUR_T'], align='center')
# axe1.set_xlabel('Millions de tonnes')

# fig.subplots_adjust(left=0.4)
# axe1.grid(True, alpha=0.3)
# plt.show()
############################################################

df_TF_3 = df_net.groupby(['PRODUITS', 'IMPORTATEURS'],
                         as_index=False).agg({'VALEUR_T': 'sum'})
df_TF_3_pivot = df_TF_3.pivot_table(
    columns='IMPORTATEURS', index='PRODUITS', values='VALEUR_T')
df_TF_3_pivot.loc[:, 'Row_Total'] = df_TF_3_pivot.sum(
    numeric_only=True, axis=1)
df_TF_3_pivot = df_TF_3_pivot.sort_values(by=['Row_Total'], ascending=False)
df_TF_3_pivot = df_TF_3_pivot[df_TF_3_pivot.sum(
).sort_values(ascending=False).index]
df_TF_3_pivot = df_TF_3_pivot.iloc[:, :].apply(lambda x: x / x.sum())

print(df_TF_3_pivot)


sns.heatmap(df_TF_3_pivot, square=True, norm=LogNorm())
plt.show()
