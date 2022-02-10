# Template

An app template for elemenary os in python. 
This is highly inspired by [ElementaryPython](https://github.com/mirkobrombin/ElementaryPython).

![Screenshot](https://github.com/malothebault/Template/blob/main/data/assets/screenshot.png)

## 🔧 Requirements
- python3
- libgtk-3-dev
- libgranite-dev 

## 🔧 Installation
On the top right corner of this page, click on the 'Use this template' green button, then:
```bash
git clone https://github.com/<your_username>/<project_name>.git
cd <project_name>
chmod +x init.sh
./init.sh
```
This little script will ask you the project name and your username and will rename the files
accordingly.

Then you can install with:
```bash
sudo python3 setup.py install
```

## 🔧 How to run
```bash
com.github.<your_username>.<project_name>
```

## 🔧 If the schema is not found
```bash
sudo /usr/bin/glib-compile-schemas /usr/share/glib-2.0/schemas/
```
