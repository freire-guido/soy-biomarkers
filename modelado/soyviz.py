import matplotlib.pyplot as plt
from sklearn import manifold

def plot_los_tres(X, condicion, sra, fig = None, ax = None):
    tsne = manifold.TSNE()
    X_tsne = tsne.fit_transform(X)
    if not fig and not ax:
        fig, ax = plt.subplots(1, 3, figsize=(20,5))
    artists = []
    for bioproject in sra['bioproject'].unique():
        artists.append(ax[0].scatter(X_tsne[sra['bioproject'] == bioproject, 0], X_tsne[sra['bioproject'] == bioproject, 1], alpha=0.5, label=condicion))
        ax[0].set_title('bioproject')
    for tejido in condicion['tejido'].unique():
        artists.append(ax[1].scatter(X_tsne[condicion['tejido'] == tejido, 0], X_tsne[condicion['tejido'] == tejido, 1], alpha=0.5, label=tejido))
        ax[1].set_title('tejido')
        ax[1].legend()
    for estres in condicion['estres'].unique():
        artists.append(ax[2].scatter(X_tsne[condicion['estres'] == estres, 0], X_tsne[condicion['estres'] == estres, 1], alpha=0.5, label=estres))
        ax[2].set_title('estres')
        ax[2].legend()
    return artists