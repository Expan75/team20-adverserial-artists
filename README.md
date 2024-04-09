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

2. Install dependencies

```bash
# create a virtualenv in project directory
python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt
```

3. see notebooks/getting-started.ipynb

```bash
python3 -m jupyter notebook notebooks/getting-started.ipynb
```

## Code quality and style

The repository has a little CI/CD line that will run tests (see common/test_example). There's also a linter to ensure we follow the pep8 style guide. This will not be the case for notebooks. If your push or merge request blocked by the [workflow](https://github.com/Expan75/team20-adverserial-artists/actions) you'll see red.

### Passing the lint check

```bash
# lint and get notified of any lines that conflict with ruleset
python3 -m flake8 common/

# in most cases you can just run the autoformatter to have things taken care of
python3 -m black common/
```

### Passing the test check

```bash
# run all tests
python3 -m pytest

# alternatively run a test by matching the test function name(s)
python3 -m pytest -k test_very_specific_name

# you can also invert these patterns by adding "not" in front
python3 -m pytest -k not e2e
```

Once your test pass locally, you can commit and push the updated version which should now clear the CI/CD pipeline.
