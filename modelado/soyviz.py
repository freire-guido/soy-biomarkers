import matplotlib.pyplot as plt
from sklearn import manifold

def plot_los_tres(X, annot, fig = None, ax = None):
    tsne = manifold.TSNE()
    X_tsne = tsne.fit_transform(X)
    if not fig and not ax:
        fig, ax = plt.subplots(1, 3, figsize=(20,5))
    artists = []
    for bioproject in annot['bioproject'].unique():
        artists.append(ax[0].scatter(X_tsne[annot['bioproject'] == bioproject, 0], X_tsne[annot['bioproject'] == bioproject, 1], alpha=0.5, label=annot))
        ax[0].set_title('bioproject')
    for tejido in annot['tejido'].unique():
        artists.append(ax[1].scatter(X_tsne[annot['tejido'] == tejido, 0], X_tsne[annot['tejido'] == tejido, 1], alpha=0.5, label=tejido))
        ax[1].set_title('tejido')
        ax[1].legend()
    for estres in annot['estres'].unique():
        artists.append(ax[2].scatter(X_tsne[annot['estres'] == estres, 0], X_tsne[annot['estres'] == estres, 1], alpha=0.5, label=estres))
        ax[2].set_title('estrés')
        ax[2].legend()
    return artists

def plot_estres(X, annot, legend = True):
    tsne = manifold.TSNE()
    X_tsne = tsne.fit_transform(X)
    fig, ax = plt.subplots(1, 1, figsize=(6,6))
    for estres in annot['estres'].unique():
        artist = ax.scatter(X_tsne[annot['estres'] == estres, 0], X_tsne[annot['estres'] == estres, 1], alpha=0.5, label=estres)
        if legend:
            ax.legend()
    return artist