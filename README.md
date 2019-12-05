# Sygnal 
Sygnal is a hybrid wireless network simulation

## Project structure

`server/` contains the Flask REST API code. 

`client/` is a React app initiated with [CRA](https://create-react-app.dev) that controls the views of the app as a whole 

## Development Setup

We will walkthrough how to setup the development environment

### Pre-Requirements

In order to start contributing, you will need `Python v3.6+`

### Packages
First, we'll need to install some packages to work with the app

<details>
  <summary>Linux</summary>
  <p>In your <strong>Debian</strong> based linux distro, run the following: </p> 
  <code>
  <p>$ sudo apt install python3-pip -y </p>
  <p>$ sudo pip3 install virtualenv </p>
  </code>
</details>

<details>
  <summary> macOS & Windows </summary>

  1. Install a VM Emulator from [VirtualBox](https://virtualbox.org)
  2. Then install and boot an Ubuntu (or any Debian) distro
  3. Run the above linux commands after installing the pre-requisite software
</details>

### Dependency Management

To make sure that you can run code without any clashes, intialize a `virtualenv` wrapper for Python. 

```bash
git clone https://github.com/f0cus10/sygnal	  #Clone this repository
python3 -m venv .venv				        #Initialize a virtualenv wrapper at .venv
source .venv/bin/activate			        #Use the virtualenv Python executable
pip -r server/requirements.txt		        #Install the dependencies for the backend
```

Next, we move to the client and setup the dependencies on the client side
```bash
cd client	    #Move into the client directory
npm install	    #Install all dependencies through npm
```

### Script

This is the final step, where you run the commands to start up the backend and front-end

***NOTE:*** For now, this has to be done in two different terminal windows as two separate commands. *Subject to change.*

To intialize the ***backend*** server, from the project root directory, run:
```bash
python server/__init__.py
```
Please make sure that you are running the Python executable from the virtualenv wrapper that you selected at [Dependency Management](#dependency-management)

Next, run the ***frontend*** in a *different* terminal:

```bash
cd client
npm start
```

Now, you can visit the URL of the frontend app to see your app in action!
*Remember* to check that your ports match. It will usually be http://localhost:3000
