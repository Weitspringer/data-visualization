from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
data = pd.read_csv('./data/MNIST-Fashion.csv')
unlabeled_data = data.drop(['label'], axis=1)
labels = data['label']

# Perform PCA on MNIST dataset
explained_variance = .95
pca = PCA(explained_variance)
lower_dim_data = pca.fit_transform(unlabeled_data)
approximation = pca.inverse_transform(lower_dim_data)

# Create t-SNE with parameters
tsne = TSNE(n_components=2,
            n_iter=1000,
            perplexity=10,
            method='barnes_hut',
            init='random',
            random_state=0,
            n_jobs=-1)
# Perform t-SNE
tsne_result = tsne.fit_transform(approximation)

# Draw result
tsne_result_df = pd.DataFrame({'tsne_1': tsne_result[:,0], 'tsne_2': tsne_result[:,1], 'label': labels})
fig, ax = plt.subplots(1)
sns.scatterplot(x='tsne_1', y='tsne_2', hue='label', palette='deep', data=tsne_result_df, ax=ax, s=120, linewidth=0)
lim = (tsne_result.min()-5, tsne_result.max()+5)
ax.set_xlim(lim)
ax.set_ylim(lim)
ax.set_aspect('equal')
ax.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.0)
plt.show()