# team20-adverserial-artists

Team11:

<ul>
    <li>Emily Blixt</li>
    <li>Andreas Führ</li>
    <li>Erik Håkansson</li>
    <li>Lisa Lövgren</li>
    <li>Filip Olsson</li>
</ul>

Project structure

```bash
.
├── LICENSE
├── README.md           # all documentation
├── common              # importable custom python
└── notebooks           # all jupyter notebooks
```

Note that data is not stored in the repository, use google drive to gain access to the dataset and you can import it directly from a Collab loaded notebook.

## Roadmap

- [ ] Obtain dataset and produce extendable and importable code for loading it
- [ ] Basic exploratory data analysis (EDA) about underlying dataset
- [ ] Implement a baseline CNN as discriminator classifier (not trainable, resnet would be good baseline)
- [ ] Implement an image generation network (stable diffusion etc.) for introducing invisble noise
- [ ] Explore alternative models, data augmentation, and human evaluation etc.
- [ ] Results of experiments, including plots and draft write up.
- [ ] Write up about conslusions

All info that should go into the report should be generated with notebooks and then exported to the main overleaf document.

## Getting Started

1. Clone the repository to your machine

```bash
# via ssh
git clone git@github.com:Expan75/team20-adverserial-artists.git

# via https
git clone https://github.com/Expan75/team20-adverserial-artists
```

2. see notebooks/getting-started.ipynb

```bash
python3 -m jupyter notebook notebooks/getting-started.ipynb
```
