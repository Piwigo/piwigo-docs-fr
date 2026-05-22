# Documentation de Piwigo

## Building the site

Install zensical :

```bash
# Create a virtual environement in python
python3 -m venv .venv
source .venv/bin/activate
pip install zensical
```

Test Locally :

```bash
zensical serve # test locally
zensical build # build static site
```