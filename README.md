# Activity Browser packaging and recipe files

This repository will contain recipes and blueprints to bundle or package
the Activity Browser code and allow for a much simpler way of distribution.

## Conda recipe

A conda recipe (`meta.yaml`) file that is slightly edited from the one found
in the [official repository](https://github.com/LCA-ActivityBrowser/activity-browser/blob/master/recipe/meta.yaml).
Specifically, this recipe is following the conda-forge [suggestion](https://conda-forge.org/docs/maintainer/adding_pkgs.html#tarballs-no-repos)
to use a .tar ball with hash to download instead of grabbing the version
directly from Github.

This recipe can be used to build the conda package locally through the use
of `conda-build`.

## PyInstaller

In order to build a functioning standalone installation of the Activity Browser we use [PyInstaller](https://www.pyinstaller.org/).

Specifically, we use PyInstaller to put together a folder containing all
of the libraries, packages and files required to run the Activity Browser
without explicitly installing anything.

### How to use

- To use the folder created by PyInstaller, all we have to do is double-click the `activity-browser.exe` executable inside the folder itself.


### Requirements for building package

- Create a new Conda environment with the latest activity-browser installed AND a version of pyinstaller of 3.6 or greater, for example:
  ```bash
  conda create -y -n abbuild -c conda-forge -c defaults -c cmutel -c bsteubing -c haasad -c pascallesage activity-browser "pyinstaller>3.6" python=3.7 matplotlib=3.2
  ```
- Activate the new environment with: `conda activate abbuild`
- Move into the `pyinstaller` folder of this repository.
- Call pyinstaller to start the build process: `pyinstaller ./activity-browser.spec`
- PyInstaller will run (and possibly throw out some warnings, but complete the build process anyway).
- PyInstaller will create two folders within the `pyinstaller` directory, a `build` and a `dist` folder.
- The `dist` folder contains the `activity-browser` folder with all of the required executables and libraries.

## Conda Constructor

_TODO_